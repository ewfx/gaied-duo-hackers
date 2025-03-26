# 🚀 Duohackers-email-classifier

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---

## 🎯 Introduction
Duohackers-email-classifier leverages AI & NLP to automate email classification of servicing requests for Commercial Bank Lending Service teams.

It includes:

✅ Classification of emails & attachments into predefined request/sub-request types.  
✅ Handling multi request email with primary intent detection  
✅ Dynamic field extraction based on Request type (e.g. Loan Amount, Account Number etc)  
✅ Duplicate email detection using AI-driven semantic similarity  
✅ Request type management for dynamic workflows  

## 🎥 Demo
🔗 [Live Demo](#) (if applicable)  
📹 [Video Demo](#) (if applicable)  
🖼️ Screenshots:

![Screenshot 1](link-to-image)

## 💡 Inspiration
This project was inspired by real-world banking & finance challenges where:  
✅ Manual email processing slows down operations  
✅ Key data (Loan Amount, Account Number, etc.) is buried in attachments  
✅ Duplicate emails create redundant service requests  
✅ Multi-intent emails need better classification  

## ⚙️ What It Does  
1️⃣ AI-Based Email Classification  
✅ Uses Natural Language Processing (NLP) to classify emails based on sender intent.  
✅ Categorizes emails into Loan Requests, Complaints, Document Submissions, Inquiries, etc.  
✅ Multi-label classification supports emails containing multiple request types.  

2️⃣ Smart Field Extraction  
✅ Dynamically extracts key fields (e.g., Loan Amount, Account Number, Expiration Date) from both email body & attachments.  
✅ Uses NER (Named Entity Recognition) + Regex Matching to identify contextual information.  

3️⃣ AI-Powered Duplicate Detection  
✅ Uses Sentence Transformers & Semantic Similarity to detect duplicate emails.  
✅ Identifies redundant requests even if terminology is changed.  

4️⃣ Request Management Dashboard  
✅ Allows users to add, modify, and delete request & sub-request types.  
✅ Provides a structured interface for managing business workflows dynamically.  

5️⃣ Seamless Frontend & API Integration  
✅ Angular UI with a modern, responsive design.  
✅ FastAPI backend for real-time processing with RESTful API endpoints.  
✅ OpenAPI documentation for easy API testing & integration.  

6️⃣ Scalable & Deployment-Ready  
✅ Built using FastAPI + Angular 10+, ensuring high performance & scalability.  
✅ Docker-compatible, making it easy to deploy in cloud or on-premises environments.  

## 🛠️ How We Built It
We built this project using a combination of AI-powered NLP models, a FastAPI backend, and an Angular frontend, ensuring high performance, scalability, and ease of use.

🔹 Backend (FastAPI, Python)
Framework: **FastAPI** 🚀 (Lightweight & High-performance API framework)

AI Models:  
✅ **BART (facebook/bart-large-mnli)** → For multi-label email classification  
✅ **BERT-NER (dslim/bert-base-NER)** → For extracting key fields dynamically  
✅ **Sentence Transformers (all-MiniLM-L6-v2)** → For duplicate detection using semantic similarity  

Libraries Used:

**transformers** → NLP models for classification & extraction

**pdfplumber, textract** → Extract text from PDF, DOCX, and EML attachments

**scikit-learn** → AI model enhancements & preprocessing

**uvicorn** → FastAPI server deployment

🔹 Frontend (Angular)
Framework: **Angular** (Scalable & Responsive UI)

Styling: Bootstrap 5 + SCSS for a modern, clean UI

State Management: Local component-based

API Integration: HTTPClientModule for connecting to FastAPI

🔹 Additional Tools
Postman → API Testing & Debugging

Docker → Containerized deployment for scalability

GitHub → Version control & collaboration

## 🚧 Challenges We Faced
During development, our team encountered several technical and non-technical challenges. Here’s how we tackled them:

1️⃣ Handling Emails with Attachments (Technical Challenge)
📌 Problem:

Many important details (Loan Amount, Account Number, etc.) were inside PDFs, DOCX files, and email attachments, making extraction difficult.

Parsing different file types required multiple extraction techniques.

💡 Solution:  
✅ Integrated pdfplumber, textract, and email.parser to extract text from different document types.  
✅ Prioritized email body over attachments to prevent misclassification.  
✅ Used OCR-based extraction (future scope) for scanned documents.  

2️⃣ Improving Classification Accuracy (Technical Challenge)
📌 Problem:

The initial AI model sometimes misclassified multi-intent emails or struggled with ambiguous wording.

💡 Solution:  
✅ Implemented a two-step classification approach → First, detect high-level request type, then classify subcategories.  
✅ Fine-tuned the BART model with additional domain-specific email datasets.  
✅ Added confidence scoring to filter out low-confidence classifications.  

3️⃣ Detecting Duplicate Emails Effectively (Technical Challenge)
📌 Problem:

Simple text matching didn’t work well, as request emails used different wording but had the same intent.

💡 Solution:  
✅ Used Sentence Transformers & Semantic Similarity to compare the meaning of emails rather than exact text.  
✅ Set a similarity threshold (85%) to identify duplicates even when phrased differently.  

4️⃣ Coordination & Time Constraints (Non-Technical Challenge)
📌 Problem:

With tight hackathon deadlines, we had to balance development, debugging, and documentation while working remotely.

💡 Solution:  
✅ Divided tasks efficiently (Frontend, Backend, AI Model, Testing).  

## 🏃 How to Run
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/ewfx/gaied-duo-hackers.git
cd gaied-duo-hackers\code\src\duohackers-email-classifier\
```

### 2️⃣ Backend Setup
```sh
cd email-classifier-backend
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 3️⃣ Frontend Setup
```sh
cd email-classifier-frontend
npm install
ng serve --open
```
📌 Open UI: **[http://localhost:4200](http://localhost:4200)**


## 🏗️ Tech Stack

### 🖥️ Backend (FastAPI, Python)
- **API Framework:** FastAPI
- **AI Models:** BART, BERT-NER, Sentence Transformers
- **Libraries:** `pdfplumber`, `textract`, `transformers`, `scikit-learn`

### 🖥️ Frontend (Angular 10+)
- **Framework:** Angular 10+
- **Styling:** Bootstrap 5, Custom SCSS
- **State Management:** Local component-based
- **API Integration:** FastAPI backend (via `HttpClient`)

## 👥 Team : DuoHackers
- **Sunkara Swathi Venkata Ratnam(u810271)**
- **Adduri Shiva Kiran (u781829)** 
