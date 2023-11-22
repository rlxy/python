def hello(person):         #def是一个函数，def起了一个hello的名字，person是一个参数，占位置的
	print("{0}，你好吗？".format(person))         #format的意思就是让person这个变量替换调大括号里面的值
	print("{}，你看见他了吗？".format(person))
p = '小明'      #把‘小明’赋值给p
hello(p)               #调用参数，把p作为实参传入，此时person这个没有意义用来占位置的已经变成p这个变量了
