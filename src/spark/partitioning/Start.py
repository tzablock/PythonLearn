from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").master("local").getOrCreate()
rdd = spark.sparkContext.parallelize(["sa","sa","rb","rb"])
rddInt = spark.sparkContext.parallelize([(1,1),(2,2),(1,1),(2,2),(1,1)])

def customPartitioner2(str):
    code = "nope"
    if str=="s":
        code = "ok"
    print("codeee ",code)
    return hash(code)
def customPartitioner(int):
    return hash(str(int))


rdd1 = rddInt.partitionBy(2,customPartitioner)
rdd2 = rdd.partitionBy(2,customPartitioner2)

rdd1.mapPartitionsWithIndex(lambda indx, iter: print("partition: ", indx," vals ",iter))
rdd2.mapPartitionsWithIndex(lambda indx, iter: print("partition: ", indx," vals ",iter))

rdd1.collect()