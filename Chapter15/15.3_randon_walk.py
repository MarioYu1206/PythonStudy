#创建RandomWalk()类
from random import choice

class RandomWalk():
    """一个生成随机漫步数据的类"""
    def __init__(self,num_points=5000):
        self.num_points = num_points
        #所有随机漫步都始于（0,0）
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        direction = choice([1,-1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            #决定前进方向以及沿着个方向前进的距离
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance
            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance
            #拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
            #计算下一个点的x和y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def fill_walk2(self):
        while len(self.x_values) < self.num_points:
            #决定前进方向以及沿着个方向前进的距离
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4,5,6,7,8,9])
            x_step = x_direction * x_distance
            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4,5,6,7,8,9])
            y_step = y_direction * y_distance
            #拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
            #计算下一个点的x和y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def fill_walk3(self):
        while len(self.x_values) < self.num_points:
            #决定前进方向以及沿着个方向前进的距离
            x_step = self.get_step()
            y_step = self.get_step()
            #拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
            #计算下一个点的x和y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


#绘制随机漫步图
import  matplotlib.pyplot as plt

rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values,rw.y_values,s=15)
plt.show()

#模拟多次随机漫步
while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()
    keep_running = input("Make another walk? y/n: ")
    if keep_running =='n':
        break

#给点着色
while True:
    rw = RandomWalk()
    rw.fill_walk()
    point_number = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, s=15, c=point_number, cmap=plt.cm.Blues)
    plt.show()
    keep_running = input("Make another walk? y/n: ")
    if keep_running =='n':
        break

#重新绘制起点和终点
while True:
    rw = RandomWalk()
    rw.fill_walk()
    point_number = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, s=15, c=point_number, cmap=plt.cm.Blues)
    #突出起点和终点
    plt.scatter(0,0, c='green',edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    plt.show()
    keep_running = input("Make another walk? y/n: ")
    if keep_running == 'n':
        break

#隐藏坐标轴
while True:
    rw = RandomWalk()
    rw.fill_walk()
    point_number = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, s=15, c=point_number, cmap=plt.cm.Blues)
    #突出起点和终点
    plt.scatter(0,0, c='green',edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk? y/n: ")
    if keep_running == 'n':
        break

#增加点数
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    point_number = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, s=1, c=point_number, cmap=plt.cm.Blues)
    #突出起点和终点
    plt.scatter(0,0, c='green',edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk? y/n: ")
    if keep_running == 'n':
        break

#调整尺寸适合屏幕
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    #设置绘图窗口尺寸
    plt.figure(figsize=(10,6),dpi=128) #制定一个元组，单位为英寸,dpi传递系统分辨率参数
    point_number = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, s=1, c=point_number, cmap=plt.cm.Blues)
    #突出起点和终点
    plt.scatter(0,0, c='green',edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk? y/n: ")
    if keep_running == 'n':
        break



#练习
#practice 1
rw = RandomWalk()
rw.fill_walk()
plt.plot(rw.x_values,rw.y_values,linewidth=5)
plt.show()

#practice 2
rw = RandomWalk()
rw.fill_walk2()
plt.scatter(rw.x_values,rw.y_values,s=5)
plt.show()

#practice 3
rw = RandomWalk()
rw.fill_walk3()
plt.scatter(rw.x_values,rw.y_values,s=5)
plt.show()