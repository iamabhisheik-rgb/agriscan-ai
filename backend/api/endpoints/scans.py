from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os
from services.ai_engine import analyze_plant_image

router = APIRouter()

@router.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image.")
    
    temp_file_path = f"temp_{file.filename}"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    try:
        with open(temp_file_path, "rb") as img_file:
            image_bytes = img_file.read()
            
        diagnosis = analyze_plant_image(image_bytes)
        return diagnosis
        
    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)