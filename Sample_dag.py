from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG — fixed constructor
dag = DAG(
    'simple_python_dag',                # dag_id as positional arg
    default_args=default_args,
    description='A simple Python DAG',
    schedule_interval='@daily',
    start_date=datetime(2025, 8, 27),
    catchup=False
)

# Define the task function
def print_hello():
    print("Hello from Airflow!")
    return 'Success'

# Define the task
hello_task = PythonOperator(
    task_id='print_hello_task',
    python_callable=print_hello,
    dag=dag                         # assign DAG explicitly here
)

# Optional: define task dependencies (only one task here)
# hello_task >> other_task
