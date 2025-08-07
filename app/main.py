from fastapi import FastAPI
from services.aggregator import router as product_router
from fastapi.staticfiles import StaticFiles
import os


frontend_path = os.path.join(os.path.dirname(__file__), "frontend")
app.mount("/frontend", StaticFiles(directory=frontend_path, html=True), name="frontend")

app = FastAPI(title="Grocery Store API")

app.include_router(product_router, prefix="/product", tags=["Product Pages"])
