from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").master("local").getOrCreate()
df = spark.read.csv("/home/tzablock/IdeaProjects/SparkTry/src/main/resources/conv.csv",sep=",").toDF("a","b","c")
df.show()
df.write.json(path = "/home/tzablock/IdeaProjects/PythonLearn/repository/out",mode = "overwrite")
#TODO strange sql style
spark.sql("select * from json.`/home/tzablock/IdeaProjects/PythonLearn/repository/some.json`").show()