players = ['charles','martina','michael','florence','eli']
print(players[0:3]) #['charles', 'martina', 'michael']，players[0:3],其中0是起始索引（包含），3是终止索引（不包含）
print(players[1:4]) #['martina', 'michael', 'florence']
print(players[:4]) #['charles', 'martina', 'michael', 'florence'],没有指定起始索引，默认从头开始
print(players[2:]) #['michael', 'florence', 'eli'],没有指定终止索引，默认到末尾
print(players[-3:]) #['michael', 'florence', 'eli'],负索引-3返回最后3个元素

players = ['charles','martina','michael','florence','eli']
for player in players[:3]: #遍历切片
    print(player.title())

#复制列表
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:] #创建一个不指定起始和终止索引的切片，就相当于复制了list
print(my_foods)
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)


my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods #如果直接将my_foods赋给friend_foods，就不能得到两个列表，其实都指向一个列表
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)


#练习
#practice 1
items = [1,2,3,4,5,6,7,8,9]
print("the first 3 items in the list are: " + str(items[:3]))
print("the middle 3 items in the list are: " + str(items[3:6]))
print("the first 3 items in the list are: " + str(items[6:]))

#practice 2
pizzas = ['tomato','cheese','seafood']
friend_pizzas = pizzas[:]
pizzas.append('apple')
friend_pizzas.append('orange')
print(pizzas)
for pizza in pizzas:
    print(pizza)
print(friend_pizzas)
for friend_pizza in friend_pizzas:
    print(friend_pizza)

#practice 3
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
for food in my_foods:
    print(food)
    for food1 in friend_foods: #这个写的毫无意义，哈哈！
        print(food1)