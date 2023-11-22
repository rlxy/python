from flask import Flask,escape,url_for

app = Flask(__name__)


#url_for示例
#为什么要用url_for：
#1.将来如果修改了URL，但没有修改对应的函数名，那就不用到处替换URL了
#2.url_for会自动处理那些特殊字符，不需要手动处理  例如/
@app.route('/')
def index():
    my_list_path = url_for('my_list',page=1,count=111)
    print(my_list_path)
    return my_list_path
@app.route('/list/<int:page>/')
def my_list(page):
    return '第{}页'.format(page)



@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile '.format(escape(username))
with app.test_request_context():
    # url_for用于构建指定函数的URL，第一个参数是函数名的字符串格式，后面的参数会以关键字的形式传递给URL
    # 它可以接受任意个关键字参数，每个关键字参数对应URL中的变量。未知变量将添加到URL中作为查查询参数
    print(url_for('index')) #index是上面一个函数名，打印出来就是对应的路由地址
    print(url_for('login'))
    print(url_for('login',next = '/'))
    print(url_for('profile',username='johndoe'))



#为什么不把URL写死在模板中，而要使用反转函数url_for()动态构建？
'''
1.反转通常比硬编码 URL 的描述性更好。
2.你可以只在一个地方改变 URL ，而不用到处乱找。
3.URL 创建会为你处理特殊字符的转义和 Unicode 数据，比较直观。
4.生产的路径总是绝对路径，可以避免相对路径产生副作用。
5.如果你的应用是放在 URL 根路径之外的地方（如在 /myapplication 中，不在 / 中）， url_for() 会为你妥善处理。
'''
app.run()