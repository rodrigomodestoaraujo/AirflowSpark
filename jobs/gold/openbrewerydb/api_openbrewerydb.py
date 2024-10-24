from pyspark.sql import functions as f
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("openbrewerydb_gold").getOrCreate()
path_silver = "/opt/airflow/data-lake/silver/openbrewerydb"
path_gold = "/opt/airflow/data-lake/gold/openbrewerydb"

try:
    
    df = spark.read.parquet(path_silver)
    print("Quantidade total registos: ", df.count())
    
    df_agg = df.groupBy("brewery_type", "country", "state", "city").agg(f.count("id").alias("quantidade_brewery"))
    
    df_agg.write.format("parquet").mode("overwrite").partitionBy("country").save(path_gold)
    print("Escrita realizada na camada Gold")
    
except Exception as error:
    print(f"Uma exceção ocorreu durante a leitura dos dados da camada gold: {error}")

# Finalizando a sessão Spark
spark.stop()