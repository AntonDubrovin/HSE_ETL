import random
import uuid
from datetime import timedelta


def generate_user_sessions(db, fake):
    print("start generate_user_sessions")
    collection = db['UserSessions']
    for _ in range(100):
        user_session = {
            "session_id": str(uuid.uuid4()),
            "user_id": str(uuid.uuid4()),
            "start_time": fake.date_time_this_month().isoformat(),
            "end_time": fake.date_time_this_month() + timedelta(minutes=30),
            "pages_visited": [fake.uri_path() for _ in range(random.randint(3, 10))],
            "device": {
                "type": random.choice(["mobile", "desktop", "tablet"]),
                "os": random.choice(["Android", "iOS", "Windows"])
            },
            "actions": ["login", "search"] + random.choices(["search", "add_to_cart"], k=3) + ["logout"]
        }
        collection.insert_one(user_session)
