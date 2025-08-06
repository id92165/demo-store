from fastapi import FastAPI
from services.aggregator import router as product_router

app = FastAPI(title="Grocery Store API")

app.include_router(product_router, prefix="/product", tags=["Product Pages"])
