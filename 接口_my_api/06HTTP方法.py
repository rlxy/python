from flask import Flask,request

app = Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

#web应用使用不同的HTTP方法处理URL。当你使用Flask时，应当熟悉HTTP方法。缺省情况下，一个路由只回应GET请求。可以使用route()装饰器的methods参数来处理不同的HTTP方法
