# pyspark初始化
from pyspark import SparkContext                                                                                                                                                                                                        
sc = SparkContext()

# 创建RDD
rdd = sc.parallelize(_list)

# pyspark统计某个字段的取值个数
# spark: 2.5min, awk: 5min
sc.textFile("file_name").map(lambda x:x.split("\x01")).map(lambda x:(x[0], 1)).reduceByKey(lambda a,b:a+b).collect()

# RDD集合操作
a.union(b)			# 并集
a.intersection(b)	# 交集
a.subtract(b)		# 差集

# RDD去重
a.distinct()

# spark关键概念
Application: 用户提交的任务
Driver: 任务调度
Job: 每个action算子是一个job
Task: RDD的partitions上的执行单元
Stage: 按照宽窄依赖划分
宽窄依赖: "https://github.com/rohgar/scala-spark-4/wiki/Wide-vs-Narrow-Dependencies"

# pandas DataFrame to spark DataFrame
from pyspark.sql import SparkSession
spark = SparkSession\
            .builder \
            .appName("dataFrame") \
            .getOrCreate()
spark_df = spark.createDataFrame(df)

# pandas DataFrame to spark rdd
spark.createDataFrame(df).rdd
