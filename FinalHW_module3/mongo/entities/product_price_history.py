import random
import uuid
from datetime import timedelta


def generate_product_price_history(db, fake):
    print("start generate_product_price_history")
    collection = db['ProductPriceHistory']
    for _ in range(50):
        product_price_history = {
            "product_id": str(uuid.uuid4()),
            "price_changes": [{
                "date": fake.date_this_year().isoformat(),
                "price": random.randint(3, 100)
            } for _ in range(random.randint(1, 5))],
            "current_price": random.randint(3, 100),
            "currency": random.choice(["USD", "EUR", "RUB"])
        }
        collection.insert_one(product_price_history)
