from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import magic
from .routers import pdf_router, image_router

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 환경에서는 구체적인 도메인을 지정하세요
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # 파일 타입 확인
    content_type = magic.from_buffer(await file.read(1024), mime=True)
    await file.seek(0)  # 파일 포인터를 다시 처음으로
    
    if content_type == "application/pdf":
        return await pdf_router.process_pdf(file)
    elif content_type.startswith("image/"):
        return await image_router.process_image(file)
    else:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type. Only PDF and image files are allowed."
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)