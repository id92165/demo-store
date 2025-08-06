from database import AsyncSessionLocal
from models import Inventory
from sqlalchemy import select

async def get_inventory(product_id: int):
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Inventory).where(Inventory.product_id == product_id))
        return result.scalar_one_or_none()
