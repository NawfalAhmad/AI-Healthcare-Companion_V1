from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pytesseract
from PIL import Image
import fitz  # PyMuPDF
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class SymptomInput(BaseModel):
    symptoms: str

class DrugInput(BaseModel):
    drugs: str

class SummarizeInput(BaseModel):
    text: str

# Helper: call OpenAI GPT
def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

# Symptom Checker
@app.post("/check-symptoms/")
async def check_symptoms(data: SymptomInput):
    prompt = f"Analyze these symptoms: {data.symptoms}. Predict possible severity and suggest next steps."
    result = ask_gpt(prompt)
    return {"result": result}

# Drug Interaction Checker
@app.post("/check-drugs/")
async def check_drugs(data: DrugInput):
    prompt = f"Check interactions for these drugs: {data.drugs}. Provide warnings and guidance."
    result = ask_gpt(prompt)
    return {"result": result}

# Medical Document Summarizer
@app.post("/summarize/")
async def summarize_text(data: SummarizeInput):
    prompt = f"Summarize this medical document clearly and concisely:\n{data.text}"
    result = ask_gpt(prompt)
    return {"result": result}

# Upload & analyze medical reports (PDF/Image)
@app.post("/upload-report/")
async def upload_report(file: UploadFile = File(...)):
    ext = file.filename.split('.')[-1].lower()
    text = ""
    if ext in ["png", "jpg", "jpeg", "tiff", "bmp"]:
        image = Image.open(file.file)
        text = pytesseract.image_to_string(image)
    elif ext == "pdf":
        doc = fitz.open(stream=await file.read(), filetype="pdf")
        for page in doc:
            text += page.get_text()
    else:
        return {"result": "Unsupported file type."}

    prompt = f"Analyze this medical report:\n{text}\nProvide a brief summary, possible concerns, and suggested next steps."
    result = ask_gpt(prompt)
    return {"result": result}

# Simple root
@app.get("/")
async def root():
    return {"message": "AI Healthcare Companion Backend Running"}
