import httpx

async def fetch_current_time():
    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.get("http://worldclockapi.com/api/json/utc/now")
        if response.status_code == 200:
            data = response.json()
            return {
                "timezone": data.get("timezone"),
                "currentDateTime": data.get("currentDateTime")
            }
        return {"error": "Failed to fetch time"}
