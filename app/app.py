from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("myapp").getOrCreate()
sc = spark.sparkContext

# Consumer code
df = spark.readStream.format("kafka")\
    .option("kafka.bootstrap.servers", "kafka:9093")\
    .option("subscribe", "topic1")\
    .option("maxRequestSize", "1073741824")\
    .load()

# Afficher la data
query = df.writeStream.outputMode("append").format("console").start()

query.awaitTermination()
