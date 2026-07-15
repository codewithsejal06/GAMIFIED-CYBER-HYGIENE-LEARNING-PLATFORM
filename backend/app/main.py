from fastapi import FastAPI

app = FastAPI(
    title="CyberVerse AI API",
    description="Backend API for the Gamified Cyber Hygiene Learning Platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to CyberVerse AI 🚀",
        "status": "Backend Running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "CyberVerse AI Backend"
    }