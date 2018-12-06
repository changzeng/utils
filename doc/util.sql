# hive表新增字段
alter table detail_flow_test add columns(original_union_id string);

# hive删除分区
ALTER TABLE my_partition_test_table DROP IF EXISTS PARTITION (dt='MHA');

# 为新增的字段添加注释
alter table detail_flow_test change column original_union_id original_union_id string COMMENT'原始设备唯一性标识’;

# hive创建新表
CREATE EXTERNAL TABLE `live_laxin_cuid_list` (
 `cuid` string COMMENT 'cuid'
)
PARTITIONED BY (`dt` string COMMENT '天级别分区字段')
ROW FORMAT DELIMITED
 FIELDS TERMINATED BY '\t'
STORED AS INPUTFORMAT
 'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
 'bos://zyb-offline/hive/warehouse/live_laxin_cuid_list';

# 按a排序去b字段
SELECT *, Row_Number() OVER (partition by deptid ORDER BY salary desc) rank FROM employee;

empid       deptid      salary                                  rank
----------- ----------- --------------------------------------- --------------------
1           10          5500.00                                 1
2           10          4500.00                                 2
4           20          4800.00                                 1
3           20          1900.00                                 2
7           40          44500.00                                1
6           40          14500.00                                2
5           40          6500.00                                 3
9           50          7500.00                                 1
8           50          6500.00                                 2

# 修改字段名
ALTER table live_laxin_act_rec_user_feature CHANGE act_id uid bigint;

# hive插入map字段
str_to_map("a:b,c:d")

# 日期到时间戳
unix_timestamp("{@date}", "yyyyMMdd")

# 时间戳转日期
from_unixtime(t1,'yyyy-MM-dd HH:mm:ss')
