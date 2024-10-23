# AirflowSpark

Docker com Airflow + Postgres + Spark cluster 

## 📦 Containers


## 🛠 Criação

### Clone do projeto

    $ $ git clone https://github.com/rodrigomodestoaraujo/AirflowSpark.git

### Construindo projeto com Docker

    $ docker-compose up -d

### Acessos

* Airflow: http://localhost:8080 - U admin - S admin
* Spark Master: http://localhost:9090

### Criação conexão Airflow

* Acesse Airflow UI > Admin > Edit connections

    * Connection Id: spark-conn 
    * Connection Type: Spark
    * Host: spark://spark-master
    * Port: 7077
    * Extra: {"queue": "root.default"}


### Dicas: 

Caso você encontre o erro "[Errno 13] Permission denied: '/opt/airflow/logs/scheduler'", execute o comando abaixo:

    $ sudo chmod -R 777 ./logs


### Obrigado pela leitura!