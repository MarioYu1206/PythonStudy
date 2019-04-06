#字典是一系列键值对，用{}来括起来。通过使用键来访问与之相关的值，python中的任何对象都可以作为字典的值
alien_0 = {'color':'green','points':5}
new_points = alien_0['points'] #用字典中的键来找到相应的值，为变量赋值
print("you just earned " + str(new_points) + " points!")

#添加键值对
alien_0 = {'color':'green','points':5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0) #直接定义添加，键值对和键值对之间没有顺序可言

#使用字典来存储用户提供的数据或在编写能自动生成大量键值对的代码时，通常都需要先定义一个空字典
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25

#修改字典中的值
alien_0 = {'color':'green'}
print("the alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow' #更新相应键的值
print("the alien is now " + alien_0['color'] + ".")


#对一个能够以不同速度移动的外星人的位置进行追踪
alien_0 = {'x_position': 0, 'y_position': 25, 'speed':'medium'}
print("original x-position: " + str(alien_0['x_position']))
#向右移动外星人
#具外星人当前速度决定其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #这个外星人的速度一定很快
    x_increment = 3
#新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("new x-position: " + str(alien_0['x_position']))


#删除键值对
alien_0 = {'color':'green','points':5}
print(alien_0)
del alien_0['points'] #del删除键值对
print(alien_0)

#由类似对象组成的字典
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python', #在最后一个键值对后面也加上逗号，为以后再下一行添加键值对做好准备,这个都好不会报错
    }
print(favorite_languages)
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")


#练习
#practice 1
jane = {
    'first_name':'Shanshan',
    'last_name':'Liu',
    'age':31,
    'city':'Dalian',
    }
print(jane['first_name'])
print(jane['last_name'])
print(jane['age'])
print(jane['city'])

#practice 2
lucky_numbers = {
    'mario':7,
    'jane':8,
    'tom':9,
    'jack':3,
    'kate':1,
    }
print("mario's lucky number is " + str(lucky_numbers['mario']))
print("jane's lucky number is " + str(lucky_numbers['jane']))
print("tom's lucky number is " + str(lucky_numbers['tom']))
print("jack's lucky number is " + str(lucky_numbers['jack']))
print("kate's lucky number is " + str(lucky_numbers['kate']))

#practice 3
vocabularies = {
    'for':"遍历循环",
    'test':"测试",
}
print("for的含义是：" + "\n\t" + vocabularies['for'])
print("test的含义是：" + "\n\t" + vocabularies['test'])