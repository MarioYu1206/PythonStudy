#位置实参，这要求实参的顺序与形参的顺序相同
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet('harry', 'hamster')

#关键字实参时传递给函数的名称-值对，就无须考虑顺序了
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry')

#默认值，编写函数时，给每个形参指定默认值
def describe_pet(pet_name, animal_type='dog'): #给定默认值的形参只能放在后面，而在调用时只能把将来要传值的参数放到前面
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')
describe_pet('willie')
describe_pet(animal_type='hamster', pet_name='harry')

#等效的函数调用
def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('willie')
describe_pet(pet_name='willie')
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

#避免实参错误
def describe_pet(pet_name, animal_type):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#describe_pet() #必须传递两个参数


#练习
#practice 1
def make_shirt(size, logo):
    print("\nthe size is " + str(size) + ", the logo is " + logo + ".")
make_shirt(36,'mario')

#practice 2
def make_shirt(size, logo='I love Python'):
    print("\nthe size is " + size + ", the logo is " + logo + ".")
make_shirt('medium')
make_shirt('large','here it is')

#practice 3
def describe_city(city, country='China'):
    print(city + " is in " + country)
describe_city('dalian')
describe_city(city='beijing')
describe_city('tokyo','Japan')