##正则表达式（RegularExpression，re）
#是一个计算机科学的概念
#用于使用单个字符串来描述，匹配符合某个规则的字符串
#常常用来检索，替换某些模式的文本

#正则的写法
'''
.（点号) 表示任意一个字符除了\n,比如哈找所有的一个字符\.
[] 匹配中括号中列举的任意字符，比如[L,Y,0],LLY,Y0,TIU就不行
\d  任意一个数字
\D 除了数字都可以
\s 表示空格，tab键
\S 除了空白符号
\w 单词字符  就是a-z,A-Z,0-9  除此之外都不行
\W 除了\w 行的不行，其他的都行
* 表示前面内容重复零次或者多次 |w*
+ 表示前面内容至少出现一i
？ 前面才出现的内容零次或者一次
{m,n} 允许前面内容出现最少m次，最多n次
^ 匹配字符串的开始
$ 匹配字符串的结尾
\b 匹配单词的边界
（） 对正则表达式内容进行分组，从第一个括号开始，编号逐渐增大

    验证一个数字： ^\d$
    必须有一个数字，最少以为 ^\d+$
    只能出现数字，且位数为5-10位  ^\d{5,10}$
    注册者输入年龄，要求16岁到99岁之间  ^[16-99]$
    只能输入英文字符和数字  ^[A-Za-z0-9]$
    验证qq号码  [0-9]{5,12}

\A 只匹配字符串开头  \Aabcd 则abce
\Z 仅匹配字符串末尾 abcd\z  则abcd
| 左右任意一个
（？p<name>...）  分组 除了原来的编号再制定一个别名，（？p<id>12345）{2}
(?p=name)  引用分组

'''



##RE 是用大致步骤
# 使用compile将表示正则的字符编译为一个pattern对象
# 使用pattern对象提供一系列方法对文本进行查找匹配，获取匹配结果，一个match对象
# 最后使用match对象提供的属性和方法获得信息，根据需要进行操作

##RE常用函数
#group():获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，直接使用gourp或者goup(0)
#start :获取分组匹配的子串在整个字符串中的起始位置，参数默认为0
#end：获取分组匹配的子串在整个字符串中的结束位置，默认为0
#span ：返回的结构技术（star(gourp),end(group)）

#导入相关的包
import re

#查找字符串里面的数字
#r表示字符不进行转义
p = re.compile(r'\d+')
m = p.match("jiangxi52yiyanglxy222",5,30)
print(m)
#在字符串"一串字符串，520在这13里面查找相14应的内容"中进行查找，按照规则p制定的正则进行查找
#返回结果时None表示没有找到，否则会返回match对象
#参数5，30表示在字符串中查找的范围
#查找到的结果只包含一个，第一次进行匹配成功的内容

#查找a-z的字母，查找两个，中间用空格隔开  re.l表示忽略大小写
# a = re.compile(r'([a-z]+) ([a-z]+)',re.l)
# m = p.match('i am lxy')
# print(m)
#print(m.group(0))      #获取一个或多个分组匹配的内容  0是所有 1的话就是第一个
# print(m.start(0))     #从第几个索引位置匹配到内容  参数填匹配到的第几个内容   0默认所有
# print(m.end(0))       #匹配到的内容最后一个索引
#print(m.groups())      #把匹配到的内容全部打印出来


##查找
#search(str,[,pos[,endpos]]):在字符串中查找匹配，pos和endpos表示起始位置
#findall：查找所有
#finditer：查找，返回一个iter结果

p = re.compile(r'\d+')
m = p.search('one11two22three33four44')
print(m.group())
rst = p.findall('one11two22three33four44')  #找到所有能找到的内容
print(rst)  #查找出来时个列表



##sub 替换
#sub（rep1，str[,count]）
p = re.compile(r'(\w+) (\w+)')      #\w是数字和字母，查找两个字符串（英文或数字） 两个字符串中间需要有空格隔开
s ='hello 123 bilbil 456 xinyao,i love you'
rst = p.sub(r'需要替换',s)      #参数填一个需要把匹配到的内容替换成的字符，s就是查找的内容
print(rst)


##匹配中文
#大部分中文内容表示范围是[u4e00-u9fa5],不包括全角标点
title = u'世界 你好，hello moto'
p = re.compile(r'[\u4e00-\u9fa5]+')     #+代表最少一个
rst = p.findall(title)
print(rst)


##贪婪和非贪婪
#贪婪：尽可能多的匹配，(*)表示贪婪匹配
#非贪婪：找到符合条件的最小内容即可，(?)表示非贪婪
#正则默认使用贪婪匹配
tt = u'<div>name</div><div>age</div>'
p1 = re.compile(r'<div>.*</div>')       #'.'表示任意一个内容 ，*贪婪匹配第一个<div>和最后一个</div>中间的所有内容
p2 = re.compile(r'<div>.*?</div>')      #‘？’非贪婪，只匹配第一个<div>和第一个</div>中间的所有内容

m1 = p1.search(tt)
print(m1.group())
m2 = p2.search(tt)
print(m2.group())







