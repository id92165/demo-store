from database import AsyncSessionLocal
from models import Review
from sqlalchemy import select

async def get_reviews(product_id: int):
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Review).where(Review.product_id == product_id))
        return result.scalars().all()
