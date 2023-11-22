#matplotilib 库
    -这是一个强大的绘图库，能够将数据绘制成沟中2D图形
    -其一系列功能完善的api可以帮助我们快速建立起我们需要的图形
    
    
     import matplotilib.pyplot as plt  #as用来赋予pyplot别名plt
     plt.title('标题'，fontsize=num)   用于编写图形的标题，fontsize是字体大小
     plt.ylabel('y轴名'，fontsize=num) 用于编写y轴的名字
     plt.xlabel('x轴名'，fontsize=num)  用于编写X轴名字
     plt.plot(squares,linewidth=5)  用来编辑图形的形状宽度，squares是正方形，linewidth是宽度
     tick_params(axis='both',labelsize=12)方法：设置坐标轴刻度的样式，实参axis='both'表示同时设置两条轴，
        也可以为x和y单独设置,
   