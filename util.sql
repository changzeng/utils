# 时间戳转日期
from_unixtime(t1,'yyyy-MM-dd HH:mm:ss')

# hive表新增字段
alter table detail_flow_test add columns(original_union_id string);

# 为新增的字段添加注释
alter table detail_flow_test change column original_union_id original_union_id string COMMENT'原始设备唯一性标识’;