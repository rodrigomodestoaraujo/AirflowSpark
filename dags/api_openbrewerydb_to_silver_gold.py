import airflow
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

dag = DAG(
    dag_id = "api_openbrewerydb_to_silver_gold",
    default_args = {
        "owner": "Rodrigo Araujo",
        'start_date': datetime(2024, 10, 22),
        "retries": 1
    },
    schedule_interval='0 8 * * *',
    max_active_runs=1,
)

silver = SparkSubmitOperator(
    task_id="Silver",
    conn_id="spark-conn",
    application="jobs/silver/openbrewerydb/api_openbrewerydb.py",
    dag=dag
)

gold = SparkSubmitOperator(
    task_id="Gold",
    conn_id="spark-conn",
    application="jobs/gold/openbrewerydb/api_openbrewerydb.py",
    dag=dag
)

silver >> gold