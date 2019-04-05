for value in range(1,5): #range()可以让你从指定的第一个值开始数，并在到达你指定的第二个值后停止，但输出不包含第二个值
    print(value) #1,2,3,4，

numbers = list(range(1,6)) #指定1-5作为list的元素
print(numbers)

even_number = list(range(2,11,2)) #range()中的第三个参数是指间隔为2（不断+2）
print(even_number) #[2, 4, 6, 8, 10]

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

squares = []
for value in range(1,11):
    squares.append(value ** 2) #不使用临时变量
print(squares)


digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))



#list解析
squares = [value**2 for value in range(1,11)] #定义list名称，指定表达式，用于生成list中的值。用for循环来提供值。
print(squares)


#练习
#practice 1
for value in range(1,21):
    print(value)

#practice 2
numbers = []
for number in range(1,1000001):
    # print(number)
    numbers.append(number)
# print(numbers)
print(min(numbers),max(numbers),sum(numbers))

#practice 3
for value in range(1,21,2):
    print(value)

#practice 4
for value in range(3,31,3):
    print(value)

#practice 4
digits = [digit**3 for digit in range(1,11)]
print(digits)
