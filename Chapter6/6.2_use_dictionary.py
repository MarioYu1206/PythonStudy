#字典是一系列键值对，用{}来括起来。通过使用键来访问与之相关的值，python中的任何对象都可以作为字典的值
alien_0 = {'color':'green','points':5}
new_points = alien_0['points'] #用字典中的键来找到相应的值，为变量赋值
print("you just earned " + str(new_points) + " points!")
