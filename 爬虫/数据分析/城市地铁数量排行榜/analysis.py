import pandas as pd             #pandas是强大的分析结构化数据的工具集   as是赋予pandas别名
from matplotlib import pyplot as plt    #2D绘图库，通过这个库将数据绘制成各种2D图形（直方图，散点图，条形图等）

#全国哪一个城市地铁线最多
def subline_count():
    df1 = df.iloc[:, :-1]        #筛选前三列      df是下面main读取的
    df2 = df1.drop_duplicates(subset=['city', 'subwayline'])     # 去重
    # drop_duplicates是pandas里面的函数   subset用来指定特定的列，不填参数就默认所有列

    df3 = df2['city'].value_counts()    #pandas里面的value_counts()函数可以对Series里面每个值进行计数并排序
    df3.plot.bar()      #bar条形图
    plt.savefig("城市地铁数量排行榜.png")
    plt.show()      #将处理后的数据显示出来

    print(df3)
if __name__=='__main__' :
    df = pd.read_csv('subway.csv', encoding='utf-8')   #读取subway.csv文件，并制定字符集的类型
    plt.rcParams['font.sans-serif'] = 'fangsong'    #font.sans-serif就是修改字体，后面是仿宋字体
    #rcParams可以修改默认属性，包括窗体大小，每英寸的点数，线颜色，样式，坐标轴，坐标和网络属性，文本，字体等

    subline_count()     #运行函数

