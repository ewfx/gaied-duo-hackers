import os
import json
import email
import pdfplumber
import textract
import hashlib
import re
from fastapi import APIRouter, FastAPI, File, UploadFile
from transformers import pipeline
from typing import List, Dict
from transformers import AutoModelForTokenClassification, AutoTokenizer
import torch
from sentence_transformers import SentenceTransformer, util

router = APIRouter(prefix="/upload", tags=["Classification"])
app = FastAPI()

# Pretrained transformer model for classification
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Pretrained transformer model for Named Entity Recognition (NER)
ner_model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
ner_tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
ner_pipeline = pipeline("ner", model=ner_model, tokenizer=ner_tokenizer, aggregation_strategy="simple")

# Sentence Transformer model for semantic similarity
similarity_model = SentenceTransformer("all-MiniLM-L6-v2")

# Define categories and subcategories with expected field extractions
CATEGORIES = {
    "Loan Request": {
        "subcategories": ["New Loan", "Loan Extension", "Loan Modification"],
        "fields": ["ACCOUNT_NUMBER", "LOAN_AMOUNT", "REPAYMENT_PERIOD", "LOAN_TYPE"]
    },
    "Document Submission": {
        "subcategories": ["KYC Documents", "Financial Statements", "Collateral Documents"],
        "fields": ["DOCUMENT_TYPE", "SUBMISSION_DATE", "CUSTOMER_ID"]
    },
    "General Inquiry": {
        "subcategories": ["Interest Rates", "Repayment Schedule", "Eligibility Criteria"],
        "fields": ["INTEREST_RATE", "SCHEDULE_DATE", "LOAN_TERM"]
    },
    "Complaint": {
        "subcategories": ["Service Issue", "Loan Processing Delay", "Incorrect Charges"],
        "fields": ["ISSUE_DESCRIPTION", "REFERENCE_NUMBER", "COMPLAINT_STATUS"]
    }
}

CONFIDENCE_THRESHOLD = 0.7  # Show only classifications with confidence >= 70%
SIMILARITY_THRESHOLD = 0.85  # Identify duplicates with semantic similarity >= 85%

seen_texts = []  # Store previous email embeddings for similarity comparison

# Function to extract text from different file types
def extract_text_from_file(file_path: str) -> str:
    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            return " ".join([page.extract_text() or "" for page in pdf.pages])
    elif file_path.endswith(".docx") or file_path.endswith(".txt"):
        return textract.process(file_path).decode("utf-8")
    return ""

# Function to parse .eml files and extract email + attachment text
def extract_text_from_eml(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        msg = email.message_from_file(f)
    text = []
    for part in msg.walk():
        if part.get_content_type() == "text/plain":
            text.append(part.get_payload(decode=True).decode(errors="ignore"))
        elif part.get_content_disposition() == "attachment":
            filename = part.get_filename()
            if filename and filename.endswith((".pdf", ".docx", ".txt")):
                attachment_path = f"temp_{filename}"
                with open(attachment_path, "wb") as att_file:
                    att_file.write(part.get_payload(decode=True))
                text.append(extract_text_from_file(attachment_path))
                os.remove(attachment_path)
    return " ".join(text)

# Function to classify email content
def classify_email(content: str) -> Dict:
    flattened_labels = sum([cat["subcategories"] for cat in CATEGORIES.values()], [])
    result = classifier(content, flattened_labels, multi_label=True)
    
    classified_results = {}
    primary_request = None
    
    for label, score in zip(result["labels"], result["scores"]):
        if score >= CONFIDENCE_THRESHOLD:
            for category, details in CATEGORIES.items():
                if label in details["subcategories"]:
                    classified_results.setdefault(category, []).append({"subcategory": label, "confidence": score})
    
    if classified_results:
        primary_request = max(classified_results.items(), key=lambda x: max(sub["confidence"] for sub in x[1]))[0]
    
    return {"classification": classified_results, "primary_request": primary_request}

# Function to detect duplicate emails using semantic similarity
def is_duplicate(content: str) -> bool:
    global seen_texts
    content_embedding = similarity_model.encode(content, convert_to_tensor=True)
    
    for prev_embedding in seen_texts:
        similarity_score = util.pytorch_cos_sim(content_embedding, prev_embedding).item()
        if similarity_score >= SIMILARITY_THRESHOLD:
            return True
    
    seen_texts.append(content_embedding)
    return False

# Function to extract key fields dynamically using regex & NER
def extract_fields(content: str, primary_request: str) -> Dict:
    fields = {}
    if not primary_request or primary_request not in CATEGORIES:
        return fields
    
    expected_fields = CATEGORIES[primary_request]["fields"]
    ner_results = ner_pipeline(content)
    
    for entity in ner_results:
        label = entity['entity_group']
        text = entity['word']
        if label in expected_fields:
            fields[label] = text
    
    # Additional regex-based extraction
    regex_patterns = {
        "ACCOUNT_NUMBER": r"(?:Account|Acct)\s*Number\s*[:\-]?\s*(\d+)",
        "LOAN_AMOUNT": r"(?:Loan|Amount)\s*[:\-]?\s*(\d+[,.]?\d*)",
        "REFERENCE_NUMBER": r"(?:Reference|Ref)\s*Number\s*[:\-]?\s*(\w+)"
    }
    
    for field, pattern in regex_patterns.items():
        match = re.search(pattern, content, re.IGNORECASE)
        if match and field in expected_fields:
            fields[field] = match.group(1)
    
    return fields

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    
    if file.filename.endswith(".eml"):
        content = extract_text_from_eml(file_path)
    else:
        content = extract_text_from_file(file_path)
    
    os.remove(file_path)
    
    if is_duplicate(content):
        return {"error": "Duplicate email detected (Semantic Match)"}
    
    classification_result = classify_email(content)
    extracted_fields = extract_fields(content, classification_result["primary_request"])
    
    return {"filename": file.filename, "classification": classification_result, "extracted_fields": extracted_fields}
