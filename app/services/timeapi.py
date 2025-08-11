import httpx

async def fetch_current_time():
    url = "http://worldtimeapi.org/api/timezone/Etc/UTC"
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(url)
            if response.status_code == 200:
                data = response.json()
                return {
                    "timezone": data.get("timezone"),
                    "currentDateTime": data.get("utc_datetime")
                }
            return {"currentDateTime": "Failed to fetch time"}
    except Exception:
        return {"currentDateTime": "Failed to fetch time"}
