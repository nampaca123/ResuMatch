from fastapi import APIRouter, UploadFile, File, HTTPException
from ..services.image_extractor import ImageExtractor

router = APIRouter(
    prefix="/image",
    tags=["image"]
)

# ImageExtractor 인스턴스 생성
image_extractor = ImageExtractor()

async def process_image(file: UploadFile):
    """
    메인 라우터에서 호출되는 이미지 처리 함수
    """
    try:
        text = await image_extractor.extract_text(file)
        return {
            "filename": file.filename,
            "text": text,
            "status": "success"
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process image: {str(e)}"
        )

@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    """
    직접 이미지 업로드 엔드포인트 (필요한 경우 사용)
    """
    return await process_image(file)
