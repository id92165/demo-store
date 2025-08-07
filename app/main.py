from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from database import create_tables
from services.products import router as product_router
import os

app = FastAPI()

app.include_router(product_router)


frontend_path = os.path.join(os.path.dirname(__file__), "frontend")
app.mount("/frontend", StaticFiles(directory=frontend_path, html=True), name="frontend")


@app.on_event("startup")
def startup():
    create_tables()