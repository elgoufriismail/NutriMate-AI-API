from fastapi import FastAPI, File
import cv2
import io
from PIL import Image
import numpy as np
import pytesseract


app = FastAPI()


@app.post("/ocr")
async def ocr(file: bytes = File(...)):
    img = Image.open(io.BytesIO(file))
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(img)
    return text
