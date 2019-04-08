#for循环用于针对集合中的每个元素都一个代码块，二while循环不断地运行，直到制定的条件不满足为止
current_number = 1 #设置初始值，从1开始
while current_number <= 5: #while循环指定小于或者等于5就一直执行
    print(current_number)
    current_number += 1 #每次执行完自行+1

#让用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = "" #变量初始值设置为空字符串
while message != 'quit':
    message = input(prompt)
    if message != 'quit': #加入这个if判断，可以不打印'quit'
        print(message)


#使用标志
#在要求很多条件都满足才继续运行的程序中，可以定义一个变量，用于判断整个程序是否处于活动状态，这个变量就是标志。
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False #触发条件时，将active更新为False
    else:
        print(message)


#使用break退出循环
#break语句用于控制程序流程，可使用他来控制那些代码行将执行
prompt = "\nplease enter the name of a city you have visited: "
prompt += "\n(enter 'quit' when you are finished.)"
while True:
    city = input(prompt)
    if city == 'quit':
        break #遇到break语句，退出整个循环
    else:
        print("I'd live to go to " + city.title() + "!")


#在循环中使用continue
#要返回到循环开头，并根据条件测试结果决定是否继续执行循环，可使用continue语句
current_number = 0
while current_number <10:
    current_number += 1
    if current_number % 2 ==0:
        continue #continue不是继续下面的步骤，而是返回到循环开头，不是退出整个循环，比如这个结果打印的时1,3,5,7,9
    print(current_number)


#避免无限循环
x = 1
while x < 5:
    print(x)
    x += 1 #如果遗漏了这行代码，程序将不断打印1，无限循环


#练习
#practice 1
topping = "what topping would you like? "
topping += "\nplease input 'quit' to stop. "
while True:
    toppings = input(topping)
    if toppings == 'quit':
        break
    else:
        print("we will add " + toppings + " on your pizza.")

#practice 2
prompt = "how old are you? "
while True:
    age = input(prompt)
    if age == 'quit':
        break
    elif int(age) < 3:
        print("you are free!")
    elif int(age) >=3 and int(age) < 12:
        print("you need to pay $10.")
    else:
        print("you need to pay $15.")

#practice 3
prompt = "how old are you? "
active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    elif int(age) < 3:
        print("you are free!")
    elif int(age) >=3 and int(age) < 12:
        print("you need to pay $10.")
    else:
        print("you need to pay $15.")

#practice 4
# x = 1
# while x < 2:
#     print(x)
