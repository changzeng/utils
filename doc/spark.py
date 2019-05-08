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

# rdd保存与加载
rdd.saveAsPickleFile(file_name, partition_num)
sc.pickleFile(file_name)

# spark关键概念
Application: 用户提交的任务
Driver: 任务调度
Job: 每个action算子是一个job
Task: RDD的partitions上的执行单元
Stage: 按照宽窄依赖划分
宽窄依赖: "https://github.com/rohgar/scala-spark-4/wiki/Wide-vs-Narrow-Dependencies"

# pandas DataFrame to spark DataFrame
from pyspark.sql import SparkSession
sqlContext = SparkSession\
				.builder \
	            .appName("dataFrame") \
	            .getOrCreate()
spark_df = sqlContext.createDataFrame(df)

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

# rdd获取指定数量元素转化为列表
rdd.take(_num)					#返回list
rdd.takeSample(_flag, _num)		# _flag为True代表放回采样，False不放回采样，返回list

# 随机采样，结果仍为rdd
rdd.sample(False, _fraction)

# 获取rdd元素个数
rdd.count()

# 获取rdd的top N结果仍为rdd
rdd.cache()
_count = rdd.count()
rdd.zipWithIndex().filter(lambda x:x[1]<=_count*_fraction).map(lambda x:[0])

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

# rdd转map
rdd.collectAsMap()

# rdd排序
rdd.sortByKey(ascending=False)
rdd.sortBy(_func, ascending=False)

# groupByKey注意事项
rdd.groupByKey()	# 之后需要将rdd的第二项转为list

# rdd随机分裂
rdd.randomSplit([0.2, 0.8])

# 笛卡尔积
c = a.cartesian(b)

# DataFrame读取csv
df = sqlContext.read.csv(file_name, header=True)

# DataFrame添加新列
from pyspark.sql.functions import exp
from pyspark.sql.functions import lit
df = sqlContext.createDataFrame([(1, "a", 23.0), (3, "B", -23.0)], ("x1", "x2", "x3"))
df_with_x4 = df.withColumn("x4", lit(0))
df_with_x5 = df_with_x4.withColumn("x5", exp("x3"))

# DataFrame保存为csv
df.write.csv(file_name)

# pyspark自定义udf
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
maturity_udf = udf(lambda age: "adult" if age >=18 else "child", StringType())
df = sqlContext.createDataFrame([{'name': 'Alice', 'age': 1}])
df.withColumn("maturity", maturity_udf(df.age))
