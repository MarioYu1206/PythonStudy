requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    print("adding " + requested_topping + ".")
print("\nfinished making your pizza!")

requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("sorry, we are out of " + requested_topping + " now.")
    else:
        print("adding " + requested_topping + ".")
print("\nfinished making your pizza!")

requested_toppings = []
if requested_toppings: #在for循环之前判断列表是否为空，在if语句中将列表名用在条件表达式中是，程序在列表为空时返回False
    for requested_topping in requested_toppings:
        print("adding " + requested_topping + ".")
    print("\nfinished making your pizza!")
else:
    print("are you sure you want a plain pizza?")

available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("adding " + requested_topping + ".")
    else:
        print("sorry, we don't have " + requested_topping + " now.")
print("\nfinished making your pizza!")

#练习
#practice 1
users = ['mario','john','tom','admin','jane']
for user in users:
    if user == 'admin':
        print("hello admin, would you like to see a status report?")
    else:
        print("hello " + user.title() + ", thank you for logging in again.")

#practice 2
users = ['mario','john','tom','admin','jane']
#users = []
if users:
    for user in users:
        if user == 'admin':
            print("hello admin, would you like to see a status report?")
        else:
            print("hello " + user.title() + ", thank you for logging in again.")
else:
    print("we need to find some users!")

#practice 3
current_users = ['mario','john','tom','tim','jane']
new_users = ['Mario','james','black','jane','sarah']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("user " + new_user + " already exists, you need to try another user")
    else:
        print("user " + new_user + " is not occupied, you can use it")

#practice 4
ordinal_numbers = [21,22,23,24,25,26,27,28,29]
for ordinal_number in ordinal_numbers:
    #print(str(ordinal_number)[-1:])
    if str(ordinal_number)[-1:] == '1':
        print(str(ordinal_number) + 'st')
    elif str(ordinal_number)[-1:] == '2':
        print(str(ordinal_number) + 'nd')
    elif str(ordinal_number)[-1:] == '3':
        print(str(ordinal_number) + 'rd')
    else:
        print(str(ordinal_number) + 'th')