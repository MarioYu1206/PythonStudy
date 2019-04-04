bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0].title()) # 列表索引从0开始
print(bicycles[3])
print(bicycles[-1], bicycles[-3]) # 索引-1代表列表最后一个元素,-3代表倒数第三个元素

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

#练习
names = ['mario','tom','susan','chris','james']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[-2].title())
print(names[-1].title())
message0 = "How are you doing, " + names[0].title() + "?"
message1 = "How are you doing, " + names[1].title() + "?"
message2 = "How are you doing, " + names[2].title() + "?"
message3 = "How are you doing, " + names[3].title() + "?"
message4 = "How are you doing, " + names[4].title() + "?"
print(message0+ '\n' + message1 + '\n' + message2 + '\n' + message3 + '\n' + message4)
