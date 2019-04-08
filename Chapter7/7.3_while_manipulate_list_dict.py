#要在遍历列表是对其进行修改，可使用while循环。

#在列表之间移动元素
unconfirmed_users = ['alice','brian','candace','mario']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop() #使用pop()方法每次从列表末尾删除一个元素
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
print("\nthe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
print(unconfirmed_users) #[]，最后变成了空列表

#删除包含特定值的所有列表元素
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#使用用户输入来填充字典
responses = {}
polling_active = True
while polling_active:
    name = input("\nwhat is your name? ")
    response = input("which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
print("\n=== Poll Results ===")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")


#练习
#practice 1
sandwich_orders = ['sandwich1','sandwich2','sandwich3','sandwich4','sandwich5']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0) #每次弹出第一个元素
    print("I made your " + current_sandwich)
    finished_sandwiches.append(current_sandwich)
print("all sandwiches are finished:")
for sandwich in finished_sandwiches:
    print(sandwich)

#practice 2
sandwich_orders = ['sandwich1','sandwich1','sandwich3','sandwich1','sandwich5']
finished_sandwiches = []
print("sandwich1 is sold out.")
while 'sandwich1' in sandwich_orders:
    sandwich_orders.remove('sandwich1')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0) #每次弹出第一个元素
    print("I made your " + current_sandwich)
    finished_sandwiches.append(current_sandwich)
print("all sandwiches are finished:")
for sandwich in finished_sandwiches:
    print(sandwich)

#practice 3
places_polls ={}
active = True
while active:
    user = input("what is your name? ")
    place = input("if you could visit one place in the world, where would you go? ")
    places_polls[user] = place

    repeat = input("find another person for the poll? yes/no? ")
    if repeat =='no':
        active = False
print("-----results-----")
for user, place in places_polls.items():
    print(user + " would like to visit " + place)