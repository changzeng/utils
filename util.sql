# 时间戳转日期
from_unixtime(t1,'yyyy-MM-dd HH:mm:ss')

# hive表新增字段
alter table detail_flow_test add columns(original_union_id string);

# hive删除分区
ALTER TABLE my_partition_test_table DROP IF EXISTS PARTITION (dt='MHA');

# 为新增的字段添加注释
alter table detail_flow_test change column original_union_id original_union_id string COMMENT'原始设备唯一性标识’;

# hive创建新表
CREATE EXTERNAL TABLE `batch_20180904_L3_CouponExp_exp_control_group` (
 `uid` bigint COMMENT '学生id',
 `group` string COMMENT '用户组别'
)
PARTITIONED BY (`dt` string COMMENT '天级别分区字段')
ROW FORMAT DELIMITED
 FIELDS TERMINATED BY '\t'
STORED AS INPUTFORMAT
 'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
 'bos://zyb-offline/hive/warehouse/batch_20180904_L3_CouponExp_exp_control_group';