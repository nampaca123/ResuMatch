import httpx
from fastapi import HTTPException
import logging

logger = logging.getLogger(__name__)

class TextSender:
    def __init__(self):
        self.spring_boot_url = "http://spring-boot:8080/text"
        
    async def send_text(self, text: str, filename: str):
        try:
            logger.info(f"Attempting to send text for {filename} to Spring Boot server")
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    self.spring_boot_url,
                    json={
                        "text": text,
                        "filename": filename
                    }
                )
                response.raise_for_status()
                logger.info(f"Successfully sent text to Spring Boot server. Response status: {response.status_code}")
                return response.json()
        except Exception as e:
            logger.error(f"Failed to send text to Spring Boot server: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Failed to send text to Spring Boot: {str(e)}")