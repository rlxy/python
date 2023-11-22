"""
Filename: 01ndarray和图片.py
Author: 药药
Contact: 1579954422@qq.com
introduce：转义字符(\\)，格式化数据，占位符(%,format),对数字的格式化注意点，**解包操作
"""


#转义字符案例
#想表达Let' s Go
#使用转义字符'\'
#s = 'Let\' s Go '
#s = "Let' s Go "              #这是用双引号括起Let' s Go，让双引号不会和里面的当引号分辨错误
#print(s)
#表示斜杠
#比如表示C：\User\Augsnano
#s = 'C:\\User\\Augsnano'     #这里是用反斜杠对反斜杠进行转义，\U在python中有别的意思，所以用了反斜杠对他进行转义
#print(s)

#用转义字符回车换行，使用\n，windows用\r\n\意思相同
# 想表达的效果是：
'''
ich
lieb
Zhengyanxin
'''
#s = 'ich\nlieb\nZhengyanxin'
#print(s)

                                                # 格式化
                    # 传统格式化
  # %s 表示简单的字符串
    # 占位符可以单独使用
s = 'I love %s'
print(s%'zhengyanxin')
print('I love %s'%'zhengyanxin')  #占位符一般只可以被同类型转换，或者替换类型能被转换成占位符的类型

#j = 'i am %fKG weight,%fm Heigh'
#如果需要格式化的信息多于一个，则用括号括起来就可以了，这个打印使用了默认格式，多打出来了好多0
#print(j%(55,1.65)  )
#实际需要进行格式化的信息的数量必须与百分号后面给出的数据匹配，否则报错
#j = 'i am %.2fKG weight,%.2fm Heigh'       #这里需要n个小数点就在%后面填.n
#print(j%(55,1.65))

                    # format
#不用指定位置，按顺序读取   {}这里这个是个占位符
#方式一
#s = '{} {} !'
#print(s.format('hello','word'))
#方式二
#s = '{} {} !'.format('hallo', 'word')
#print(s)
 #设置指定位置1
#s = '{0} {1} ! '.format('hallo', 'word')
#print(s)
#设置指定位置2
#s = 'I love {0} and {0} loves me'.format('z')
#print(s)
#使用命名参数,       参数不能填数字
#s = 'what is love，{z}，{x}，{y}。'
#s = s.format ( z= 'blush', x='heartbeat', y='no words')
#print(s)
#上面的案例可以通过字典设置参数，不过需要解包
#s = 'what is love，{z}，{x}，{y}。'


#s_dict = { 'z' : 'blush', 'x' : 'heartbeat', 'y' : 'no words'}
#s = s.format(**s_dict)          # **是解包操作，不解包就会报错
#print(s)
# 对数字的格式化需要用到
#s = 'Li xinyao is {:.2f}m heigh, {:.2f}KG weight'
#print(s.format(1.65, 55))
