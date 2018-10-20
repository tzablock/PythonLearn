import pyspark # only run after findspark.init()
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("sss").master("local").getOrCreate()
df = spark.sparkContext.parallelize([1,2,3,4]).toDF("int")
df.show()