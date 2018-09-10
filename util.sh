# 查看进程的启动命令
function start_cmd(){
	cat /proc/$1/cmdline | tr '\000' ' '
	echo ""
}

# 查看进程的启动目录
function cwd(){
	ls -al /proc/$1/cwd
}

# 递归搜索制定类型的文件
find . -name "*.py" | xargs grep --color=auto "ua_info_list"

# hive加载hadoop文件
hive -e "load data inpath '{0}' overwrite into table {1} partition (dt={2});"

# hive加载hadoop文件
hive -e "load data local inpath '{0}' overwrite into table {1} partition (dt={2});"