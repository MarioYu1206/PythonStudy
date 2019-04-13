#如果你要编写的类是另一个现成类的特殊版本，可以使用继承，它将自动获取另一个类的所有属性和方法，称为子类，还可以定义自己的属性和方法.
#子类的方法__init__()
class Car(): #父类，创建子类时，父类必须在当前文件中，且位于子类前面
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #给属性指定默认值
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self,mileage): #创建一个更新属性的方法
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading += miles
    def fill_gas_tank(self, fill_flag):
        print(fill_flag)



class ElectricCar(Car): #定义子类，必须在括号内指定父类的名称
    """电动汽车的独特之处"""
    def __init__(self, make, model, year): #__init__()方法接受创建Car实例所需的信息
        """初始化父类的属性"""
        super().__init__(make, model, year) #super()方法是一个特殊函数，帮助Python将父类和子类联系起来。这行代码让P樱桃红、调用ElectricCar的弗雷德方法__init__()，让ElectricCar实例包含父类的所有属性。父类也成为了超类（superclass），所以super因此得名。
        self.battery_size = 70 #给子类定义属性
    def describe_battery(self): #给子类定义方法
        print("The car has a " + str(self.battery_size) + "-kWh battery.")
    def fill_gas_tank(self): #重写父类的方法
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
# my_tesla.fill_gas_tank('no')
# my_car = Car('a','b',1)
# my_car.fill_gas_tank('yes')


#使用代码模拟实物时， 你可能会发现自己给类添加的细节越来越多： 属性和方法清单以及文件都越来越长。 在这种情况下， 可能需要将类的一部分作为一个独立的类提取出来。你可以将大型类拆分成多个协同工作的小类。
class Battery():
    """一次模拟电动车电瓶的简单尝试"""
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("The car has a " + str(self.battery_size) + "-kWh battery.")
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar2(Car): #定义子类，必须在括号内指定父类的名称
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery = Battery() #创建一个Battery的新实例，使用默认值
my_tesla2 = ElectricCar2('tesla','model s',2018)
print(my_tesla2.get_descriptive_name())
# my_tesla2.battery.battery_size = 85
my_tesla2.battery.describe_battery()
my_tesla2.battery.get_range()



#练习
#practice 1
class Restaurant():
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("The restaurant " + self.restaurant_name.title() + " is cooking " + self.cuisine_type)
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open!")

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name, cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['apple','banana','orange']
IceCreamStand_Mario = IceCreamStand('IceCreamStand_Mario','Ice Cream')
print("We have: ")
for flavor in IceCreamStand_Mario.flavors:
    print("\t" + flavor)

#practice 2
class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title())
    def greet_user(self):
        print("Hello, " + self.first_name.title() + " " + self.last_name.title())
    def increment_login_attempts(self,incr_attempts):
        self.login_attempts += incr_attempts
    def reset_login_attempts(self,initial_attempt):
        self.login_attempts = initial_attempt

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges = ["can add post","can delete post","can ban user"]
    def show_privileges(self):
        for privilege in self.privileges:
            print("\t" + privilege)
admin1 = Admin('Mario','Yu')
print("you are admin, you")
admin1.show_privileges()

#practice 3
class Privileges():
    def __init__(self,privileges):
        self.privileges = privileges
    def show_privileges2(self):
        for privilege in self.privileges:
            print("\t" + privilege)
class Admin2(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges = Privileges(privileges=['add user'])
admin2 = Admin2('Shanshan','Liu')
# admin2.privileges.privileges = input()["can add post","can delete post"]
print("you are admin, you")
admin2.privileges.show_privileges2()

#practice 4
class Battery2():
    """一次模拟电动车电瓶的简单尝试"""
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("The car has a " + str(self.battery_size) + "-kWh battery.")
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    def upate_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar3(Car): #定义子类，必须在括号内指定父类的名称
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery = Battery2()

my_car3 = ElectricCar3('vw','langyi',2019)
my_car3.battery.get_range()
my_car3.battery.upate_battery()
my_car3.battery.get_range()