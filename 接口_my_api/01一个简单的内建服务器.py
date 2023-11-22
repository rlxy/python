import flask

app = flask.Flask(__name__)     #__name__会根据这个 模块是按应用方式使用还是作为一个模块导入而发生变化（可能是 ‘__main__’ ， 也可能是实际导入的名称）

@app.route('/')     #route()装饰器告诉Flask触发函数的URL
def hello_world():  #函数名称被用于生成相关联的URL
    return 'Hello,World!'   #函数最后返回需要在浏览器显示的信息

#如何启动这个简单的服务器呢？
'''
在windows下：
set FLASK_APP=文件名例如:01一个简单的内建服务器.py     运行前需要在终端导出FLASK_APP环境变量
set FLASK_ENV=development 运行前也可以把FLASK_APP环境变量设置成development
                        这是打开调试模式 这样可以实现以下功能：
                            1.激活调试器。
                            2.激活自动重载。
                            3.打开 Flask 应用的调试模式。
                        还可以通过导出 FLASK_DEBUG=1 来单独控制调试模式的开关。  1或0

flask run        
或者在设置了python环境下可以：python -m flask run

可以直接在代码末尾加入 app.run()   参数就是一些需要设置的例如端口 开发者的开关
'''
#启动后会发现，在局域网内只有主机能访问，其他电脑却不行，因为在调试模式下，设置就是这样，如果需要局域网内其他电脑访问可以这样:
#在运行命令中加上 --host=0.0.0.0     flask run --host=0.0.0.0           这行代码告诉你的操作系统监听所有公开的 IP

# app.run() 常见的参数：port，debug  post默认5000