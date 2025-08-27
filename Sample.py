from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    dag_id='simple_python_dag',
    default_args=default_args,
    description='A simple example DAG running a Python function',
    schedule_interval='@daily',  # Runs daily
    start_date=datetime(2025, 8, 27),
    catchup=False,
    tags=['example'],
) as dag:

    def print_hello():
        print("Hello from Airflow!")
        return 'Success'

    # Define the Python task
    hello_task = PythonOperator(
        task_id='print_hello_task',
        python_callable=print_hello
    )

    # Set task dependencies (if more tasks, define them here)
    hello_task
