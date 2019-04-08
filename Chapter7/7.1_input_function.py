#input()函数让程序暂停运行，让用户输入一些文本,接受一个参数
message = input("tell me something, and I will repeat it back to you:")
print("\n" + message)

name = input("please enter your name: ")
print("Hello, " + name + ".")

prompt = "if you tell us who you are, we can personlize the message you see."
prompt += "\nWhat is your first name? " #运算符+=再存储在prompt中的字符串末尾附加一个字符串
name = input(prompt)
print("\nHello, " + name + ".")


#使用int()来获取数值输入
age = input("How old are you? ")
print(age) #这里面返回的是字符串，而不是数字
print(int(age) >= 18) #需要用int()函数来转换类型

height = input("how tall are you in inches? ")
height = int(height)
if height >= 36:
    print("\nyou are tall enought to ride!")
else:
    print("\nyou will be able to ride when you are a little older.")


#求模运算符
print(4%3)
print(6%3)

number = input("Enter a number, and I will tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nthe number " + str(number) + " is even.")
else:
    print("\nthe number " + str(number) + " is odd.")


#练习
#practice 1
car = input("what car would you like? ")
print("Let me see if I can find you a " + car + ".")

#practice 2
consumer_count = input("how many people will have the meal? ")
consumer_count = int(consumer_count)
if consumer_count > 8:
    print("Sorry, there is no more position.")
else:
    print("there is position.")

#practice 3
number = input("please input a number: ")
number = int(number)
if number % 10 == 0:
    print("the number " + str(number) + " is divisible by 10.")
else:
    print("the number " + str(number) + " is NOT divisible by 10.")