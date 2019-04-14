#处理ZeroDivisionError 异常
try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by zero!")

#使用异常避免崩溃，使用else代码块
#try-except-else 代码块的工作原理大致如下： Python尝试执行try 代码块中的代码； 只有可能引发异常的代码才需要放在try 语句中。 有时候， 有一些仅在try 代码块成功执行时才需要运行的代码； 这些代码应放在else 代码块中。 except 代码块告诉Python， 如果它尝试运行try 代码块中的代码时引发了指定的异常， 该怎么办。
print("give me 2 numbers, and I'll divide them.")
print("enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("you can't divide by zero!")
    else:
        print(answer)

#处理FileNotFoundError 异常
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

#分析文本
title = "Alice in Wonderland"
print(title.split()) #split()方法以空格为分隔符将字符串分拆成多个部分，并存到一个列表中

filename = "E:\Python_Projects\crash_course\pcc-master\chapter_10\\alice.txt"
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")

#使用多个文件
def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")
filename = "E:\Python_Projects\crash_course\pcc-master\chapter_10\\alice.txt"
count_words(filename)

filenames = [
    "E:\Python_Projects\crash_course\pcc-master\chapter_10\\alice.txt",
    "E:\Python_Projects\crash_course\pcc-master\chapter_10\siddharth.txt",
    "E:\Python_Projects\crash_course\pcc-master\chapter_10\moby_dick.txt",
    "E:\Python_Projects\crash_course\pcc-master\chapter_10\little_women.txt",
    ]
for filename in filenames:
    count_words(filename)

#失败时一声不吭
def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass #pass语句直接略过
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")
filenames = [
    "E:\Python_Projects\crash_course\pcc-master\chapter_10\\alice.txt",
    "E:\Python_Projects\crash_course\pcc-master\chapter_10\siddharth.txt",
    "E:\Python_Projects\crash_course\pcc-master\chapter_10\moby_dick.txt",
    "E:\Python_Projects\crash_course\pcc-master\chapter_10\little_women.txt",
    ]
for filename in filenames:
    count_words(filename)


#练习
#practice 1
print("give me 2 numbers, and I'll add them.")
print("enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    else:
        try:
            first_number = int(first_number)
        except ValueError:
            print("you need to input a number!")
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    else:
        try:
            second_number = int(second_number)
        except ValueError:
            print("you need to input a number!")
    try:
        answer = first_number + second_number
    except TypeError:
        print("you need to input both numbers!")
    else:
        print(answer)

#practice 2
#similar with practice 1

#practice 3
filename1 = "E:\Python_Projects\crash_course\\files\cats.txt"
filename2 = "E:\Python_Projects\crash_course\\files\dogs.txt"
try:
    with open(filename1) as f_obj1:
        contents = f_obj1.read()
        print(contents)
except FileNotFoundError:
    print("file not found: " + filename1)
try:
    with open(filename2) as f_obj2:
        contents = f_obj2.read()
        print(contents)
except FileNotFoundError:
    print("file not found: " + filename2)

#practice 4
filename1 = "E:\Python_Projects\crash_course\\files\cats.txt"
filename2 = "E:\Python_Projects\crash_course\\files\dogs.txt"
try:
    with open(filename1) as f_obj1:
        contents = f_obj1.read()
        print(contents)
except FileNotFoundError:
    pass
try:
    with open(filename2) as f_obj2:
        contents = f_obj2.read()
        print(contents)
except FileNotFoundError:
    pass

#practice 5
filename = "E:\Python_Projects\crash_course\pcc-master\chapter_10\\alice.txt"
with open(filename) as f_obj:
    contents = f_obj.read()
line = contents.split()
print(line)
count_alice = line.count("Alice")
print(count_alice)
line2 = [item.lower() for item in line]
count_alice2 = line2.count("alice")
print(count_alice2)