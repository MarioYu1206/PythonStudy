#传递任意数量的实参
def make_pizza(*toppings): #*星号让Python穿件一个名为toppings的空元组，并将收到的所有值都封装到这个元组中。
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

#结合使用位置实参和任意数量实参
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms','green peppers','extra cheese')

#使用任意数量的关键字实参
def build_profile(first, last, **user_info): #**两个星号让Python创建一个名为user_info的孔子点，并将收到的所有名称-值对都封装到这个字典中。
    profile ={}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value.title()
    return profile
user_profile = build_profile('albert','einstein',
                             location='princeton',
                             field='physics')
print(user_profile)


#练习
#practice 1
def add_materials(*materials):
    print(materials)
add_materials('potato')
add_materials('potato','onion')
add_materials('a','b','c')

#practice 2
def build_profile(first, last, **user_info):
    profile ={}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value.title()
    return profile
user_profile = build_profile('mario','yu',
                             location='dalian',
                             field='business intelligence',
                             age=str(31))
print(user_profile)

#practice 3
def make_car(manufactor,model,**other_info):
    car_info = {}
    car_info['manufactor'] = manufactor
    car_info['model'] = model
    for key, value in other_info.items():
        car_info[key] = value
    return car_info
car = make_car('subaru','outback',color='blue',tow_package=True)
print(car)