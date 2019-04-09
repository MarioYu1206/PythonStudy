#函数时带名字的代码块
def greet_user():
    print("hello!")
greet_user()

def greet_user(username): #定义参数，此处的username是个形参
    print("hello, " + username.title() + "!")
greet_user('jesse') #输入参数，此处的jesse是个实参


#练习
#practice 1
def display_message():
    print("I have learned function defination.")
display_message()

#practice 2
def favorite_book(title):
    print("one of my favorite books is " + title + ".")
favorite_book('Alice in Wonderland')