from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").master("local").getOrCreate()
spark.read.csv("/home/tzablock/IdeaProjects/PythonLearn/repository/conv.csv").toDF("a","b","c").createOrReplaceTempView("sometable")
spark.sql("select * from sometable").show()
spark.sql("select count(*) from sometable").show()