from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").master("local").getOrCreate()
input = spark.sparkContext.parallelize([1,2,3,4,5])
print(input.reduce(lambda agg,i: agg+i))
print(input.fold(0,lambda agg,i: agg+i))

result = input.aggregate((0,0),  # zero element
                         lambda acc,val: (acc[0]+val,acc[1]+1), # accumulating on executor
                         lambda acc1,acc2: (acc1[0]+acc2[0],acc1[1]+acc2[1])) # accumulating between executors
print(result[0]/result[1])
