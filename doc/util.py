# encoding: utf-8
import time
import requests
import pandas as pd

# encoding: utf-8

# 设置编码
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# jupyter设置编码
import sys
stdi, stdo, stde = sys.stdin, sys.stdout, sys.stderr
reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdin, sys.stdout, sys.stderr = stdi, stdo, stde

if __name__ == "__main__":
	pass

from collections import defaultdict
a = defaultdict(int)
a = defaultdict(lambda :1)

# 参数
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--mode', type=str, default="buy_user")
args = parser.parse_args()

# 时间戳转日期
def timestamp_to_timestr(timestamp):
	otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", time.localtime(timestamp))
	return otherStyleTime

# 日期转时间戳
def timestr_to_timestamp(timestr):
	return int(time.mktime(time.strptime(timestr, "%Y%m%d")))

# 发送post请求
def post_url(url, _dict={}):
	return requests.post(url,data=_dict).text

# 发送get请求
def get_url(url, _dict={}):
	if len(_dict) == 0:
		url = url
	else:
		url = "{0}?{1}".format(url, "&".join(["{0}={1}".format(key, value) for key, value in _dict.items()]))
	return requests.get(url).text

# 日期递增
def date_range_num(start_date, day_num):
	def timestr_to_timestamp(timestr):
		# time.strptime(timestr, "%Y-%m-%d %H:%M:%S")
		return int(time.mktime(time.strptime(timestr, "%Y%m%d")))
	def timestamp_to_timestr(timestamp):
		timeArray = time.localtime(timestamp)
		otherStyleTime = time.strftime("%Y%m%d", timeArray)
		return otherStyleTime
	start_timestamp = timestr_to_timestamp(start_date)
	result = []
	for i in range(day_num):
		if i != 0:
			start_timestamp += 24*3600
		result.append(timestamp_to_timestr(start_timestamp))
	return result

# 日期范围
def date_range(start_date, end_date):
	start_datetime = datetime.datetime.strptime(start_date, "%Y%m%d")
	day_diff = (datetime.datetime.strptime(end_date, "%Y%m%d") - start_datetime).days
	for i in range(day_diff):
		yield (start_datetime + datetime.timedelta(days=i)).strftime("%Y%m%d")

# list数据保存到excel
def list_to_excel(_list, file_name):
	df = pd.DataFrame(_list)
	writer = pd.ExcelWriter(file_name)
	df.to_excel(writer, sheet_name="untitle_1")
	writer.save()

# flask快速建站
from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/')
def index():
	return "hello"
app.run(host="127.0.0.1", port=5555, debug=True)

# python文件操作
import os
os.listdir()
os.path.exists()
os.remove()

# timestamp转datetime
datetime.datetime.fromtimestamp(t)

# 获取当前的日期
datetime.datetime.now().strftime("%Y%m%d %H%M")

# 日期加减N操作
datetime.datetime.strptime("20180602", "%Y%m%d") + datetime.timedelta(days=4)

# 获得今天是星期几
datetime.datetime.now().weekday()

# python判断当前脚本是否正在运行
import os
import sys

pid = str(os.getpid())
if not os.path.exists("log"):
	os.mkdir("log")
pid_file = "log/pid.log"

if os.path.isfile(pidfile):
    print "%s already exists, exiting" % pidfile
    sys.exit()
file(pidfile, 'w').write(pid)
try:
    # Do some actual work here
finally:
    os.unlink(pidfile)

# python集合操作
# 差集
a - b
# 并集
a.union(b)
# 交集
a.intersection(b)

# 判断对象是否包含某属性
hasattr(t, "name")

# python代码换行
\

# 存为csv
df.to_csv(csv_file_name)

# 打开excel文件
data_sheet = pd.read_excel("compare_detail.xlsx", sheetname="Sheet1")

# 保存excel
writer = pd.ExcelWriter('E:\\PythonTestCode\\public opinion_result.xlsx')
data1.to_excel(writer, sheet_name = 'data1', index = False)
writer.save()
writer.close()

# 显示所有列名
data.keys()

# 按行遍历DataFrame
for index, row in df.iterrows():
	print row['c1'], row['c2']

# pandas打开excel
df=pd.read_excel(file_name)

# pandas修改excel
for index, row in data.iterrows():
	data.loc[i, col_name] = new_value

# pandas dataframe 同时获取多列
df[[col1, col2, col2]]

# format输出{}
print "{{test}}{0}".foramt("hello")

# python globals and locals and global keyword
locals: 局部变量字典(函数参数等等)
globals: 全部变量字典
global: 文件的全局变量

# pandas列转化
inv_label_mapping = {v:k for k,v in label_mapping.items()}
data["label"] = data["label"].map(inv_label_mapping)
print(data)

# 判断python版本
import sys
sys.version_info < (3, 0)

# 重定向标准输出到标准输入
with open(test_file, "w") as fd:
	fd.write(out_str)
with open(test_file) as fd:
	sys.stdin = fd

# 从任一位置引入python脚本
import sys
sys.path.append(package_path)

# WSGI模块详解
# TODO: 添加WSGI详解

# xlrd使用方法
import xlrd
workbook = xlrd.open_workbook(file_path)
workbook.sheet_names()
sheet = workbook.sheet_by_index(sheet_index)
sheet = workbook.sheet_by_name(sheet_name)
sheet.row_values(3)
sheet.col_values(3)
sheet.cell(1, 2)
sheet.cell_value(1, 2)
# 表格的行数
sheet.nrows
# 表格的列数
sheet.ncols

# 求top N
from heapq import nlargest, nsmallest
nlargest(n, _list, key=lambda x:x)

# 开启多线程
import threading
t = threading.Thread(target=func, args=(a, b, c))
t.start()
t.join()

# thrift编译
thrift --gen py hello.thrift

# thrift服务模式
# 单进程单线程...
TServer.TSimpleServer
# 每个请求独立的线程
TServer.TThreadedServer
# 线程池模型
TServer.TThreadPoolServer
# 每个请求独立的进程
TServer.TForkingServer
# 进程池方案
TServer.TProcessPoolServer

# 多线程加锁
import threading
mutex = threading.Lock()
mutex.acquire()
mutex.release()

# 获得日志对象
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler(config["log_path"], "a")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# python3.5+合并字典
a = {"a":1 ,"b": 2}
b = {"c":3 ,"d": 4}
c = {**a, **b}

# 多条件或
any(a, b, c)

# python开启ftp服务
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
# 实例化虚拟用户，这是FTP验证首要条件
authorizer = DummyAuthorizer()
# 添加用户权限和路径，括号内的参数是(用户名， 密码， 用户目录， 权限)
authorizer.add_user('user', '12345', '/home/homework/user', perm='elradfmw')
# 初始化ftp句柄
handler = FTPHandler
handler.authorizer = authorizer
# 监听ip 和 端口,因为linux里非root用户无法使用21端口，所以我使用了2121端口
server = FTPServer(('192.168.240.13', 2121), handler)
# 开始服务
server.serve_forever()

# pandas排序
df.sort_values("name")

# 获得文件所在路径
os.path.split(os.path.realpath(__file__))[0]
