age = 19
if age >= 18:
    print("you are old enough to vote!")
    print("have you registered to vote yet?")

age = 17
if age >= 18:
    print("you are old enough to vote!")
    print("have you registered to vote yet?")
else:
    print("sorry, you are too young to vote.")
    print("please register to vote as soon as you turn 18!")

age = 12
if age < 4:
    print("your admission cost is $0.")
elif age < 18:
    print("your admission cost is $5.")
else:
    print("your admission cost is $10.")

age =12
if age < 4:
    price = 0
elif age <18:
    price = 5
else:
    price = 10
print("your admission cost is $" + str(price) + ".")

age =70
if age < 4:
    price = 0
elif age <18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 3
print("your admission cost is $" + str(price) + ".")

age =70
if age < 4:
    price = 0
elif age <18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 3
print("your admission cost is $" + str(price) + ".")

requested_toppings = ['mushrooms','extra cheese']
if  'mushrooms' in requested_toppings:
    print("adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("adding extra cheese.")
print("\nFinished making your pizza!")

requested_toppings = ['mushrooms','extra cheese']
if  'mushrooms' in requested_toppings:
    print("adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("adding extra cheese.")
print("\nFinished making your pizza!") #adding mushrooms. Finished making your pizza!如果使用了elif，程序只检查第一个mushrooms，通过了，就不检查后面的了，所以只会输出第一个条件。

#练习
#practice 1
alien_color = 'yellow'
if alien_color == 'green':
    print("you got 5 points")
else:
    print("you got 10 points")

#practice 2
alien_color = 'yellow'
if alien_color == 'green':
    print("you got 5 points")
if alien_color != 'green':
    print("you got 10 points")

#practice 3
alien_color = 'red'
if alien_color == 'green':
    print("you got 5 points")
if alien_color == 'yellow':
    print("you got 10 points")
if alien_color == 'red':
    print("you got 15 points")

alien_color = 'red'
if alien_color == 'green':
    print("you got 5 points")
elif alien_color == 'yellow':
    print("you got 10 points")
else:
    print("you got 15 points")

alien_color = 'red'
if alien_color == 'green':
    print("you got 5 points")
elif alien_color == 'yellow':
    print("you got 10 points")
elif alien_color == 'red':
    print("you got 15 points")

#practice 4
age = 1
if age < 2:
    print("baby")
elif age < 4:
    print("learn to walk")
elif age < 13:
    print("child")
elif age < 20:
    print("youth")
elif age < 65:
    print("adult")
else:
    print("aged")

#practice 5
favorite_fruits  = ['apple','orange','banana']
if 'pineapple' in favorite_fruits:
    print("you really like pineapple")
if 'banana' in favorite_fruits:
    print("you really like banana")