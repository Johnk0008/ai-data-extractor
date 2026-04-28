from fastapi import FastAPI, UploadFile
import shutil
import pandas as pd

from parser import parse_pdf, parse_excel, parse_csv
from pipeline import clean_data
from validator import validate_data
from llm_module import extract_with_llm

app = FastAPI()

@app.post("/process/")
async def process_file(file: UploadFile):
    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    if file.filename.endswith(".pdf"):
        text = parse_pdf(file_path)
        result = extract_with_llm(text)
        return {"llm_output": result}

    elif file.filename.endswith(".xlsx"):
        df = parse_excel(file_path)

    elif file.filename.endswith(".csv"):
        df = parse_csv(file_path)

    else:
        return {"error": "Unsupported file type"}

    df = clean_data(df)
    errors = validate_data(df)

    output_path = "output.csv"
    df.to_csv(output_path, index=False)

    return {
        "message": "File processed successfully",
        "errors": errors,
        "output_file": output_path
    }