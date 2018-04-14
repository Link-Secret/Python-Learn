import redis


class RedisNews(object):
	"""docstring for RedisNews"""
	def __init__(self):
		# db为选择的数据库
		self.r = redis.Redis(host='localhost',port=6379,db=2) 
		
	#新增新闻数据 
	def add_news(self,news_obj):
		# 获取新闻id，自增
		int_id = self.r.incr('news_id')
		# 拼接新闻数据hash key(news:2)
		news_id = 'news:%d' % int_id
		# 存储新闻数据(hash)
		rest = self.r.hmset(news_id,news_obj)
		# 存储新闻的id(list)
		self.r.lpush('news',int_id)
		# 存储新闻的类别-新闻id(set)
		news_type = 'news_type:%s' % news_obj['news_type']
		self.r.sadd(news_type,int_id)
		return rest
		

	def init_news(self,data_list):
		# 批量新增新闻
		for news_obj in data_list:
			rest = self.add_news(news_obj)
			print(rest)