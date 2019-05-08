# encoding: utf-8

# author: changzeng
# github: https://github.com/changzeng

import sys
from rediscluster import StrictRedisCluster

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


def get_client(addr_list):
	"""
	根据地址获得redis客户端
	:param addr_list:
	:return:
	"""
	return StrictRedisCluster(startup_nodes=redis_nodes, decode_responses=True)


def get_all_keys(client, prefix):
	"""
	获得所有以prefix开头的key
	:param client:
	:param prefix: key前缀
	:return:
	"""
	pattern = "{0}*".format(prefix)
	key_list = client.keys(pattern)
	return key_list


def delete_redis_key(client, key):
    """
    删除redis中的key
    :param client:
    :param key:
    :return:
    """
    return client.delete(key)


def delete_redis_key_list(client, key_list):
    """
    删除redis中的key
    :param client:
    :param key_list:
    :return:
    """
    res = 0
    for key in key_list:
    	res += client.delete(key)
    return res

