FROM apache/airflow:2.7.1-python3.11

USER root
RUN apt-get update && \
    apt-get install -y gcc python3-dev openjdk-11-jdk && \
    apt-get install -y procps && \
    apt-get clean

# Set JAVA_HOME environment variable
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64

USER airflow

RUN pip install apache-airflow==2.7.1
RUN pip install apache-airflow-providers-apache-spark==1.0.2
RUN pip install pyspark

# Se você estiver rodando em um Ubuntu e encontrar o erro | PermissionError: [Errno 13] Permission denied: '/opt/airflow/logs/scheduler'
# Execute $ sudo chmod -R 777 ./logs