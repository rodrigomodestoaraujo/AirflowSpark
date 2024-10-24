# AirflowSpark

Docker com Airflow + Postgres + Spark cluster 

## 📦 Containers


## 🛠 Criação

### Clone do projeto

    $ $ git clone https://github.com/rodrigomodestoaraujo/AirflowSpark.git

### Liberação de acesso a pastas

    $ sudo chmod -R 777 ./logs
    $ sudo chmod -R 777 ./data-lake/bronze
    $ sudo chmod -R 777 ./data-lake/silver
    $ sudo chmod -R 777 ./data-lake/gold

### Construindo projeto com Docker

    $ docker-compose up  --build

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


### Obrigado pela leitura!