import easyocr
import numpy as np
import cv2
from PIL import Image
import pytesseract
import io
import logging
from fastapi import UploadFile

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ImageExtractor:
    def __init__(self):
        self.reader = easyocr.Reader(['en'])
        # Tesseract 설정 (필요한 경우)
        # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows의 경우
        
    async def extract_text(self, file: UploadFile) -> str:
        """메인 텍스트 추출 함수"""
        try:
            # 파일을 바이트로 읽기
            contents = await file.read()
            text = await self._process_image(contents)
            return text
        except Exception as e:
            logger.error(f"Error processing image: {str(e)}")
            raise

    async def _process_image(self, image_bytes: bytes) -> str:
        """이미지 처리 및 텍스트 추출"""
        try:
            # 이미지 로드
            nparr = np.frombuffer(image_bytes, np.uint8)
            image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            # 이미지 전처리
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            denoised = cv2.fastNlMeansDenoising(gray)
            
            # 대비 향상
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
            enhanced = clahe.apply(denoised)
            
            # 이진화
            _, binary = cv2.threshold(enhanced, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            
            # EasyOCR로 텍스트 영역 감지
            regions = self.reader.readtext(
                binary,
                paragraph=False,
                detail=1,
                min_size=10,
                text_threshold=0.2,
                width_ths=0.7,
                height_ths=0.7
            )
            
            logger.info(f"Found {len(regions)} text regions")
            
            # 결과 텍스트를 저장할 리스트
            extracted_texts = []
            
            # 각 영역별로 Tesseract OCR 수행
            for region in regions:
                bbox = np.array(region[0], np.int32)
                
                # 영역 좌표 계산 (패딩 포함)
                padding = 5
                x_min, y_min = bbox.min(axis=0)
                x_max, y_max = bbox.max(axis=0)
                
                x_min = max(0, int(x_min - padding))
                y_min = max(0, int(y_min - padding))
                x_max = min(binary.shape[1], int(x_max + padding))
                y_max = min(binary.shape[0], int(y_max + padding))
                
                # 영역 추출
                region_img = binary[y_min:y_max, x_min:x_max]
                
                # Tesseract OCR 수행
                text = pytesseract.image_to_string(
                    region_img,
                    config='--psm 6'  # PSM 6: Uniform block of text
                )
                
                if text.strip():  # 빈 문자열이 아닌 경우만 추가
                    extracted_texts.append(text.strip())
            
            # 모든 텍스트 합치기
            final_text = ' '.join(extracted_texts)
            logger.info(f"Extracted text length: {len(final_text)}")
            
            return final_text
            
        except Exception as e:
            logger.error(f"Error in _process_image: {str(e)}")
            raise

    def _enhance_image_quality(self, image):
        """추가적인 이미지 품질 향상이 필요한 경우를 위한 메서드"""
        # 필요한 경우 구현
        pass