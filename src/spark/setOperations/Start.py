from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local").appName("test").getOrCreate()
fNums = spark.sparkContext.parallelize([1,2,2,2,3,4])
sNums = spark.sparkContext.parallelize([3,4,5,6])
# distinct numbers
print(fNums.distinct().collect())
#all numbers
print(fNums.union(sNums).collect())
# common numbers
print(fNums.intersection(sNums).collect())
# numbers only in first set
print(fNums.subtract(sNums).collect())
#make pairs of all elements in both sets
print(fNums.cartesian(sNums).collect())