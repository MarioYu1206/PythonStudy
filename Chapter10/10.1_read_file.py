#读取整个文件
#要使用文件里的内容，必须先打开它，才能访问它。open()函数使用后表示返回一个文件的对象
#with关键字在不再需要访问文件后将其关闭。也可以使用close()来关闭，但是一旦存在问题，可能导致文件未被关闭，之后造成文件被修改
with open('E:\Python_Projects\crash_course\pcc-master\chapter_10\pi_digits.txt') as file_object:
    contents = file_object.read() #read()函数读取全部数据
    print(contents) #尾部会多出一个空行，read()到达文件末尾是返回一个空字符串
    print(contents.rstrip())
    print("--------------")

#文件路径
file_path = "E:\Python_Projects\crash_course\pcc-master\chapter_10\pi_digits.txt"
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
    print("--------------")

#逐行读取
filename = "E:\Python_Projects\crash_course\pcc-master\chapter_10\pi_digits.txt"
with open(filename) as file_object:
    for line in file_object: #用for遍历每一行
        print(line.rstrip())
    print("--------------")

#创建一个包含文件各行内容的列表
#使用关键字with 时， open() 返回的文件对象只在with 代码块内可用。 如果要在with 代码块外访问文件的内容， 可在with 代码块内将文件的各行存储在一个列表中， 并在with 代码块外使用该列表： 你可以立即处理文件的各个部分， 也可推迟到程序后面再处理。
filename = "E:\Python_Projects\crash_course\pcc-master\chapter_10\pi_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines() #realines()是读取每所有行，存在一个列表中
    print(lines)
for line in lines:
    print(line.rstrip())

#使用文件内容
filename = "E:\Python_Projects\crash_course\pcc-master\chapter_10\pi_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))
#读取文本文件时， Python将其中的所有文本都解读为字符串。 如果你读取的是数字， 并要将其作为数值使用， 就必须使用函数int() 将其转换为整数， 或使用函数float() 将其转换为浮点数。

#包含一百万位的大型文件
filename = "E:\Python_Projects\crash_course\pcc-master\chapter_10\pi_million_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string[:52] + '...')
print(len(pi_string)) #Python可以处理任意数据量，只要系统内存足够

#圆周率值中包含你的生日吗
filename = "E:\Python_Projects\crash_course\pcc-master\chapter_10\pi_million_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")


#练习
#practice 1
filename = "E:\Python_Projects\crash_course\\files\chapter10_1_1.txt"
with open(filename) as file_object:
    all_file = file_object.read()
    print(all_file.strip())
    print("----------")

    for line in file_object:
        print(line.strip())
    print("----------")

    lines = file_object.readlines()
i = 0
while i < 3:
    print(lines)
    i += 1

#practice 2
message = "I really like dogs."
message = message.replace("dog","cat") #replace()可以替换字符串
print(message)