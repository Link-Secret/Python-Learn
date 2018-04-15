from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'hello_world!'



app.config['SECRET_KEY'] = 'a random string'
if __name__ == '__main__':
    app.run(debug=True)


# 浏览器输入http://127.0.0.1:5000