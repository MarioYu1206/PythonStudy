#写入空文件
#第一个实参也是要打开的文件的名称； 第二个实参（'w' ） 告诉Python， 我们要以写入模式 打开这个文件。
#可指定读取模式 （'r' ） 、 写入模式 （'w' ） 、 附加模式 （'a' ） 或让你能够读取和写入文件的模式（'r+' ） 。 如果你省略了模式实参， Python将以默认的只读模式打开文件。
#以写入（'w' ） 模式打开文件时千万要小心， 因为如果指定的文件已经存在， Python将在返回文件对象前清空该文件。
file_path = "E:\Python_Projects\crash_course\pcc-master\chapter_10\programming.txt"
with open(file_path, 'w') as file_object:
    file_object.write("I love programming.")

#写入多行
filename = "E:\Python_Projects\crash_course\pcc-master\chapter_10\programming.txt"
with open(filename,'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

#附加到文件
filename = "E:\Python_Projects\crash_course\pcc-master\chapter_10\programming.txt"
with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")


#练习
#practice 1
name = input("please input your name: ")
filename = "E:\Python_Projects\crash_course\\files\chapter10_2_1.txt"
with open(filename, 'w') as file_object:
    file_object.write(name + "\n")

#practice 2
filename = "E:\Python_Projects\crash_course\\files\chapter10_2_2.txt"
while True:
    name = input("please input your name: ")
    if name == 'q':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(name + "\n")

#practice 3
#similar with practice 2