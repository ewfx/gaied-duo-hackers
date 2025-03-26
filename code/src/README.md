# 🚀 AI-Powered Email Classification & Request Management

## 📌 Project Overview
This project leverages **AI & NLP** to automate **email classification and request management**. 
It includes:

✅ **Classification of emails & attachments into predefined request/sub-request types**  
✅ **Handling multi request email with primary intent detection** 
✅ **Dynamic field extraction based on Request type (e.g. Loan Amount, Account Number etc)**  
✅ **Duplicate email detection using AI-driven semantic similarity**  
✅ **Request type management for dynamic workflows**  

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

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/ewfx/gaied-duo-hackers.git
cd gaied-duo-hackers\code\src\duohackers-email-classifier\
```

### 2️⃣ Backend Setup
```sh
email-classifier-backend
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

## 🖥️ Features & Navigation
### 🔹 **Email Classification**
- Upload `.eml`, `.pdf`, `.docx` files
- View classification & extracted fields
- Detect duplicate requests & display alerts

### 🔹 **Request Type Management**
- Add/Edit/Delete request & sub-request types
- Seamless UI for managing workflows

## 🎨 UI Enhancements
🔹 **Modern navbar for easy navigation**  
🔹 **Responsive design with smooth transitions**  
🔹 **Consistent theme across screens**  

## 🚀 Future Enhancements
🔹 **Role-based access for admin users**  
🔹 **Real-time API sync for instant updates**
