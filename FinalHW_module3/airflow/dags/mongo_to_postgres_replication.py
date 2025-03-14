from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from transfer_data import transfer_all_data

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 3, 14),
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'catchup': False,
    'depends_on_past': False,
}

dag = DAG(
    'mongo_to_postgres_replication',
    default_args=default_args,
    schedule_interval='@daily',
    description='Full replication of MongoDB data to PostgreSQL',
    tags=['etl', 'replication']
)

replicate_task = PythonOperator(
    task_id='replicate_all_collections',
    python_callable=transfer_all_data,
    dag=dag
)