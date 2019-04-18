#分析csv文件头
import csv
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) #只调用一次，返回第一行
    print(header_row)

#打印文件头及其位置
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)

#提取并读取数据
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)
    print(highs)

#绘制气温图表
from matplotlib import pyplot as plt
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(highs,c='red')
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()

#模块datetime
from datetime import datetime
first_date = datetime.strptime('2014-7-1','%Y-%m-%d') #strptime()方法接受实参，决定如何解读日期
print(first_date)

#在图表中添加日期
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0],'%Y-%m-%d')
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
    print(highs)
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates,highs,c='red')
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() #绘制斜的日期
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()