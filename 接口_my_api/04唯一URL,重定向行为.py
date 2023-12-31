import flask

app = flask.Flask(__name__)

#唯一的 URL / 重定向行为
@app.route('/projects/')
def projects():
    return 'The project page,url末尾有个斜杠'
#projects 的 URL 是中规中矩的，尾部有一个斜杠，看起来就如同一个文件夹。 访问这个URL如果没加斜杠时Flask 会自动进行重定向，帮你在尾部加上一个斜杠。

@app.route('/about')
def about():
    return 'The about page,末尾没有斜杠'
#about 的 URL 没有尾部斜杠，因此其行为表现与一个文件类似。如果访问这个 URL 时添加了尾部斜杠就会得到一个 404 错误。这样可以保持 URL 唯一，并帮助 搜索引擎避免重复索引同一页面。

app.run()