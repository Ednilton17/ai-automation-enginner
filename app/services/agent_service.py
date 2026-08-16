import asyncio
import time

class AgentService:
    async def run(self, message: str) -> str:

        await asyncio.sleep(1)  # Simulate some processing delay
        #time.sleep(1.5)  # Simulate some processing delay
        return f"Agent received: {message}"