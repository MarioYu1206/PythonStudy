#创建Die类
from random import randint
class Die():
    def __init__(self,num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1,self.num_sides) #取随机数

#掷骰子
die = Die()
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
print(results)

#分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

#绘制直方图
import pygal
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6',frequencies) #我们使用add() 将一系列值添加到图表中（向它传递要给添加的值指定的标签， 还有一个列表， 其中包含将出现在图表中的值） 。
hist.render_to_file('die_visual.svg')