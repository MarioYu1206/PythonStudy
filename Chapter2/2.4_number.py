#2.4.1 整数
result = 3 ** 2 #Python使用两个乘号表示乘方运算
print(result) #9

result = 2 + 3 * 4 # Python还支持运算次序，因此你可在同一个表达式中使用多种运算。
print(result)


#2.4.2 浮点数
#Python将带小数点的数字都称为浮点数
result = 0.2 + 0.1 #结果包含的小数位数可能是不确定的
print(result) # 0.30000000000000004


#2.4.3 使用函数str() 避免类型错误
age = 23
message = "Happy " + str(age) + "rd Birthday" #字符串必须拼接字符串，用str()来做类型转换
print(message)


#练习
#practice 1
a = 5 + 3
b = 9 - 1
c = 2 * 4
d = 16 / 2
print(a,b,c,int(d))

#practice 2
favorite_number = 7
message = "my favorite number is " + str(favorite_number)
print(favorite_number)