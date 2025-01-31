from fastapi import APIRouter, UploadFile, File, HTTPException
from ..services.image_extractor import ImageExtractor
from ..services.text_sender import TextSender
import logging

router = APIRouter(
    prefix="/image",
    tags=["image"]
)

# ImageExtractor 인스턴스 생성
image_extractor = ImageExtractor()
text_sender = TextSender()

logger = logging.getLogger(__name__)

async def process_image(file: UploadFile):
    """
    메인 라우터에서 호출되는 이미지 처리 함수
    """
    try:
        logger.info(f"Starting image processing for file: {file.filename}")
        
        # 텍스트 추출
        text = await image_extractor.extract_text(file)
        logger.info(f"Extracted text from image ({len(text)} chars):\n{text[:500]}...")
        
        # Spring Boot 서버로 전송
        logger.info("Sending text to Spring Boot server...")
        await text_sender.send_text(text, file.filename)
        logger.info("Successfully sent text to Spring Boot server")
        
        return {
            "filename": file.filename,
            "text": text,
            "status": "success"
        }
    except Exception as e:
        logger.error(f"Error in process_image: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process image: {str(e)}"
        )