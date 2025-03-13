import random
import uuid
from datetime import timedelta


def generate_support_tickets(db, fake):
    print("start generate_support_tickets")
    collection = db['SupportTickets']
    for _ in range(100):
        created_at = fake.date_this_year()
        support_ticket = {
            "ticket_id": str(uuid.uuid4()),
            "user_id": str(uuid.uuid4()),
            "status": random.choice(["Registered", "Reject", "Resolved"]),
            "issue_type": random.choice(["Login", "Password", "BUG"]),
            "messages": fake.sentence(),
            "created_at": created_at.isoformat(),
            "updated_at": fake.date_between(start_date=created_at, end_date='today').isoformat()
        }
        collection.insert_one(support_ticket)
