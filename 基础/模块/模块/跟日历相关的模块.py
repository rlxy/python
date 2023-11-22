#calendar
import calendar     #关于日历的模块包   calendar是获取某一年的日历
cal = calendar.calendar(2018)       #打印2018年的日历
print(cal)
cal = calendar.calendar(2018,l = 0,c =5)        #2018后面的参数，是指日历之间的间隔
print(cal)

#isleap,判断是否为闰年
year  = calendar.isleap(1989)
print('是否为闰年:{0}'.format(year))

#leapdays,获取指定年份之间的闰年的个数
leap = calendar.leapdays(2000,2019)             #判断2000 到 2019 年中间有多少闰年
print('闰年个数：{0}'.format(leap))

#month(),获取某个月的日历
m5 = calendar.month(2019,5)              #获取2019年5月的日历
print(m5)

#monthrange() 获取一个月是周几开始和这个月的天数    注意：周默认0-6，表示周一到周日
t,w = calendar.monthrange(2019,8)
print('这个月从周{0}开始'.format(t))
print('这个月共有{0}天'.format(w))

#monthcalendar()
#返回一个整数的单层嵌套列表。每个子列表装载一个星期。该月之外的日期都为0，该月之内的日期设为该日的日期，从1开始。
m = calendar.monthcalendar(2019,8)
print(m)

#prcal() 直接打印一年的日历
y = calendar.prcal(2019)
print(y)

