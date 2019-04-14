#使用json.dump()和json.load()
import json

numbers = [2,3,5,7,11,13]
filename = "E:\Python_Projects\crash_course\\files\\number.json"
with open(filename, 'w') as f_obj:
    json.dump(numbers,f_obj) #dump()将numbers存储到文件

with open(filename) as f_obj:
    numbers = json.load(f_obj) #load()文件中的信息
print(numbers)

#保存和读取用户生成的数据
username = input("what is your name? ")
filename = "E:\Python_Projects\crash_course\\files\\username.json"
with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print("We'll remember you when you come back, " + username + "!")

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")

filename = "E:\Python_Projects\crash_course\\files\\username.json"
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("what is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")

#重构
import json

def greet_user():
    filename = "E:\Python_Projects\crash_course\\files\\username.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("what is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")
greet_user()

#开始拆分greet_user()
import json
def get_stored_username():
    filename = "E:\Python_Projects\crash_course\\files\\username.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("what is your name? ")
    filename = "E:\Python_Projects\crash_course\\files\\username.json"
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")
greet_user()



#练习
#practice 1
import json
numbers = input("please input your lucky number: ")
filename = "E:\Python_Projects\crash_course\\files\\luckynumber.json"
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)
with open(filename) as f_obj:
    lucky_number = json.load(f_obj)
    print("I know your lucky number is " + lucky_number)

#practice 2
import json
def get_stored_ln():
    filename = "E:\Python_Projects\crash_course\\files\\luckynumber.json"
    try:
        with open(filename) as f_obj:
            lucky_number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return lucky_number

def get_new_ln():
    lucky_number = input("please input your lucky number: ")
    filename = "E:\Python_Projects\crash_course\\files\\luckynumber.json"
    with open(filename, 'w') as f_obj:
        json.dump(lucky_number, f_obj)
    return lucky_number

def know_ln():
    lucky_number = get_stored_ln()
    if lucky_number:
        print("I know your lucky number is " + lucky_number)
    else:
        lucky_number = get_new_ln()
        print("I will know your lucky number is " + lucky_number)
know_ln()

#practice 3
import json
def get_stored_username():
    filename = "E:\Python_Projects\crash_course\\files\\username.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("what is your name? ")
    filename = "E:\Python_Projects\crash_course\\files\\username.json"
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        check = input("are you " + username + "? y/n")
        if check == 'y':
            print("Welcome back, " + username + "!")
        if check == 'n':
            print("I am sorry.")
            username = get_new_username()
            print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")
greet_user()