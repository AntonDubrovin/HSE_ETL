import random
import uuid
from datetime import timedelta


def generate_moderation_queue(db, fake):
    print("start generate_moderation_queue")
    collection = db['ModerationQueue']
    for _ in range(50):
        moderation_queue = {
            "review_id": str(uuid.uuid4()),
            "user_id": str(uuid.uuid4()),
            "product_id": str(uuid.uuid4()),
            "review_text": fake.sentence(),
            "rating": random.randint(1, 5),
            "moderation_status": random.choice(["New", "InProgress", "Deleted", "OK"]),
            "flags": [fake.word() for _ in range(random.randint(1, 5))],
            "submitted_at": fake.date_this_year().isoformat()
        }
        collection.insert_one(moderation_queue)
