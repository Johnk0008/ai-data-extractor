import pandas as pd
import pdfplumber

def parse_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def parse_excel(file_path):
    return pd.read_excel(file_path)

def parse_csv(file_path):
    return pd.read_csv(file_path)