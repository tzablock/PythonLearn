from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").master("local").getOrCreate()
df = spark.read.csv("/home/tzablock/IdeaProjects/PythonLearn/repository/conv.csv").toDF("a","b","c")
df.write.saveAsTable("some")