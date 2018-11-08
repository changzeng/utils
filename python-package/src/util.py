# encoding: utf-8

# author: changzeng
# github: https://github.com/changzeng

import sys

# 设置utf-8编码
def set_utf_8():
	import sys
	reload(sys)
	sys.setdefaultencoding("utf-8")

# 默认字典
def d_dict(_func=int):
	global defaultdict
	if "defaultdict" not in globals():
		from collections import defaultdict
	return defaultdict(_func)

# 元组转为字典
def tuple_to_dict(_tuple, key_func=lambda x:x, value_func=lambda x:x):
	result = {}
	for item in _tuple:
		result[key_func(item[0])] = value_func(item[1])
	return result
