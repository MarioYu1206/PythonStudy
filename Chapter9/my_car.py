from car import Car

my_new_car = Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


from car import ElectricCar2

my_tesla = ElectricCar2('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


from car import Car, ElectricCar2

my_bettle = Car('vw','bettle',2016)
print(my_bettle.get_descriptive_name())
my_tesla = ElectricCar2('tesla','roadster',2019)
print(my_tesla.get_descriptive_name())


import car
my_bettle = car.Car('vw','bettle',2016)
print(my_bettle.get_descriptive_name())
my_tesla = car.ElectricCar2('tesla','roadster',2019)
print(my_tesla.get_descriptive_name())




from car import Car
from electric_car import ElectricCar2

my_bettle = Car('vw','bettle',2016)
print(my_bettle.get_descriptive_name())
my_tesla = ElectricCar2('tesla','roadster',2019)
print(my_tesla.get_descriptive_name())


#练习
# 9-10 导入Restaurant 类 ： 将最新的Restaurant 类存储在一个模块中。 在另一个文件中， 导入Restaurant 类， 创建一个Restaurant 实例， 并调
# 用Restaurant 的一个方法， 以确认import 语句正确无误。
# 9-11 导入Admin 类 ： 以为完成练习9-8而做的工作为基础， 将User 、 Privileges 和Admin 类存储在一个模块中， 再创建一个文件， 在其中创建一个Admin 实例
# 并对其调用方法show_privileges() ， 以确认一切都能正确地运行。
# 9-12 多个模块 ： 将User 类存储在一个模块中， 并将Privileges 和Admin 类存储在另一个模块中。 再创建一个文件， 在其中创建一个Admin 实例， 并对其调用方
# 法show_privileges() ， 以确认一切都依然能够正确地运行。