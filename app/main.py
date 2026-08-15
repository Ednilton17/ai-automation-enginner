from fastapi import FastAPI

app = FastAPI(
    title = "AI Automation Engineer",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "message": "Api de pé"
    }

@app.get("/health")
def health():
    return {
        "status": "UP"
    }