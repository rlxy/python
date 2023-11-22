#dict：字典
#字典是一种组合数据，没有顺序的组合数据，数据以键值对形式出现
#字典的创建
#创建空字典1
d = {}
print(d)
#创建空字典2
d = dict()
print(d)
#创建有值的字典，每一组数据用冒号隔开，每一对键值对用逗号隔开
d = {"one":1,"two":2,"three":3}
print(d)
#用dict创建有内容的字典2
d = dict({"one":1,"two":2,"three":3})
print(d)
#用dict创建有内容的字典3
d = dict(one=1,two=2,three=3)
print(d)
#
d = dict({("one",1),("two",2),("three",3)})
print(d)
#字典的特征
  #字典是序列类型，但是是无序序列，所以没有分片和索引
  #字典中的数据每个都有键值对组成，即kv对
    #key：必须是可哈希的值，比如int，string，float，tuple，但是list，set，dict不行
    #value：任何值
#字典常见操作
   #访问数据
d = {"one":1,"two":2,"three":3}
#注意访问格式，中括号内是键值
print(d['one'])
d['one'] = '一'
print(d)
#删除某个操作
#使用del操作
del d['one']
print(d)

#成员检测in，not in
#成员检测检测的是key内容
d = {"one":1,"two":2,"three":3}
if 'two' in d:
    print('key')
#遍历再python2和python3中区别比较打，代码不用
#按key来使用for循环
d = {"one":1,"two":2,"three":3}
#使用for循环，直接按key值访问
for k in d:
    print(k,d[k])
#上面代码可以改成
for k in d.keys():
    print(k,d[k])
#只访问值
for v in d.values():
    print(v)
#注意以下用法,需要使用items来表示键值对
for k,v in d.items():
    print(k,'--',v)
#常规字典生成
d = {"one":1,"two":2,"three":3}
dd = {k:v for k,v in d.items()}
print(dd)
#其实没什么意义，只是可以用来加限制条件的字典生成
dd = {k:v for k,v in d.items() if v % 2 == 0}           #这里加了一个条件，只有是偶数才生成
print(dd)

#字典相关函数
#通用函数：len，max，min，dict
#str（字典）：返回字典的字符串格式
d = {"one":1,"two":2,"three":3}
print(str(d))
#clear:清空字典
#itmes：返回字典的键值对组成的元组格式  返回可遍历的（键，值）元组数组
d = {"one":1,"two":2,"three":3}
i = d.items()
print(type(i))  #type:查看类型
print(i)
#keys：返回字典的建组成的一个结构
k = d.keys()
print(type(k))
print(k)
#values:同理，一个可迭代的结构
v = d.values()
print(type(v))
print(v)
#get：根据制定键返回相应的值，好处是，可以设置默认值
d = {"one":1,"two":2,"three":3}
print(d.get('one1'))     #返回相应的值，值不存在则返回默认值
#get默认值是None，可以设置
print(d.get('one',100))             #返回one的值，不存在就返回100
print(d.get('one1',100))
#formkeys；使用指定的序列作为键，使用一个值作为字典的所有键的值
l ={'one','two','three'}
#注意fromkeys两个参数的类型
#注意fromkeys的调用主体
d = dict.fromkeys(l,'111111')
print(d)


