from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").master("local").getOrCreate()
rdd = spark.sparkContext.parallelize([(1,"a"),(2,"b")])
df = rdd.toDF("inte INT, str STRING")
df.show()
for tup in df.rdd.collect():
    print(tup)
