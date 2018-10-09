from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local").appName("test").getOrCreate()
rdd = spark.sparkContext.parallelize([(1,2),(1,3),(2,5)])
rdd1 = spark.sparkContext.parallelize([(1,10),(3,5)])
print(rdd.join(rdd1).collect())
print(rdd.rightOuterJoin(rdd1).collect())
for (x,y) in rdd.cogroup(rdd1).collect():
    print("key" + str(x))
    for z in y:
        print(z)
        for g in z:
            print("val" + str(g))

rdd3 = spark.sparkContext.parallelize([(1,1),(1,2),(1,3),(1,2),(1,3)])
print(rdd3.combineByKey(lambda x: (x,1),lambda x, value: (x[0]+value,x[1]+1),lambda x,y: (x[0]+y[0],x[1]+y[1])).collect())