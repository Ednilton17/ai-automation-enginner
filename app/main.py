from fastapi import FastAPI
from app.api.agent_router import router as agent_router
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title = "AI Automation Engineer",
    version="0.1.0",
    debug=settings.debug
)

app.include_router(agent_router)

@app.get("/health")
def health():
    return {
        "status": "UP",
        "environment": settings.environment
    }