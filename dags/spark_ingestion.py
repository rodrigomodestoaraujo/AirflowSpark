import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

dag = DAG(
    dag_id = "Ingestion",
    default_args = {
        "owner": "Rodrigo Araujo",
        "start_date": airflow.utils.dates.days_ago(1)
    },
    schedule_interval = "@daily"
)

bronze = PythonOperator(
    task_id="Bronze",
    python_callable = lambda: print("Jobs started"),
    dag=dag
)

#silver = SparkSubmitOperator(
#    task_id="Silver",
#    conn_id="spark-conn",
#    application="jobs/python/wordcountjob.py",
#    dag=dag
#)

gold = PythonOperator(
    task_id="Gold",
    python_callable = lambda: print("Jobs completed successfully"),
    dag=dag
)

bronze >> gold