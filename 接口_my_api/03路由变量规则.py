import flask

app = flask.Flask(__name__)

#变量规则  通过把URL的一部分标记为<variable_name> 就可以在URL中添加变量。
# 标记的部分会作为关键字参数传递给函数。通过使用<converter:variable_name>可以选择性的加上一个转换器，为变量指定规则
@app.route('/user/<username>')
def show_user(username):
    return '这里设置的URL变量是username,username=={0}'.format(username)

@app.route('/post/<int:post_id>')   #int就是转换器
def show_post_id(post_id):
    return 'url变量为post_id，，为%d' % post_id
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'url变量是subpath,为%s' % subpath
'''
转换器类型：
            string:(缺省值)接受任何不包含斜杠的文本
            int:接受正整数
            float:接受正浮点数
            path:类似string，但可以包含斜杠
            uuid:接受UUID字符串
'''
app.run()