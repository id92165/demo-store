from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from database import create_tables
from services.product import router as product_router
from services.aggregator import router as aggregator_router
import os

app = FastAPI()


app.include_router(product_router, prefix="/api")
app.include_router(aggregator_router, prefix="/api/products")



from fastapi.responses import FileResponse
frontend_path = os.path.join(os.path.dirname(__file__), "frontend")
app.mount("/frontend", StaticFiles(directory=frontend_path, html=True), name="frontend")

@app.get("/")
async def root():
    return FileResponse(os.path.join(frontend_path, "index.html"))


@app.on_event("startup")
async def startup():
    await create_tables()