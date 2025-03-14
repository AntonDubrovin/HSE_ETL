from pymongo import MongoClient
import psycopg2
import json
from datetime import datetime


def transfer_collection(mongo_db, mongo_collection, pg_table, pg_columns):
    try:
        data = list(mongo_db[mongo_collection].find())

        pg_conn = psycopg2.connect(
            dbname='airflow',
            user='airflow',
            password='airflow',
            host='postgres-airflow'
        )
        pg_cursor = pg_conn.cursor()

        for doc in data:
            doc.pop('_id', None)

            values = []
            for field in pg_columns:
                value = doc.get(field)
                if isinstance(value, (dict, list)):
                    value = json.dumps(value, ensure_ascii=False, default=str)
                values.append(value)

            query = f"""
                INSERT INTO {pg_table} ({', '.join(pg_columns)})
                VALUES ({', '.join(['%s'] * len(values))})
                ON CONFLICT DO NOTHING;
            """
            pg_cursor.execute(query, values)
    except Exception as e:
        pg_conn.rollback()
        print(f"Ошибка при репликации {mongo_collection}: {str(e)}")
    else:
        pg_conn.commit()
        print(f"Репликация {mongo_collection} -> {pg_table} завершена. Записей: {len(data)}")
    finally:
        pg_cursor.close()
        pg_conn.close()


def transfer_all_data():
    mongo_client = MongoClient('mongodb://mongo:27017/')
    mongo_db = mongo_client['ecommerce']

    transfer_collection(
        mongo_db=mongo_db,
        mongo_collection='UserSessions',
        pg_table='user_sessions',
        pg_columns=['session_id', 'user_id', 'start_time', 'end_time', 'pages_visited', 'device', 'actions']
    )

    transfer_collection(
        mongo_db=mongo_db,
        mongo_collection='ProductPriceHistory',
        pg_table='product_price_history',
        pg_columns=['product_id', 'price_changes', 'current_price', 'currency']
    )

    transfer_collection(
        mongo_db=mongo_db,
        mongo_collection='EventLogs',
        pg_table='event_logs',
        pg_columns=['event_id', 'timestamp', 'event_type', 'details']
    )

    transfer_collection(
        mongo_db=mongo_db,
        mongo_collection='SupportTickets',
        pg_table='support_tickets',
        pg_columns=['ticket_id', 'user_id', 'status', 'issue_type', 'messages', 'created_at', 'updated_at']
    )

    transfer_collection(
        mongo_db=mongo_db,
        mongo_collection='UserRecommendations',
        pg_table='user_recommendations',
        pg_columns=['user_id', 'recommended_products', 'last_updated']
    )

    transfer_collection(
        mongo_db=mongo_db,
        mongo_collection='ModerationQueue',
        pg_table='moderation_queue',
        pg_columns=['review_id', 'user_id', 'product_id', 'review_text', 'rating', 'moderation_status', 'flags', 'submitted_at']
    )

    transfer_collection(
        mongo_db=mongo_db,
        mongo_collection='SearchQueries',
        pg_table='search_queries',
        pg_columns=['query_id', 'user_id', 'query_text', 'timestamp', 'filters', 'results_count']
    )

    mongo_client.close()
