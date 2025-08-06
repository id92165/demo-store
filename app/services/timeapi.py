import httpx

async def fetch_current_time():
    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.get("https://worldtimeapi.org/api/timezone/Europe/Stockholm")
        if response.status_code == 200:
            data = response.json()
            return {
                "timezone": data.get("timezone"),
                "datetime": data.get("datetime")
            }
        return {"error": "Failed to fetch time"}
