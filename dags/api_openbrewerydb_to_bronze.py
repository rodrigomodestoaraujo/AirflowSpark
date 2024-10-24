from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests
import json
import os

# Função que será executada pela DAG
def ApiOpenbrewerydb(url, path_bronze):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            dados = resp.json()
            dados_str = json.dumps(dados)
            formatted_date = datetime.today().strftime("%Y%m%d")
            path_saida = f"{path_bronze}/{formatted_date}"
            os.makedirs(path_saida, exist_ok=True)
            with open(f"{path_saida}/dados.json", "w") as arquivo:
                arquivo.write(dados_str)
                print("Arquivo gerado com sucesso!")
                print(f"Path: {path_saida}/dados.json")
        else:
            print(f"Erro na chamada da API")
            print(f"Status Code: {resp}")
    except Exception as error:
        print(f"Uma exceção ocorreu durante a chamada da API: {error}")

# Definição da DAG
default_args = {
    'owner': 'Rodrigo Araujo',
    'depends_on_past': False,
    'start_date': datetime(2024, 10, 22),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    'api_openbrewerydb_to_bronze',
    default_args=default_args,
    description='DAG para extrair dados da API OpenBrewery e salvar em bronze',
    schedule_interval='0 7 * * *',
    max_active_runs=1,
    catchup=False,
) as dag:

    
    task_api_to_bronze = PythonOperator(
        task_id='api_openbrewerydb_to_bronze',
        python_callable=ApiOpenbrewerydb,
        op_kwargs={'url': 'https://api.openbrewerydb.org/breweries', 
                   'path_bronze': '/opt/airflow/data-lake/bronze/openbrewerydb'},
    )

    task_api_to_bronze

