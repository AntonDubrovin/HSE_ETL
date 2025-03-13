import random
import uuid
from datetime import timedelta


def generate_user_recommendations(db, fake):
    print("start generate_user_recommendations")
    collection = db['UserRecommendations']
    for _ in range(30):
        user_recommendation = {
            "user_id": str(uuid.uuid4()),
            "recommended_products": [str(uuid.uuid4()) for _ in range(random.randint(1, 5))],
            "last_updated": fake.date_this_year().isoformat()
        }
        collection.insert_one(user_recommendation)
