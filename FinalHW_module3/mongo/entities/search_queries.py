import random
import uuid
from datetime import timedelta


def generate_search_queries(db, fake):
    print("start generate_search_queries")
    collection = db["SearchQueries"]
    for _ in range(50):
        search_query = {
            "query_id": str(uuid.uuid4()),
            "user_id": str(uuid.uuid4()),
            "query_text": fake.sentence(),
            "timestamp": fake.date_this_year().isoformat(),
            "filters": [fake.word() for _ in range(random.randint(1, 5))],
            "results_count": random.randint(0, 100)
        }
        collection.insert_one(search_query)
