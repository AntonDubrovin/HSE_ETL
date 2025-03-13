import random
import uuid
from datetime import timedelta


def generate_event_logs(db, fake):
    print("start generate_event_logs")
    collection = db['EventLogs']
    for _ in range(200):
        event_log = {
            "event_id": str(uuid.uuid4()),
            "timestamp": fake.date_time_this_year(),
            "event_type": random.choice(["login", "search", "add_to_cart", "logout"]),
            "details": fake.sentence()
        }
        collection.insert_one(event_log)
