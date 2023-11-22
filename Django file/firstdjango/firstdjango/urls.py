"""firstdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include    #path 只能匹配正常的路径，re_path能使用正则匹配路径
from django.views.generic import TemplateView
from firstApp import views as tv
from firstApp import second
from firstApp.views import class_view

urlpatterns = [
    path('', admin.site.urls),
    re_path('^Ctime/',tv.Ctime), #如果输入的url路径是127.0.0.1:8000/time   则运行后面一个视图函数，注意：这个函数不用括号也不用参数

    #正则讲解：
    #尖括号(^)表示以后面的内容开头
    #圆括号（()）括号里面是一个参数，里面的内容作为参数传递给被调用的函数，就是tv.withparam
    #参数名称以问好加大写P开头，尖括号内的就是参数名
    #尖括号(<>)后面的就是正则，[0-9]表示内容只能是有一个0-9的数字构成
    #大括号（{}）表示出现的次数，{4}表示只能出现4个0-9之中的数字
    re_path(r'^withparam/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])',tv.withparam),   #?P后面的是参数

    path('student_path',tv.path),

    path('student',include(second)),         #include
    re_path(r'^book/(?:page-(?P<page_number>\d+)/)$',tv.book),  #加入参数
    re_path(r'^my/$',tv.extremParam,{'name':'lxy','age':'18'}), #多个参数
    re_path(r'^address/$',tv.add,name='adds'),       #URL反向解析
    re_path(r'^exp',tv.exception),    #http404

    #HttpResponseRedirect
    re_path(r'^redirect_1',tv.redirect_1),
    re_path(r'^redirect_2',tv.redirect_2),
    re_path(r'^redirect_hello',tv.redirect,name='redirect'),

    re_path(r'^get/',tv.get),       #GET传值

    #POST传值
    re_path(r'^post_get/',tv.post_get),
    re_path(r'^post/',tv.post),

    #render
    re_path(r"^render1/",tv.render1),
    re_path(r"^render2/",tv.render2),
    re_path(r"^render3/",tv.render3),

    #内建视图
    re_path(r'^NotFound_404/',tv.NotFound_404),

    #基于类的视图     #TemplateView.as_view这个视图函数是系统自带
    re_path(r'as_view/',TemplateView.as_view(template_name="render1.html")), #最简单
    re_path(r'class_view/',class_view.as_view()),   #需要在基于类的视图下面定义一个template_name
]
