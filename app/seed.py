import asyncio
from database import engine, Base, AsyncSessionLocal
from models import Product, Inventory, Review

async def seed():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async with AsyncSessionLocal() as session:
        p1 = Product(name="Apple", category="Fruit", price=1.2)
        p2 = Product(name="Milk", category="Dairy", price=2.5)
        p3 = Product(name="Bread", category="Bakery", price=1.5)
        p4 = Product(name="Banana", category="Fruit", price=1.0)
        p5 = Product(name="Cheese", category="Dairy", price=3.5)

        session.add_all([p1, p2, p3, p4, p5])
        await session.flush()

        session.add_all([
            Inventory(product_id=p1.id, store="Main Warehouse", in_stock=120),
            Inventory(product_id=p2.id, store="Branch A", in_stock=45),
            Inventory(product_id=p3.id, store="Branch B", in_stock=0),
            Inventory(product_id=p4.id, store="Main Warehouse", in_stock=30),
            Inventory(product_id=p5.id, store="Branch A", in_stock=60),
        ])

        session.add_all([
            Review(product_id=p1.id, user="Anna", rating=5, comment="Fresh and tasty!"),
            Review(product_id=p1.id, user="John", rating=4, comment="Good apples."),
            Review(product_id=p2.id, user="Maria", rating=3, comment="Too expensive."),
            Review(product_id=p4.id, user="Nick", rating=4, comment="Good bananas."),
        ])

        await session.commit()

asyncio.run(seed())
