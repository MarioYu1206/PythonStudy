#2.3.1 使用方法修改字符串的大小写
name = "ada lovelace"
print(name.title()) # "Ada Lovelace", title() 以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写。

name1 = "ADA LOVELACE"
print(name1.title()) # "Ada Lovelace"

print(name.title().upper()) #upper()是大写
print(name1.lower()) #lower()是小写, 存储数据时，方法lower() 很有用。很多时候，你无法依靠用户来提供正确的大小写，因此需要将字符串先转换为小写，再存储它们。以后需要显示这些信息时，再将其转换为最合适的大小写方式。


#2.3.2 合并（拼接）字符串
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name #Python使用加号（+ ）来合并字符串。
print(full_name)
print("Hello, " + full_name.title() + "!")
message = "Hello, " + full_name.title() + "!"
print(message)


#2.3.3 使用制表符或换行符来添加空白
'''
在编程中，空白 泛指任何非打印字符，如空格、制表符和换行符。你可使用空白来组织输出，以使其更易读。
'''
print("Python")
print("\tPython") #\t制表符

print("Languages:\nPython\nC\nJavaScript") #\n换行符
print("Languages:\n\tPython\n\tC\n\tJavaScript")


#2.3.4 删除空白
favorite_language = "python "
print(favorite_language)
print(favorite_language.rstrip()) #要确保字符串末尾没有空白，可使用方法rstrip() 。

favorite_language = favorite_language.rstrip() #在编程中，经常需要修改变量的值，再将新值存回到原来的变量中。这就是变量的值可能随程序的运行或用户输入数据而发生变化的原因。
print(favorite_language)

favorite_language = " python "
print(favorite_language.rstrip()) #rstrip()末尾去除空格
print(favorite_language.lstrip()) #lstrip()开头去除空格
print(favorite_language.strip()) #strip()两端都去除空格


#2.3.5 使用字符串时避免语法错误
message = "One of Python's strengths is its diverse community."
print(message)


#练习
#practice 1
user_name = "Mario"
message = "Hello " + user_name + ", would you like to learn some Python today?"
print(message)
#practice 2
user_name = "Mario"
print(user_name.title())
print(user_name.lower())
print(user_name.upper())

#practice 3
famous_people = "周恩来"
quote = "为中华之崛起而读书"
message = famous_people + "曾经说过：" + '"' + quote + '!"'
print(message)

#practice 4
name = " My name is: \nMario\tYu "
print(name.strip())