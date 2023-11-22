from django.shortcuts import render,reverse
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView

# Create your views here.
import time



#这个函数就是视图函数，应该有个参数，参数类型是HttpResponse

#每个视图函数中都应该带有一个参数，request，代表的是请求

def Ctime(request):
    return HttpResponse('这是时间戳{}'.format(time.ctime()))    #这里返回到网页上的内容

def withparam(request,year,month):
    return HttpResponse('你进入的是{}年{}月下的文件'.format(year,month))

def do_lxy(request):
    return HttpResponse('这是一个子路由')

def path(request):
    return HttpResponse('你进入了{}'.format(__file__))

def book(request,page_number):
    return HttpResponse('this is page {}'.format(page_number))

def extremParam(request,name,age):
    return HttpResponse('My name is {} and age is {}'.format(name,age))

def add(request):
    return HttpResponse('you access is {}'.format(reverse('adds')))




def exception(request):
    raise Http404   #直接返回 404   进入报错处理，不处理下面的返回
    return HttpResponse('访问正常？？？')

#重定向url
def redirect_1(request):
    return HttpResponseRedirect('redirect_hello') #重定向，redirect重定向到这个路由的位置，  路由
def redirect_2(request):
    return HttpResponseRedirect(reverse('redirect'))    #reverse：重定向的位置是viewname，并不是路由的位置   viewname
def redirect(request):
    return HttpResponse('welcome to redirect!')

def get(request):       #GET传值
    rsult=''
    for k,v in request.GET.items():
        rsult += k + '---' + v
        rsult += ','
    return HttpResponse('Get value of request is {}'.format(rsult))

def post_get(request):
    #渲染一个HTML模板并返回
    return render(request,'post_get.html')  #for_post.html放在templates里面
#在html页面把信息用post传输过去，需要在设置中把csrf防护关闭，因为这里涉及到了一个攻击(setting我已经设置过了)
def post(request):
    rsult=''
    for k,v in request.POST.items():
        rsult += k + '--' + v
        rsult += ','
    return HttpResponse("Get value of POST is {}".format(rsult))

def render1(request):
    response = render(request,'render1.html')
    return  response
def render2(request):
    #上下文环境，这里必须是一个字典格式，用来替换模板中的变量
    c = dict()
    c['name'] = 'render2'
    c['age'] = 'fifty years old'
    #这是自动找到了render2.html模板
    response = render(request,'render2.html',context=c) #context 这个就是上下文环境参数
    return  response
def render3(request):
    from django.template import loader
    tem = loader.get_template('render2.html')       #用loader手动选择模板
    r = tem.render({'name':'render3','age':'fifty years old'})
    #这个时候r不是HttpResponse的子类，下面返回的话需要手动生成一个HttpResponse用来返回
    return HttpResponse(r)

def NotFound_404(request):
    from django.views import defaults
    return defaults.page_not_found(request,exception)    #模板也可以自定义，这个是内建的模板

#下面是基于类的视图（还一种简单的方法直接在urlconf中使用）
class class_view(TemplateView):
    template_name = 'render1.html'      #这种方法要求在类下面定义一个template_name
