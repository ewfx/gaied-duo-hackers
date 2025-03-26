# Email Classifier - Backend

## 📌 Project Overview
Email Classifier - Backend project automates **email classification & field extraction**. 

It supports:

✅ **Classification of emails & attachments** into predefined **request/sub-request types**  
✅ **Dynamic field extraction** based on email context (e.g., Loan Amount, Account Number)  
✅ **Duplicate email detection** using AI-driven semantic similarity  
✅ **Scalable API for real-time processing**  

## 🏗️ Tech Stack
- **Backend:** FastAPI (Python)
- **AI Models:** BART, BERT-NER, Sentence Transformers
- **Libraries:** `pdfplumber`, `textract`, `transformers`, `scikit-learn`
- **Storage:** Local (can be integrated with databases)
- **Deployment:** Docker-ready

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/ewfx/gaied-duo-hackers.git
cd gaied-duo-hackers\code\src\duohackers-email-classifier\email-classifier-backend
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️ Run FastAPI Server
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## 📥 API Endpoints
### 🔹 Upload & Classify Emails
**Endpoint:** `POST /upload/`  
**Payload:** `.eml`, `.pdf`, `.docx` file upload  
**Response:** JSON with classification, extracted fields, and duplicate check  

## 🛠️ Future Enhancements
🔹 Improve request type detection with **domain-specific fine-tuning**  
🔹 Implement **real-time email ingestion** with event-driven architecture

## 👥 Team & Credits
Built by **[DuoHackers]**  
📧 Contact: **sunkara.ratnam@gmail.com**  
💻 GitHub: **[https://github.com/ewfx/gaied-duo-hackers.git](https://github.com/ewfx/gaied-duo-hackers.git)**  


