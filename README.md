# AirflowSpark

Docker com Airflow + Spark cluster + Postgres 

## Containers

- **AirFlow** [bitnami/spark:3.5.0](https://hub.docker.com/r/bitnami/spark)
- **Spark** [apache/airflow:2.7.1-python3.11](https://hub.docker.com/r/apache/airflow)
- **Postgres** [postgres:14.0](https://hub.docker.com/_/postgres)

## Clone do projeto

    $ $ git clone https://github.com/rodrigomodestoaraujo/AirflowSpark.git

## Liberação de acesso a pastas

    $ cd AirflowSpark
    $ sudo chmod -R 777 ./logs ./data-lake/bronze ./data-lake/silver ./data-lake/gold

## Construindo projeto com Docker

    $ docker-compose build

## Subindo projeto com Docker

    $ docker-compose up

## Acessos

- Airflow: http://localhost:8080 - U admin - S admin
- Spark Master: http://localhost:9090

## Criação conexão Airflow

- Acesse Airflow UI > Admin > Edit connections

    - Connection Id: spark-conn 
    - Connection Type: Spark
    - Host: spark://spark-master
    - Port: 7077
    - Extra: {"queue": "root.default"}


# Pipelines Airflow - API OpenBreweryDB

Este repositório contém duas DAGs no Apache Airflow para consumir dados da [API OpenBreweryDB](https://api.openbrewerydb.org/breweries) e processá-los em três camadas de um data lake: Bronze, Silver e Gold.

## Estrutura

- **Camada Bronze**: Armazena os dados brutos extraídos diretamente da API em formato json.
- **Camada Silver**: Armazena os dados em uma estrutura tabular particionados em formato parquet.
- **Camada Gold**: Agregação dos dados.

## DAGs

### 1. `api_openbrewerydb_to_bronze`

Esta DAG é responsável por consumir os dados da API OpenBreweryDB e armazená-los na camada Bronze.

### Fluxo

   - Os dados consumidos pela API são armazenados no diretório `./data-lake/bronze/openbrewerydb/YYYYMMDD` no formato JSON.

### Agendamento

- A DAG é agendada para rodar diariamente às 7h (UTC)

### 2. `api_openbrewerydb_to_silver_gold`

Esta DAG processa os dados da camada Bronze e os transforma, armazenando na camada Silver particionada e na Gold com agregações.

**Transformação para camada Silver**:

   - Os dados são filtrados e particionados pelas chaves: "country", "state", "city". e salvos no diretório `./data-lake/silver/openbrewerydb`.

**Agregação e armazenamento na camada Gold**:

   - Realiza agregações, contagem de "brewery_id" pelo agrupamento "brewery_type", "country", "state", "city" e armazena os resultados no diretório `./data-lake/gold/openbrewerydb`.

### Agendamento

- A DAG é agendada para rodar diariamente às 8h (UTC)

## Obrigado pela leitura!