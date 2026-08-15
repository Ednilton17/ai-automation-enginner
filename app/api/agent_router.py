from fastapi import APIRouter

from app.schemas.agent import AgentRequest, AgentResponse
from app.services.agent_service import AgentService

router = APIRouter(
    prefix="/api/v1/agent",
    tags=["agent"]
)

agent_service = AgentService()

@router.post("/run", 
    response_model=AgentResponse
)

def run_agent(request: AgentRequest)-> AgentResponse:

    response = agent_service.run(request.message)

    return AgentResponse(
        response=response
    )