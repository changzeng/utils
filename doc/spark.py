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

# 设置缓存级别
from pyspark.storagelevel import StorageLevel
StorageLevel.DISK_ONLY = StorageLevel(True, False, False, False)
StorageLevel.DISK_ONLY_2 = StorageLevel(True, False, False, False, 2)
StorageLevel.MEMORY_ONLY = StorageLevel(False, True, False, False)
StorageLevel.MEMORY_ONLY_2 = StorageLevel(False, True, False, False, 2)
StorageLevel.MEMORY_AND_DISK = StorageLevel(True, True, False, False)
StorageLevel.MEMORY_AND_DISK_2 = StorageLevel(True, True, False, False, 2)
StorageLevel.OFF_HEAP = StorageLevel(True, True, True, False, 1)

# spark使用随机森林
from pyspark.mllib.tree import RandomForest, RandomForestModel
model = RandomForest.trainClassifier(trainingData, numClasses=2, categoricalFeaturesInfo={}, numTrees=3, featureSubsetStrategy="auto", impurity='gini', maxDepth=4, maxBins=32)

# spark rdd存为本地文本文件
rdd.saveAsTextFile(file_name)

# rdd采样
rdd.take(_num)					#返回list
rdd.takeSample(_flag, _num)		# _flag为True代表放回采样，False不放回采样，返回list

# 加载样本
from pyspark.mllib.util import MLUtils 
samples = MLUtils.loadLibSVMFile(sc, sample_file_name) 

# 样本分割
(trainingData, testData) = samples.randomSplit([0.7, 0.3]) 

# 频繁项挖掘
from pyspark.mllib.fpm import FPGrowth

data = sc.textFile("data/mllib/sample_fpgrowth.txt")
transactions = data.map(lambda line: line.strip().split(' '))
model = FPGrowth.train(transactions, minSupport=0.2, numPartitions=10)
result = model.freqItemsets().collect()
for fi in result:
    print(fi)
