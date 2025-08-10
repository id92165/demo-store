import httpx

async def fetch_usd_to_eur():
    url = "https://api.frankfurter.app/latest?from=USD&to=EUR"
    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            rate = data.get("rates", {}).get("EUR")
            return rate if rate else None
        return None
