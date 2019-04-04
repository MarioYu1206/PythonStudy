cars = ['bmw','audi','toyota','subaru']
cars.sort() # sort()进行排序，对列表的修改时永久性的
print(cars)

cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True) # reverse=True代表倒序
print(cars)

cars = ['bmw','audi','toyota','subaru']
print("here is the original list:")
print(cars)
print("here is the sorted list:")
print(sorted(cars)) #sorted()也可以进行排序，但是不会改变列表元素的顺序
print("here is the original list again:")
print(cars)
print(sorted(cars,reverse=True))



cars = ['bmw','audi','toyota','subaru']
print(cars)
cars.reverse() #reverse()可以反转排列列表元素，是反转元素的顺序，不是字母顺序，是永久性的修改。
print(cars)


cars = ['bmw','audi','toyota','subaru']
print(len(cars)) #len()获取列表长度。


#练习
#practice 1
tour = ['beijing','shanghai','shenzhen','guangzhou','xizang']
print(tour)
print(sorted(tour))
print(tour)
print(sorted(tour,reverse=True))
print(tour)
tour.reverse()
print(tour)
tour.reverse()
print(tour)
tour.sort()
print(tour)
tour.sort(reverse=True)
print(tour)


#practice 2
print(len(tour))

#practice 3
