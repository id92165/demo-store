from fastapi import APIRouter, HTTPException
from services.product import get_product, list_products
from services.inventory import get_inventory
from services.reviews import get_reviews
from services.timeapi import fetch_current_time
from services.currency import fetch_usd_to_eur

router = APIRouter()

@router.get("/")
async def get_product_list():
    products = await list_products()
    return [
        {
            "id": p.id,
            "name": p.name,
            "category": p.category,
            "price": p.price
        } for p in products
    ]

@router.get("/{product_id}/full")
async def get_full_product(product_id: int):
    product = await get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    inventory = await get_inventory(product_id)
    reviews = await get_reviews(product_id)
    external_time = await fetch_current_time()
    rate = await fetch_usd_to_eur()
    price_eur = round(product.price * rate, 2) if rate else None

    avg_rating = round(sum(r.rating for r in reviews) / len(reviews), 1) if reviews else None

    return {
        "external_time_api": external_time,
        "product": {
            "id": product.id,
            "name": product.name,
            "category": product.category,
            "price": product.price,
            "price_eur": price_eur
        },
        "inventory": {
            "store": inventory.store,
            "in_stock": inventory.in_stock
        } if inventory else None,
        "reviews": [
            {
                "user": r.user,
                "rating": r.rating,
                "comment": r.comment
            } for r in reviews
        ],
        "summary": {
            "review_count": len(reviews),
            "average_rating": avg_rating,
            "availability": "In stock" if inventory and inventory.in_stock > 0 else "Out of stock"
        }
    }
