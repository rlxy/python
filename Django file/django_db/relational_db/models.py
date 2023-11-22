from django.db import models

# Create your models here.

## 一比一 关系型数据表
class school(models.Model):
    school_id = models.IntegerField()
    school_name = models.CharField(max_length=20)
    # my_manage = models.OneToOneField('Manage',on_delete=models.CASCADE)   #关系建立一次就行，Manage中建立了
    def __str__(self):
        return self.school_name

class Manage(models.Model):
    manage_id = models.IntegerField()
    manage_name = models.CharField(max_length=20)

    my_school = models.OneToOneField(school,on_delete=models.CASCADE)
                        #django2.0以后创建关联表就需要多一个on_delete参数，否则报缺少参数错误
    def __str__(self):
        return self.manage_name

class teacher(models.Model):
    teacher_name = models.CharField(max_length=20)
    my_school = models.ForeignKey(school,on_delete=models.CASCADE)
    def __str__(self):
        return self.teacher_name