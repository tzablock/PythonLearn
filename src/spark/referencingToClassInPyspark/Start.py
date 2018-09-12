from pyspark.sql import SparkSession


class SomeClass(object):
    def __init__(self,str):
        self.str = str
    def isMatch(self,s):
        return self.str in s
    def badFilterRdd(self,rdd):
        return rdd.filter(self.isMatch)
    def badFilterRdd1(self,rdd):
        return rdd.filter(lambda s: self.str in s)
    def goodFilterRdd(self,rdd):
        str = self.str
        return rdd.filter(lambda s: str in s)

spark = SparkSession.builder.appName("test").master("local").getOrCreate()
input = spark.sparkContext.parallelize(["ssss","sss","sss","sss"])
someClass = SomeClass("s")
#Don't do like this because it will cause hole object serialization!
print(someClass.badFilterRdd(input).collect())
print(someClass.badFilterRdd1(input).collect())
#Do like this!
print(someClass.goodFilterRdd(input).collect())