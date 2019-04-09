def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['mario','jane','kate']
greet_users(usernames)

#在函数中修改列表，做的任何修改都是永久性的
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop(0)
    print("Printing model: " + current_design)
    completed_models.append(current_design)
print("\nThe following models have printed:")
for completed_model in completed_models:
    print(completed_model)
#编写两个函数，实现相同功能
#每个函数都应该只负责一项具体的工作
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop(0)
        print("Printing model: " + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\nThe following models have printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
print(unprinted_designs)

#禁止函数修改列表，可以向函数传递列表的副本，而不是原件
print("***********************************************")
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop(0)
        print("Printing model: " + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\nThe following models have printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
print_models(unprinted_designs[:],completed_models) #[:]创建列表的副本，但是能避免则避免，创建副本需要花时间和内存
show_completed_models(completed_models)
print(unprinted_designs)


#练习
#practice 1
magicians = ['mario','jane','kate','brioni']
def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())
show_magicians(magicians)

#practice 2
print("-------------------------")
def make_great(magicians):
    for i in range(0,len(magicians)):
        magicians[i] = 'the great ' + magicians[i]
show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)
print("-------------------------")

#practice 3
updated_magicians = [] #利用了列表对换
magicians = ['mario','jane','kate','brioni']
def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())
show_magicians(magicians)
def make_great2(magicians):
    while magicians:
        this_magician = "the great " + magicians.pop(0)
        updated_magicians.append(this_magician)
make_great2(magicians)
show_magicians(magicians)
print(magicians)
show_magicians(updated_magicians)