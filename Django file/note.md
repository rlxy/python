Django
-参考资料
    -[django中文文档](https://yiyibooks.cn/)
    -参考书：django架站的16堂课
###Django安装
pip install Django django可以指定版本(django==版本)

#####创建第一个django程序
-django-admin startproject firstdjango #创建项目
    -这个项目文件中带有一个同名目录和一个启动程序(manage.py)
    -同名目录中带有__init__.py,基本的配置文件(settings.py),asgi.py,urls.py,wsgi.py
### manage.py :
    -python manage.py runserver #启动服务  
#路由系统-urls.py
    -创建app
        -此app非彼app，全名application应用
        -app：负责一个具体业务或者一类具体业务的模块
        -python manage.py startapp firstApp #创建一个app
    -路由
        -按照具体的请求url，导入到相应的业务处理模块的一个功能
        -django的信息控制中枢
        -本质上是接受的URL和相应的处理模块的一个映射
        -在接受URL请求的匹配上使用了RE
        -URL的具体格式如urls.py中所示
    -url需要关注的两点：
        -接受的URL是什么，如何用RE对这个URL进行匹配
        -已知URL匹配到哪一个处理模块
        
    -URL匹配规则
        -从上往下一个一个比对
        -url格式是分级格式，则按照级别一级一级往下比对，主要对应url包含子url的情况
        -子url一旦被调用，则不会返回到主url
            -/one/two/three/
        -正则以r开头，表示不需要转义，注意尖括号（^）:从头开始匹配
                                     美元符号（$）：结尾一定是以美元符号前面的结束，所以美元符号都是放在末尾
            #下面的例子以/开头，路由会自动把第一个斜杠忽略              
            -'/one/two/three'  r'^one/'匹配
            -'/oo/one/two/three'    r'^one/' 不匹配
            -'/one/two/three'   r'three/$' 匹配
            -'/oo/one/two/three/oo/'    r'three/$'
        -如果从上向下都没有找到合适的匹配内容，则报错
    # 2.正常映射
    -把某一个符合RE的URL映射到事物处理函数中去
    -举例如下：
          ‘’‘
          from showeast import views as sv
          urlpatterns = [
              url(r'^admin/',admin.site.urls),
              url(r'^normalmap/',sv.normalmap)
          ]
          ’‘’
    # 3.URL中带参数映射 
    - 在事件处理代码中需要由URL传入参数，例如/myurl/param中的param
    - 参数都是字符串形式 ，如果需要整数形式需要自行转换
    - 通常的形式如下：
        ‘’‘
            /search/page/432 中的432需要经常性变换，所以设置成参数比较合适
        ’‘’
         
       
    # 4.URL在app中处理
        -如果所有应用URL都集中在一个urls.py文件中，可能导致文件的臃肿
        -可以把urls具   体功能逐渐分散到每个aoo中
            -从django.conf.urls 导入 include
            -注意此时RE部分的写法
            -添加include导入
        -使用方法
            -确保include被导入
            -主路由的url
            -子路由的url
            -views函数
        -同样可以使用参数
    # 5.URL中的嵌套参数
        -捕获某个参数的一部分
            -例如URL /index/page-3，需要捕获数字3作为参数
            ‘’‘
            re_path(r'index_1/(page-(\d+)/)?$',sv.myindex_1)  #这种方法没下面那种好
            re_path(r'index_1/(?:page-(?P<page_number>\d+)/)?$',sv.myindex_2)
            '?:' 表示忽略后面一个参数(page-),'?P'表示后面的尖括号内是一个可变参数(page_number),\d+ 表示至少有一个数字，
             ?匹配前面的字符零次或一次， $ 表示已经是结尾了
            ’‘’
    # 6.传递额外的参数
        -参数不仅仅来自URL，我们还可以自己定义参数
        ‘’‘
        re_path(r'myname/$',sv.extremParam,{'name':'lxy','age':'18'})  #后面那个字典就是自定义参数，前面是参数名，后面是参数代表的是什么
        ’‘’
        -附加的参数同样适用于include语句，此时对include内所有都添加
    # 7.URL的反向解析
        -防止硬编码
        -本质上是对每一个URL进行命名
        -以后在编码代码中使用URL的值，原则上都应该使用反向解析
        
# views 视图
    # 1.视图概述
    -视图及视图函数，接受web请求并返回web响应的食物处理函数
    -响应指符合http协议要求的任何内容，包括json,string,html 等
    # 2.简单视图 
        -django.http给我们提供了很多和HttpResponse类似的简单视图，可以通过查看django.http代码
        -下面介绍几种
            -最基础的一个视图就是HttpResponse，返回最基础的字符串
            -Http404是Exception(异常)的子类，需要引发出来，所以我们需要通古今哦raise使用
        -此类视图使用方法基本类似，通过return语句直接反馈给浏览器
    # 3.HttpResponse详解
    -方法 
        -init:使用页面内容实例化HttpResponse对象
        -write(content):以文件的方式写
        -flush():以文件的方式输出缓存区
        -set_cookie(key,value='',max_age=None,expires=None) :设置cookie
            - key,value都是字符串类型
            - max_age是一个整数，表示在指定秒数后过期
            - expires是一个datetime或timedelta对象，会话将在这个指定的日期/时间过期
            - max_age 和expires二选一
            - 如果不指定过期时间，则两个星期后过期
        - delete_cookie(key):删除指定的key的Cookie，如果key不存在则什么也不发生
    # 4.HttpResponseRedirect
      -重定向，服务器端跳转
      -构造函数的第一个参数用来指定重定向的地址
          
    # 5.Request对象  请求对象
    - Request介绍
        - 服务器接收到http协议的请求后，会根据报文创建HttoRequest对象
        - 视图函数的第一个参数是HttpRequest对象
        - 在django.http模块中定义了HttpRequest对象的API
    - 属性
        - 下面除非特别说明，属性都是只读的，因为既然是请求，已经发出了，再更改也没有任何意义
        - path： 一个字符串，表示请求的页面的完整路径，不包含域名
        - method：一个字符串，表示请求使用的HTTP方法，常用值包括：'GET','POST'
        - encoding：一个字符串，表示提交的数据的编码方式
            - 如果为None则表示使用浏览器的默认配置，一般为utf-8
            - 这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码，接下来对属性的任何访问将使用新的encoding值
        - GET：一个类似于字典的对象，包含get请求方式的所有参数
        - POST：一个类似于字典的对象，包含post请求方式的所有参数
        - FILES：一个类似于字典的对象，包含所有的上传文件
        - COOKIES：一个标准的python字典，包含所有的cookie，键和值都为字符串
        - session：一个即可读又可写的类似于字典的对象，表示当前的会话，只有当Django启用会话的支持时才可用，详细内容见“状态保持”。
    - 方法
        - is_ajax()：如果请求是通过XMLHttprequest发起的则放回True
    - QueryDict对象
        - 定义在django.http.QueryDict
        -request对象的属性GET,POST都是QueryDict类型的对象
        -与python字典不同，QueryDict类型的对象用来处理同一个键带有多个值的情况
        -方法get()：根据键获取值
            - 只能获取键的一个值    
            - 如果一个键同时拥有多个值，则获取最后一个值
        -方法getlist()：根据键获取值
            - 将键的值以列表放回，可以获取一个键的多个值
    - GET属性
        -QueryDict类型的对象
        -包含get请求方式的所有参数
        -与url请求地址中的参数对应，url地址后位于？后面面填键，
        -参数的格式是键值对，如key1=value1
        -键是开发人员定下来的，值是可变的
        
    - POST属性
        -QueryDict类型的对象
        -包含post请求方式的所有参数
        -与form表单中的控件对应
        -表单中控件必须有name属性，name为键，value为值
            -checkbox存在一键多值的问题
        -键是开发人员定下来的，值可变    
        -setting中需要设置模板位置   （创建一个文件夹，一般叫做templates，里面放网页）
        -设置get页面的urls和函数

    - 手动编写视图
        -利用django快捷函数手动编写视图处理函数
        -分析
            -django把所有信息封装入request
            -django通过urls模块把相对应请求跟事件处理函数连接起来，并把request作为参数传入
            -在相应的处理函数中，我们需要完成两部分
                - 业务处理
                - 把结果封装并返回，我们可以使用简单HttpResponse，同样也 可以使用它的子类
                注意：这里不介绍业务处理，注重如何渲染结果并返回
        render(request,template_name[,context][,context_instance][,content_type])              
            -使用模板和一个给定的上下文环境，返回一个渲染的HttpResponse
            -request：django的请求 （必要）
            -template_name:模板名称（例如html模板）
            -context_instance:上下文环境
        -render_to_response() ##新版本中django已经把render_to_response 移除了，render功能更完美
            - 根据给定的上下文字典格式的内容渲染给定模板，返回渲染后的HttpResponse
            
    - 系统内建视图
        -系统内建试图，可以直接使用
        -404
            -default.page_not_found(request,template_name='404.html')
            -系统引发Http404时触发
            -setting.py里设置DEBUG=True则不会调用404，取而代之的就是调试信息
            -404视图会被传递一个RequestContext对象并且可以访问模板上下文处理器提供的变量
        -500（server error）   
            -defaults.server_error(request,template_name='500.html')
            -需要设置DEBUG=False，否则不会调用
        - 403(HTTP Forbidden)视图
            - defaults.permission_denied(request, template_name='403.html')
            - 通过PermissionDenied触发
        - 400(bad request)视图
            - defaults.bad_request(request, template_name='400.html')
            - DEBUG=False
    
    - 基于类的视图
        -和基于函数视图的优势和区别
            -HTTP方法的methode可以有各自的方法，不需要使用条件分支来解决
            -可以使用OOP技术(例如Mixin)
        -概述
            -允许使用不同的实例方法来相应不同的HTTP请求方法，从而避开条件分支实现
            -as_view函数作为类的可调用入库，该方法创建一个实例并调用dispatch方法，按照请求方法区队请求进行分发
                /如果该方法没有定义，则引发HttpResponseNotAllowed
        -类属性使用
            -在定义时直接覆盖
            -在调用as_view的时候直接作为参数使用，例如：
　　             '''
                 urlpatterns = [
　　              re_path(r'^about/', GreetingView.as_view(greeting="G'day")),
　　              ]
                '''
            -对基于类的视图的扩充大致有三种方法：Mixin，装饰as_view，装饰dispatch
            -使用Mixin
                -多继承的一种形式，来自父类的行为和属性结合在一起
                -解决多继承问题
                -View的子类只能单继承，多继承会导致不可期问题
                -多继承带来的问题：
                    -结构复杂
                    -优先顺序模糊
                    -功能冲突
                -解决方法
                    -规格继承  -java interface
                    -实现继承  -python，ruby
            -最简单方法是直接在URLconf中创建它们
                ```
            　　from django.views.generic import TemplateView
            　　urlpatterns = [
            　　url(r'^about/', login_required(TemplateView.as_view(template_name="secret.html"))),
            　　]
            　　```
            -子类化通用视图
                -使用通用视图的第二种更强大的方法是
                    从现有视图继承并覆盖子类中的属性（例如template_name）或方法（例如get_context_data）以提供新值或方法。
                url：
                    from django.urls import path
                    from django.views.generic import TemplateView
                    urlpatterns = [
                        path('about/', TemplateView.as_view(template_name="about.html")),
                    ]
                view：
                    from django.views.generic import TemplateView
                    class AboutView(TemplateView):
                        template_name = "about.html"

            -装饰类
                -类的方法和独立方法不同，不能直接运用装饰器，需要用methode_decorator进行装饰
                    　　　　```
                    　　　　from django.contrib.auth.decorators import login_required
                    　　　　from django.utils.decorators import method_decorator
                    　　　　from django.views.generic import TemplateView
                    
                    　　　　class ProtectedView(TemplateView):
                    　　　　　　template_name = 'secret.html'
                    
                        　　　　@method_decorator(login_required)       
                        　　　　def dispatch(self, *args, **kwargs):
                        　　　　　　return super(ProtectedView, self).dispatch(*args, **kwargs)    
                                    
#Models模型
    -ORM(objectRelationMap):把面向对象思想转换成关系数据库思想，操作上把类当成数据库里的一张表
        -类对应表格
        -类中的属性对应表中的字段
        -在应用中的models.py文件中定义class
        -所有需要使用ORM的class都必须是models.Model的子类
        -class中所有属性对应表格中的字段
        -字段的类型都必须使用models.xxx 不能使用python中的类型
        -在django中Models负责跟数据库交互
    -django链接数据库
        -自带默认的数据库sqlite3
            -关系型数据库
            -轻量级
            -单文件数据库，所有数据存放在一个文件
        -切换数据库
            -在实际部署的时候切换成别的适合的数据库
            -1.切换数据库在setting中设置
                # django链接mysql
                DATABASE = [
                    'default':{
                    'ENGINE':'django.db.backends.mysql',
                    'NAME' : '数据库名',
                    'PASSWORD' : '数据库密码',
                    'HOST':'123.0.0.1', #数据库HOST
                    'PORT':'3306',  #数据库端口一般都是3306
                    }
                ]
            -2.需要在项目文件下的__init__.py文件中导入pymysql包
                ‘’‘
                #在主项目下的__init__.py文件中
                import pymysql
                pymysql.install_as_MySQLdb()
                ’‘’
        -models类的使用
            -定义和数据库表映射的类(称为模型)
                -在应用中的models.py文件中定义class
                -所有需要使用MOR的class都必须是models.Model的子类,不然在数据库迁移的时候检测不到app的任何变化 （基类，models.Model必须得是父类）
                -数据库表格中的字段都应该在class里面有一个属性相对应
                -字段的类型都必须使用modles.xxx不能使用python中的类型  
                    #modles是模块，里面有表示数据库数据的数据类型
                    列举：  
                        modles.CharField :字符串类型(定义字符串类型需要给个max_length限制)
                        odles.IntegerField:整数类型（可以不用限制也可以限制整数类型大小）
            - 字段常用参数
                1、max_length:规定数值的最大长度
                2、blank:是否允许字段为空，默认不允许
                3、null:在DB中控制是否保存为null，默认为false
                4、default:默认值
                5、unique:唯一
                6、verbose_name:假名  
                 
        -数据库
            -数据库的迁移(在models里创建类后通知数据库)
                1.在命令行中，生成数据迁移的语句(生成sql语句)
                    python manage.py makemigrations
                2.在命令行中，输入数据迁移的指令
                    python manage.py migrate
                如果迁移中没有变化或者报错，可进行强制迁移
                    1.python manage.py makemigrations APP名
                    1.python manage.py migrate APP名  
                ‘’‘
                对于默认数据库(sqlites3),避免迁移数据库后因为多个数据库混乱，
                可以删除自定义app下面的migrations文件夹和db.sqlites3数据库
                (前提保证数据库内数据不需要或者提前备份)
                ’‘’
            —数据库数据查询
                1.命令行启动数据库：python manage.py shell  (在django文件下面的cmd启动)
                    #注意点：对orm的操作分为静态函数和非静态函数两种，静态函数是指在内存中类共用的，非静态函数是指每个f.实例掌握的
                2.启动之后需要先导入相应的映射类  导入app中的models.py文件  
                    from 应用.models import 类名
                3.使用object属性操作数据库，object是模型中实际和数据进行交互的
                4.查询命令
                    类名.objects.all() 查询数据库中的所有内容，放回结果是一个QuerySet查询， 在映射类中可以调用魔法函数 __str__
                    类名.objects.filter(要查找属性的条件)
                        常见查找方式  
                            1.通用查找格式，属性名__条件符号=值
                                条件符号：
                                    gt：大于
                                    gte：大于等于
                                    lt：小于
                                    lte：小于等于
                                    range：范围
                                    year：年份
                                    isnull：是否为空
                            2.直接指定值的格式，精确查找：属性名=值
                                类名.objects.filter(属性=条件) ：精确查找属性是什么的数据
                            3.模糊查找：属性名__查找方式=值
                                查找方式有:
                                    exact:精确等于
                                    iexact:不区分大小写
                                    contains：包含
                                    startwith：以...开头
                                    endwith：以...结尾
                                    
                                    
    - 数据库表关系
        -多表联查：利用多个表联合查找某一项信息或多项信息
        
        1:1  One To One   一对一
            -增：
                -添加没有关系的一边，直接实例化保存就可以
                    s = school()
                    s.school_id = 1
                    s.school_name = 'jd'
                    s.save()
                -添加有关系的一边，使用create方法，或者使用实例化然后save
                    # 方法一
                        m = Manage()
                        m.manage_id = 1
                        m.manage_name = 'lixin'
                        m.my_school = s     #s 是对应的表的信息,可以是school.objects.all()[0] 
                        m.save()
                    # 方法二：create方法
                        m = Manage.objects.create(manage_id=1,manage_name='lixin',my_school=s)    
                    一对一只能一个对一个
                -查：
                    由子表查母表，由子表的属性直接提取信息，建立了关系的一方为子表
                        Manage.objects.get(manage_name='药药').my_school.school_name  直接查询母表学校的信息
                    由母表查子表,使用双下划线
                        school.objects.get(manage__manage_name='yaoyao')  查询了manage_name='yaoyao'的school
                                            (这里好像是类名的小写)__manage_name='yaoyao'，，查资料说是类名的小写
                -改
                    - 单个的修改用save   
                         >>> a = school.objects.all()[0]
                         >>> a
                         <school: 育才>
                         >>> a.school_name = 'yucai'
                         >>> a.save()
                         >>> a
                         <school: yucai>
                    - 批量修改用update
                        >>> s = school.objects.all()
                        >>> s
                        <QuerySet [<school: yucai>, <school: 陶湾>]>
                        >>> s.update(school_name = '学校')
                        2
                        >>> s
                        <QuerySet [<school: 学校>, <school: 学校>]>
                    -子表母表都适用
                -删
                    -直接使用delete
                        >>> a = school.objects.all()[2]
                        >>> a.delete()
                        (2, {'relational_db.Manage': 1, 'relational_db.school': 1})
                        

        1:N  One To Many    一对N
            -一个表格的一个数据项/对象等，可以由很多个另一个表格的数据线/对象等
            -使用：需要在对象多的一方数据的表中添加属性：ForengnKey
            添加：
                --实例化添加
                    t = teacher()
                    t.teacher_name = '测试'
                    t.my_school = '测试'
                    t.save()
                -或者
                    t = teacher(teacher_name='测试',my_school='测试')
                    t.save()
                -跟一对一方法类似，通过create和new来添加
                -create：需要把属性填满，不需要手动save保存
                -new：属性参数可以为空，必须使用save保存
                
        
        
        N:N  Many To Many   N对N
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                