#tuple元组，是不可变的列表，使用（）,如果需要存储的一组值在程序的整个生命周期内都不变，可使用元组
dimensions = (200,50)
print(dimensions)
print(dimensions[1]) #元组的索引和列表一样
print(dimensions[0])

dimensions = (200,50)
#dimensions[0] = 250 #返回错误，tuple不支持修改操作，所以在有些时候不允许代码修改的时候可用

#遍历tuple
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

#修改tuple变量
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

dimensions = (400,100) #给tuple的变量赋值是合法的
for dimension in dimensions:
    print(dimension)

#练习
#practice 1
buffets = ('milk','candy','rice','pork','apple')
for buffet in buffets:
    print(buffet.title())
#buffets[1] = 'orange' #报错了
buffets = ('milk','orange','beef','pork','apple')
for buffet in buffets:
    print(buffet)