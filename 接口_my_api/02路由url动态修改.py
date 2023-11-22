import flask

#web网页都应该有个有意义的URL(路由)

#使用route()装饰器来吧函数绑定到URL

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')    #可以动态变换URL的某些部分，还可以为一个函数指定多个规则
def hello_world():
    return 'Hello,World!'


app.run()