from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for, abort, request

# pip install flask_wtf
from forms import NewsForm
from redis_news import RedisNews

app = Flask(__name__)
query = RedisNews()

@app.route('/')
def index():
	'''新闻首页'''
	news_list = query.get_all_news()
	return render_template("index.html",news_list=news_list)

@app.route('/cat/<name>/')
def cat(name):
	'''新闻类别页面'''
	news_list = query.get_news_from_cat(name)
	return render_template('cat.html',name=name,news_list=news_list)



@app.route('/detail/<int:pk>/')
def detail(pk):
	'''新闻详情页'''
	new_obj = query.get_news_from_id(pk)
	return render_template('detail.html',new_obj = new_obj)


@app.route('/admin/')
@app.route('/admin/<int:page>/')
def admin(page):
	'''后台管理首页'''
	if page is None:
		page = 1
	page_data = query.paginage(page,5)
	return render_template('admin/index.html', page_data = page_data)


# @app.route('/admin/add/',methods=['GET','POST'])
# def add():
# 	'''新增新闻'''
# 	return render_template("amin/add.html",form=form)
#
#
# @app.route('/admin/update/<pk>/',methods=['GET','POST'])
# def update(pk):
# 	'''更新新闻'''
# 	new_obj = query.get_news_from_id(pk)
# 	if new_obj is None:
# 		abort(404)
# 	form = NewsForm(data = news_obj)
# 	if form.validate_on_submit():
# 		news_obj['title'] = form.title.data
# 		news_obj['content'] = form.content.data
# 		news_obj['news_type'] = form.news_type.data
# 		query.update_news(pk,news_obj)
# 		flash('修改成功')
# 		return redirect(url_for('admin'))
# 	return render_template("/admin/update.html",form=form)
#




# 启动flask
if __name__ == '__main__':
	app.run()

