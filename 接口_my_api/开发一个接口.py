import flask,json,pymysql


#flask是一个轻量级的开发框架

server = flask.Flask(__name__)  #把当前这个文件当做一个服务  __name__代表当前文件
db = pymysql.connect(host='localhost',user='root',password='root',db='USER_PASS')

#/index是接口路径
@server.route('/index',methods=['get'])     #methosd默认是get，也可以写多种['get'，'post']
def reg():
    username = flask.request.values.get('username')#获取传入的参数
    pwd = flask.request.values.get('passwd')
    if username and pwd :
        sql = 'select * from mv user where username = "%s";'%username
        if db(sql):
            res = {'msg':'用户名已存在'}
        else :
            insert_sql = 'insert into mv user (username,passwd is admin) values ("%s","%s",0);'%(username,pwd)
            db(insert_sql)
            res = {'msg':'注册成功'}
    else:
        res = 'ERROR'

    return json.dumps(res,ensure_ascii=False)   #ensure_ascii=False 可以显示中文了
server.run(port=8999,debug=True)    #post是端口号，默认5000   debug=True，这样修改代码后不需要重新启动服务