car = 'audi'
print(car=='audi') #True

requested_topping = 'mushrooms'
if requested_topping != 'anchovies': # !=表示不等于
    print("Hold the anchovies!")

answer = 17
if answer !=42:
    print("That is not the correct answer, please try again!")

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21) #False
print(age_0 >= 21 or age_1 >= 21) #True

#检查特定值是否包含在列表中
requested_toppings = ['mushrooms','onions','pineapple']
print('mushrooms' in requested_toppings) #True，in表示在...内
print('apple' in requested_toppings) #False

#检查特定值是否不包含在列表中
banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users: #not in表示不在...内
    print(user.title() + ", you can post a response if you wish.")

#布尔表达式
game_active = True
can_edit = False

#练习
#practice 1
car = 'subaru'
print("is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nis car == 'audi'? I predict False.")
print(car == 'audi')

#practice 2
string0 = 'abc'
string1 = 'def'
if string0 == string1:
    print('equal')
else:
    print('not equal')