from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PythonWordCount").getOrCreate()

# Imprimindo uma mensagem
print("Hello from Spark!")

# Finalizando a sessão Spark
spark.stop()