from fastapi import APIRouter, UploadFile, File, HTTPException
from ..services.pdf_extractor import PDFExtractor

router = APIRouter(
    prefix="/pdf",
    tags=["pdf"]
)

# PDFExtractor 인스턴스 생성
pdf_extractor = PDFExtractor()

async def process_pdf(file: UploadFile):
    """
    메인 라우터에서 호출되는 PDF 처리 함수
    """
    try:
        text = await pdf_extractor.extract_text(file)
        return {
            "filename": file.filename,
            "text": text,
            "status": "success"
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process PDF: {str(e)}"
        )

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """
    직접 PDF 업로드 엔드포인트 (필요한 경우 사용)
    """
    return await process_pdf(file)