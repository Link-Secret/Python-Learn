#@Time  :   2018/4/9 19:13
#@Author:   zjl
#@File  :   4-9-5filter.py

import MySQLdb

#获取连接
try:
	conn = MySQLdb.connect(
		host = '127.0.0.1',
		user = 'root',
		password = 'admin',
		db = 'news',
		port = 3306,
		charset = 'utf8'
	)

# 获取数据
	cursor = conn.cursor()
	cursor.execute("select * from news")
	rest = cursor.fetchone()
	print(rest)

	# 关闭连接
	conn.close()
except MySQLdb.Error as e:
	print('Error: %s' % e)