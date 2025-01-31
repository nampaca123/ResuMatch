import PyPDF2
import io
import logging
from fastapi import UploadFile

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PDFExtractor:
    def __init__(self):
        pass
        
    async def extract_text(self, file: UploadFile) -> str:
        """메인 텍스트 추출 함수"""
        try:
            # 파일을 바이트로 읽기
            contents = await file.read()
            text = await self._process_pdf(contents)
            return text
        except Exception as e:
            logger.error(f"Error processing PDF: {str(e)}")
            raise

    async def _process_pdf(self, pdf_bytes: bytes) -> str:
        """PDF 처리 및 텍스트 추출"""
        try:
            # 바이트 스트림으로 PDF 읽기
            pdf_file = io.BytesIO(pdf_bytes)
            reader = PyPDF2.PdfReader(pdf_file)
            
            # 전체 페이지의 텍스트 추출
            extracted_texts = []
            total_pages = len(reader.pages)
            
            logger.info(f"Processing PDF with {total_pages} pages")
            
            for page_num in range(total_pages):
                page = reader.pages[page_num]
                text = page.extract_text()
                
                if text.strip():  # 빈 페이지가 아닌 경우만 추가
                    extracted_texts.append(text.strip())
                    
                logger.info(f"Processed page {page_num + 1}/{total_pages}")
            
            # 모든 텍스트 합치기
            final_text = '\n\n'.join(extracted_texts)
            logger.info(f"Extracted text length: {len(final_text)}")
            
            return final_text
            
        except Exception as e:
            logger.error(f"Error in _process_pdf: {str(e)}")
            raise