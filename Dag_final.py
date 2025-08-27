# hello_world_dag.py
# A minimal Airflow 2.x DAG that prints "Hello, World!" and runs a simple Bash echo.

from datetime import timedelta
import pendulum
from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

# DAG basics
DAG_ID = "hello_world_v1"

with DAG(
    dag_id=DAG_ID,
    description="Minimal Hello World DAG (TaskFlow + BashOperator)",
    schedule_interval="@daily",          # run once a day
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    catchup=False,                       # do not backfill
    default_args={
        "owner": "airflow",
        "retries": 0,
        "retry_delay": timedelta(minutes=5),
    },
    tags=["example", "hello-world"],
) as dag:

    @task(task_id="say_hello")
    def say_hello():
        """
        Simple Python task that logs a hello message.
        """
        print("Hello, World! 👋 This is a TaskFlow @task in Airflow.")

    bash_hello = BashOperator(
        task_id="bash_hello",
        bash_command='echo "Hello from BashOperator!"'
    )

    # Task order
    say_hello() >> bash_hello
