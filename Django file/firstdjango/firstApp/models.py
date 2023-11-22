from django.db import models

#举例一个模型
#数据库应有一个对应的表名叫firstdjango
#里面有四个字段：name，age，address，course
class firstdjango(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    course = models.CharField(max_length=20)
# Create your models here.
    def __str__(self):
        return self.name






'''
命令行打开数据库保存数据的方法：
进入到文件下的终端，导入需要使用的数据库那个类  （这里拿firstdjango演示）
from firstApp.models import firstdjango as f

增
t = f()     实例化这个类 方便操作
t.name = 'xxx'  给对象赋值想要保存的数据  后面数据的格式要按照类里面设置的要求来
t.age = x
t.address = 'xxxxx'
t.course = 'xxxxx'
t.save()      最后需要save保存到数据库中去

删


查
f.objects.all()    查看f（firstdjango）类下的所有表
f.objects.all()[0].name   查看f下第一个表里面name的信息
f.objects.all()[0].age    age信息
f.objects.all()[0].address   address信息
f.objects.all()[0].course    course信息

'''
