import redis


class Paginate(object):
    """分页"""

    def __init__(self, data_list, now_page, per_page):
        self.data_list = data_list
        self.now_page = now_page
        self.per_page = per_page

    @property
    def page(self):
        return self.now_page

    @property
    def items(self):
        '''当页数据，'''
        return self.data_list

    @property
    def has_prev(self):
        '''是否有上一页'''
        return self.now_page > 1

    @property
    def has_next(self):
        '''是否有下一页,模糊判断是否有十个'''
        return self.per_page == len(self.data_list)

    @property
    def pre_num(self):
        '''上一页页码'''
        return self.now_page - 1

    @property
    def nex_num(self):
        '''下一页页码'''
        return self.now_page + 1

    def iter_pages(self):
        '''页码'''
        return range(1, self.now_page)


class RedisNews(object):
    """docstring for RedisNews"""

    def __init__(self):
        # db为选择的数据库
        self.r = redis.Redis(
            host='localhost',
            port=6379,
            db=4,
            decode_responses=True)

    # 封装3个函数
    def _news_id(self, int_id):
        '''拼接新闻id'''
        return 'news:%d' % int(int_id)

    def _news_list_name(self):
        '''新闻id 列表名称'''
        return 'news'

    def _news_type(self, news_type):
        '''新闻的类别key'''
        return 'news_type:%s' % news_type

    # 新增新闻数据
    def add_news(self, news_obj):
        # 获取新闻id，自增
        int_id = self.r.incr('news_id')
        # 拼接新闻数据hash key(news:2)
        news_id = self._news_id()
        # 存储新闻数据(hash)
        rest = self.r.hmset(news_id, news_obj)
        # 存储新闻的id(list)
        self.r.lpush(self._news_list_name(), int_id)
        # 存储新闻的类别-新闻id(set)
        news_type = self._news_type(news_obj)['news_type']
        self.r.sadd(news_type, int_id)
        return rest

    def add_news_width_trans(self, news_obj):
        '''新增新闻+事务支持'''
        '''直接通过管道pipe获取，而不是通过连接获取'''
        try:
            # 事务
            pipe = self.r.pipeline()

            # 获取新闻id，自增，这里id只能从连接获取，而不能从缓存获取
            int_id = self.r.incr('news_id')
            # 拼接新闻数据hash key(news:2)
            news_id = 'news:%d' % int_id
            # 存储新闻数据(hash)
            rest = pipe.hmset(news_id, news_obj)
            # 存储新闻的id(list)
            pipe.lpush('news', int_id)
            # 存储新闻的类别-新闻id(set)
            news_type = 'news_type:%s' % news_obj['news_type']
            pipe.sadd(news_type, int_id)
            # 事务执行返回结果给rest
            rest = pipe.execute()
        except:
            pass
        return rest

    def get_all_news(self):
        '''获取所有新闻数据'''
        # 取所有的新闻的id，从列表中去news
        id_list = self.r.lrange(self._news_list_name(), 0, -1)
        news_list = []
        #循环id列表，获取新闻数据hash
        for int_id in id_list:
            # 新闻的key
            news_id = self._news_id(int_id)
            data = self.r.hgetall(news_id)
            data['id'] = int_id
            news_list.append(data)
        return news_list

    def get_news_from_id(self, int_id):
        '''根据新闻的id来获取新闻数据'''
        # 获取新闻key
        news_id = self._news_id(int_id)
        # 查询新闻数据hash
        data = self.r.hgetall(news_id)
        data['id'] = int_id
        return data

    def get_news_from_cat(self, news_type):
        '''根据新闻的类别来获取新闻数据'''
        news_list = []
        # 获取新闻类别key
        news_type = self._news_type(news_type)
        # 查询该类别所有新闻id
        id_list = self.r.smembers(news_type)
        # 通过循环来查询所有新闻数据
        for int_id in id_list:
            news_id = self._news_id(int_id)
            data = self.r.hgetall(news_id)
            data['id'] = int_id
            news_list.append(data)
        return news_list


    def paginage(self, page=1,per_page=10):
        '''分页数据'''
        if page is None:
            page = 1
        news_list = []
        # 计算开始和结束标记
        start = (page - 1) * per_page
        end = page * per_page - 1
        # 获取当页的id
        id_list = self.r.lrange(self._news_list_name(), start, end)
        # 通过循环来查询数据
        for int_id in id_list:
            news_id = self._news_id(int_id)
            data = self.r.hgetall(news_id)
            data['id'] = int_id
            news_list.append(data)
        return Paginate(news_list, page, per_page)


    # def update_news(self, int_id, news_obj):
    #     '''修改新闻数据'''
    #     news_id = self._news_id(int_id)
    #     return self.r.hmset(news_id, news_obj)


    def init_news(self, data_list):
        # 批量新增新闻
        for news_obj in data_list:
            # rest = self.get_all_news(news_obj)
            print(rest)
