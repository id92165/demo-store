from fastapi import APIRouter, HTTPException
from database import AsyncSessionLocal
from models import Product
from sqlalchemy import select
from sqlalchemy.orm import selectinload
import asyncio

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

@router.get("/product-city")
async def get_product_city(product_id: int):
    # Simulate high CPU load with 20-second delay for product ID 3
    if product_id == 3:
        await asyncio.sleep(20)
    
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Product).where(Product.id == product_id))
        product = result.scalar_one_or_none()
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        
        return {"product_id": product_id, "product_name": product.name, "city": "Krakow"}

@router.get("/product-price")
async def get_product_price(product_id: int):
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Product).where(Product.id == product_id))
        product = result.scalar_one_or_none()
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        return {"product_id": product_id, "product_name": product.name, "price": product.price}

@router.get("/product-review-count")
async def get_product_review_count(product_name: str):
    return {"product_name": product_name, "review_count": 42}

@router.get("/product-average-rating")
async def get_product_average_rating(product_name: str):
    return {"product_name": product_name, "average_rating": 4.7}

@router.get("/product-category")
async def get_product_category(product_id: int):
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Product).where(Product.id == product_id))
        product = result.scalar_one_or_none()
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        return {"product_id": product_id, "product_name": product.name, "category": product.category}

@router.get("/product-stock")
async def get_product_stock(product_id: int):
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Product).options(selectinload(Product.inventory)).where(Product.id == product_id)
        )
        product = result.scalar_one_or_none()
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        
        stock = product.inventory.in_stock if product.inventory else 0
        return {"product_id": product_id, "product_name": product.name, "stock": stock}

@router.get("/product-availability")
async def get_product_availability(product_id: int):
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Product).options(selectinload(Product.inventory)).where(Product.id == product_id)
        )
        product = result.scalar_one_or_none()
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        
        stock = product.inventory.in_stock if product.inventory else 0
        availability = "In Stock" if stock > 0 else "Out of Stock"
        return {"product_id": product_id, "product_name": product.name, "availability": availability}
