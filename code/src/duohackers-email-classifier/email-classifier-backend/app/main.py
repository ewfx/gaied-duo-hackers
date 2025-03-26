from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.classifier import router as classifier_router

app = FastAPI(title="Email Classifier API")

# Enable CORS for Angular frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Allow Angular app
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (POST, GET, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(classifier_router)

@app.get("/")
def home():
    return {"message": "Email Classifier API is running!"}
