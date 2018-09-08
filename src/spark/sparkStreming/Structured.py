from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").master("local").getOrCreate()
input = spark.readStream.csv("/home/tzablock/IdeaProjects/PythonLearn/repository/structStreming",schema="num INT, str STRING")  #TODO it will take from file first rows as in schema if other types will fill with nulls

input.writeStream.start(format = "console").awaitTermination()
