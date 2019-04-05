magicians = ['alice','david','carolina']
for magician in magicians: #for循环遍历list, magician是个变量,建议变量名和list名称相似，比较有意义，通常list名称为复数，变量名称为单数
    print(magician)

magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")