# encoding: utf-8
import time
import requests
import pandas as pd

# encoding: utf-8

# 设置编码
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

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
	# time.strptime(timestr, "%Y-%m-%d %H:%M:%S")
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

# 打开excel文件
data_sheet = pd.read_excel("compare_detail.xlsx", sheetname="Sheet1")

# 显示所有列名
data.keys()

# 按行便利DataFrame
for index, row in df.iterrows():
	print row['c1'], row['c2']

# pandas修改excel
for index, row in data.iterrows():
	data.loc[i, col_name] = new_value

# format输出{}
print "{{test}}{0}".foramt("hello")

# python globals and locals and global keyword
locals: 局部变量字典(函数参数等等)
globals: 全部变量字典
global: 文件的全局变量

