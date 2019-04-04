motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati' #直接修改list里的值
print (motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati') #append()直接在末尾追加
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati') # insert()可以指定元素插入位置
print(motorcycles)
motorcycles.insert(3, 'lifan')
print(motorcycles)


#如果你要从列表中删除一个元素， 且不再以任何方式使用它， 就使用del 语句； 如果你要在删除元素后还能继续使用它， 就使用方法pop() 。
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0] # del可以删除任何位置的list元素
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motercycle = motorcycles.pop() #pop()可以删除list末尾的元素，并让你能够接着使用它，相当于弹出。
print(motorcycles)
print(popped_motercycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned + ".")


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.remove('suzuki') #remove()可以删除指定值,但是只删除第一个指定的值，如果要删除的值在列表中出此案多次，就需要使用循环来判断是否删除了所有这样的值。
print(motorcycles)

print("test")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

#练习
#practice 1
guest = ['mario','tom','jane']
print("please join my party " + guest[0].title() + "\nplease join my party " + guest[1].title() + "\nplease join my party " + guest[2].title())

#practice 2
print(guest[-1].title() + " can't join")
guest.remove(guest[-1])
print(guest)
guest.append('kate')
print(guest)

#practice 3
guest.insert(0,'a')
guest.insert(3,'b')
guest.append('c')
print(guest)

#practice 4
message0 = guest.pop()
print(message0)
#guest.pop()
print(message0 + " sorry")
print(guest)
message1 = guest.pop()
print(message1)
#guest.pop()
print(message1 + " sorry")
print(guest)
message2 = guest.pop()
print(message2)
#guest.pop()
print(message2 + " sorry")
print(guest)
message3 = guest.pop()
print(message3)
#guest.pop()
print(message3 + " sorry")
print(guest)

del guest[0]
del guest[0]
print(guest)