from fastapi import APIRouter, UploadFile, File, HTTPException
from ..services.pdf_extractor import PDFExtractor
from ..services.text_sender import TextSender
import logging

router = APIRouter(
    prefix="/pdf",
    tags=["pdf"]
)

# PDFExtractor 인스턴스 생성
pdf_extractor = PDFExtractor()
text_sender = TextSender()

logger = logging.getLogger(__name__)

async def process_pdf(file: UploadFile):
    """
    메인 라우터에서 호출되는 PDF 처리 함수
    """
    try:
        logger.info(f"Starting PDF processing for file: {file.filename}")
        
        # 텍스트 추출
        text = await pdf_extractor.extract_text(file)
        logger.info(f"Extracted text from PDF ({len(text)} chars):\n{text[:500]}...")
        
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
        logger.error(f"Error in process_pdf: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process PDF: {str(e)}"
        )