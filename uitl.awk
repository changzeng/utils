# 查看字段取值的次数
awk -F '\x01' '{_d[$7]+=1}END{for(i in _d)print i"\t"_d[i]}' 

# 打印某文件的某一列
awk -F '\t' '{print $1}'