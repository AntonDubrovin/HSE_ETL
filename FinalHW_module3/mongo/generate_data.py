from pymongo import MongoClient
from faker import Faker
from mongo.entities.event_logs import generate_event_logs
from mongo.entities.moderation_queue import generate_moderation_queue
from mongo.entities.product_price_history import generate_product_price_history
from mongo.entities.search_queries import generate_search_queries
from mongo.entities.support_tickets import generate_support_tickets
from mongo.entities.user_recommendations import generate_user_recommendations
from mongo.entities.user_sessions import generate_user_sessions

fake = Faker()
client = MongoClient('mongodb://localhost:27017/')
db = client['ecommerce']

if __name__ == "__main__":
    print("start generate datas")
    generate_user_sessions(db, fake)
    generate_product_price_history(db, fake)
    generate_event_logs(db, fake)
    generate_support_tickets(db, fake)
    generate_user_recommendations(db, fake)
    generate_moderation_queue(db, fake)
    generate_search_queries(db, fake)

    collections = ["UserSessions", "ProductPriceHistory", "EventLogs", "SupportTickets", "UserRecommendations",
                   "ModerationQueue", "SearchQueries"]
    for collection in collections:
        print('##########')
        print(collection)
        print(db[collection].count_documents({}))
        documents = db[collection].find().limit(2)
        for document in documents:
            print(document)

    print("Данные успешно сгенерированы!")
