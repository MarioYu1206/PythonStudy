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

#涵盖更长的时间
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) #只调用一次，返回第一行
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates,highs,c='red')
plt.title("Daily high temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() #绘制斜的日期
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()

#再绘制一个数据系列
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) #只调用一次，返回第一行
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
        low = int(row[3])
        lows.append(low)
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates,highs,c='red')
plt.plot(dates,lows,c='blue') #需要两次plot
plt.title("Daily high & low temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() #绘制斜的日期
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()

#给图表区域着色
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) #只调用一次，返回第一行
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
        low = int(row[3])
        lows.append(low)
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5) #alpha指定颜色透明度
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1) #fill_between为区域着色
plt.title("Daily high & low temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() #绘制斜的日期
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()

#错误检查
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # 只调用一次，返回第一行
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else:
            highs.append(high)
            dates.append(current_date)
            lows.append(low)
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)  # alpha指定颜色透明度
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)  # fill_between为区域着色
plt.title("Daily high & low temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()  # 绘制斜的日期
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()


#练习
#practice 2
import csv
from matplotlib import pyplot as plt
from datetime import datetime
filename1 = 'death_valley_2014.csv'
filename2 = 'sitka_weather_2014.csv'
with open(filename1) as f1:
    reader1 = csv.reader(f1)
    header_row1 = next(reader1)  # 只调用一次，返回第一行
    dates1, highs1, lows1 = [], [], []
    for row in reader1:
        try:
            current_date1 = datetime.strptime(row[0], '%Y-%m-%d')
            high1 = int(row[1])
            low1 = int(row[3])
        except ValueError:
            print(current_date1,'missing data')
        else:
            highs1.append(high1)
            dates1.append(current_date1)
            lows1.append(low1)
with open(filename2) as f2:
    reader2 = csv.reader(f2)
    header_row2 = next(reader2)  # 只调用一次，返回第一行
    dates2, highs2, lows2 = [], [], []
    for row in reader2:
        try:
            current_date2 = datetime.strptime(row[0], '%Y-%m-%d')
            high2 = int(row[1])
            low2 = int(row[3])
        except ValueError:
            print(current_date2,'missing data')
        else:
            highs2.append(high2)
            dates2.append(current_date2)
            lows2.append(low2)
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates1, highs1, c='red', alpha=0.5)
plt.plot(dates1, lows1, c='blue', alpha=0.5)  # alpha指定颜色透明度
plt.fill_between(dates1, highs1, lows1, facecolor='blue', alpha=0.1)  # fill_between为区域着色
plt.plot(dates2, highs2, c='red', alpha=0.5)
plt.plot(dates2, lows2, c='blue', alpha=0.5)  # alpha指定颜色透明度
plt.fill_between(dates2, highs2, lows2, facecolor='blue', alpha=0.1)
plt.title("Daily high & low temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()  # 绘制斜的日期
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()

