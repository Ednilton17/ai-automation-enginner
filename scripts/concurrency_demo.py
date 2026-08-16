import asyncio
import time

import httpx


URL = "http://localhost:8000/api/v1/agent/run"


async def call_agent(client: httpx.AsyncClient, number: int):

    response = await client.post(
        URL,
        json={
            "message": f"Request {number}"
        }
    )

    return response.json()


async def main():

    start = time.perf_counter()

    async with httpx.AsyncClient(timeout=10.0) as client:

        tasks = [
            call_agent(client, number)
            for number in range(1, 6)
        ]

        responses = await asyncio.gather(*tasks)

    elapsed = time.perf_counter() - start

    for response in responses:
        print(response)

    print(
        f"\nTotal execution time: {elapsed:.2f} seconds"
    )

if __name__ == "__main__":
    asyncio.run(main())