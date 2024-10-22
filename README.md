# AirflowSpark

Docker com Airflow + Postgres + Spark cluster 

## 📦 Containers


## 🛠 Criação

### Clone do projeto

### Construindo projeto com Docker

    $ docker-compose up -d

### Check accesses

* Airflow: http://localhost:8080
* Spark Master: http://localhost:9090

### Criação conexão Airflow

* Acesse Airflow UI > Admin > Edit connections

    * Connection Id: spark-conn 
    * Connection Type: Spark
    * Host: spark://spark-master
    * Port: 7077
    * Extra: {"queue": "root.default"}

Obrigado pela leitura!