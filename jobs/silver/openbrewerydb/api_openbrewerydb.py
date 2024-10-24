from pyspark.sql import SparkSession
from datetime import datetime

#Variáveis 
spark = SparkSession.builder.appName("openbrewerydb_silver").getOrCreate()
path_bronze = "/opt/airflow/data-lake/bronze/openbrewerydb"
path_silver = "/opt/airflow/data-lake/silver/openbrewerydb"
formatted_date = datetime.today().strftime("%Y%m%d")

try: 
    df = spark.read.json(f"{path_bronze}/{formatted_date}/dados.json")
    print("Leitura realizada com sucesso!")
    if (df.count() > 0):
        print("Quantidade: ", df.count())
        df.write.format("parquet").mode("overwrite").partitionBy("country", "state", "city").save(path_silver)
        print("Arquivos gerados com sucesso na camada Silver")
    else:
        print(f"Sem dados para o dia {formatted_date}")
except Exception as error:
    print(f"Uma exceção ocorreu durante a leitura dos dados da camada bronze: {error}")
    
# Finalizando a sessão Spark
spark.stop()