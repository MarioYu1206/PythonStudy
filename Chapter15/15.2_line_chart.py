import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
plt.plot(squares)
plt.show()

#修改标签文字和线条粗细
squares = [1,4,9,16,25]
plt.plot(squares, linewidth=5)
#设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
#设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14)#设置刻度样式
plt.show()

#校正图形
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values,squares,linewidth=5)#指定输入值和输出值
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',labelsize=14)
plt.show()

#使用scatter()绘制散点图并设置其样式
plt.scatter(2,4)
plt.show()

#scatter()绘制单个点
plt.scatter(2,4,s=200)
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.show()

#scatter()绘制一系列点
x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]
plt.scatter(x_values,y_values,s=100)
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.show()

#自动计算数据
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,s=40)
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.axis([0,1100,0,1100000]) #设置每个坐标轴的取值范围
plt.show()

#删除数据点的轮廓
plt.scatter(x_values,y_values,edgecolors='none',s=40)
plt.show()

#自定义颜色
plt.scatter(x_values,y_values,c='red',edgecolors='none',s=40)
plt.show()
plt.scatter(x_values,y_values,c=(0,0,0.8),edgecolors='none',s=40)#支持RGB
plt.show()

#使用颜色映射（colormap），它们从起始颜色渐变到结束颜色。 在可视化中， 颜色映射用于突出数据的规律
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
edgecolor='none', s=40)
plt.show()

#自动保存图表
plt.savefig('squares_plot.png',bbox_inches='tight')


#练习
#practice 1
x_values = [1,2,3,4,5]
y_values = [x**3 for x in x_values]
plt.scatter(x_values,y_values,s=40)
plt.show()

x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values,y_values,s=40)
plt.show()


#practice 2
x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap='viridis',s=40)
plt.show()
