from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext

spark = SparkSession.builder.appName("test").master("local").getOrCreate()
ssc = StreamingContext(spark.sparkContext,1)

sd = ssc.textFileStream("/home/tzablock/IdeaProjects/PythonLearn/repository/streming").map(lambda x: x+"działa")
sd.pprint()

ssc.start()
ssc.awaitTermination()