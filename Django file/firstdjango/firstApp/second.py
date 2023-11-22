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
from firstApp import views as tv


urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path('^time/',tv.Ctime), #如果输入的url路径是127.0.0.1:8000/time   则运行后面一个视图函数，注意：这个函数不用括号也不用参数



    re_path('lixinyao',tv.do_lxy),      #子路由
]
