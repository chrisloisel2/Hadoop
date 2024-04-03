from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Test").getOrCreate()
sc = spark.sparkContext
# RDD
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])

df = spark.createDataFrame([(1, "Alice"), (2, "Bob")], ["id", "name"])

# Creer un rdd
numberRDD = sc.parallelize(range(1, 101))

print(numberRDD.collect())


filtrerRDD = numberRDD.filter(lambda x: x >= 50)

print(filtrerRDD.collect())


# MAP
# FILTER
# REDUCE
# SORT
# JOIN
# GROUPBY
# UNION
# AGGREGATE

# Promesse de traitement
res = df.rdd.map(lambda x : (x[0] + 1, x[1]))
# map
print(res.collect())

# fermer la session spark
spark.stop()
