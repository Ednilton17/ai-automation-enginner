from fastapi import FastAPI
from app.api.agent_router import router as agent_router

app = FastAPI(
    title = "AI Automation Engineer",
    version="0.1.0"
)
app.include_router(agent_router)

@app.get("/health")
def health():
    return {
        "status": "UP"
    }