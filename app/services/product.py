from app.database import AsyncSessionLocal
from app.models import Product
from sqlalchemy import select

async def get_product(product_id: int):
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Product).where(Product.id == product_id))
        return result.scalar_one_or_none()

async def list_products():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Product))
        return result.scalars().all()
