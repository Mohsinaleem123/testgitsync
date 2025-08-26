from __future__ import annotations
import pendulum
from airflow.models.dag import DAG

with DAG(
    dag_id="hello_world_dag",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
    tags=["example"],
) as dag:
    pass  # Add your tasks here later
