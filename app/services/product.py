from fastapi import APIRouter, HTTPException
from database import AsyncSessionLocal
from models import Product
from sqlalchemy import select

router = APIRouter()

@router.get("/products/{product_id}")
async def get_product(product_id: int):
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Product).where(Product.id == product_id))
        product = result.scalar_one_or_none()
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        return product

@router.get("/products")
async def list_products():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Product))
        return result.scalars().all()
