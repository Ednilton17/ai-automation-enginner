import asyncio
import time

import httpx


BASE_URL = "http://127.0.0.1:8000"

CONCURRENT_REQUESTS = 10


async def call_health(
    client: httpx.AsyncClient,
    request_id: int
):

    try:

        response = await client.get(
            f"{BASE_URL}/health"
        )

        return {
            "request_id": request_id,
            "status_code": response.status_code,
            "success": response.status_code == 200
        }

    except httpx.HTTPError as exc:

        return {
            "request_id": request_id,
            "status_code": None,
            "success": False,
            "error": str(exc)
        }


async def main():

    start = time.perf_counter()

    async with httpx.AsyncClient(
        timeout=5.0
    ) as client:

        tasks = [
            call_health(client, request_id)
            for request_id
            in range(CONCURRENT_REQUESTS)
        ]

        results = await asyncio.gather(*tasks)

    elapsed = time.perf_counter() - start

    success_count = sum(
        1
        for result in results
        if result["success"]
    )

    failure_count = (
        len(results) - success_count
    )

    print()

    print("=== Concurrency Test ===")

    print(
        f"Requests: {len(results)}"
    )

    print(
        f"Success: {success_count}"
    )

    print(
        f"Failures: {failure_count}"
    )

    print(
        f"Elapsed: {elapsed:.3f}s"
    )

    print()

    for result in results:
        print(result)


if __name__ == "__main__":
    asyncio.run(main())