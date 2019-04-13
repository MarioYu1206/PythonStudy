class Car():
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
my_new_car = Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 23 #可以修改属性的值
my_new_car.read_odometer()
my_new_car.update_odometer(30)
my_new_car.read_odometer()
my_new_car.update_odometer(35)
my_new_car.read_odometer()
my_new_car.update_odometer(5)
my_new_car.read_odometer()

my_used_car = Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()


#练习
#practice 1
class Restaurant():
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_saved = 0
    def describe_restaurant(self):
        print("The restaurant " + self.restaurant_name.title() + " is cooking " + self.cuisine_type)
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open!")
    def set_number_served(self, number):
        self.number_saved = number
    def increment_number_served(self,incr_number):
        self.number_saved += incr_number
restaurant = Restaurant("Mario's kitchen",'chuancai')
print(restaurant.restaurant_name,restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(restaurant.number_saved)
restaurant.number_saved = 10
print(restaurant.number_saved)
restaurant.set_number_served(15)
print(restaurant.number_saved)
restaurant.increment_number_served(100)
print(restaurant.number_saved)

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
user1 = User('mario','yu')
user2 = User('shanshan','liu')
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3 = User('jane','bread')
user3.increment_login_attempts(1)
user3.increment_login_attempts(1)
user3.increment_login_attempts(1)
user3.increment_login_attempts(1)
user3.increment_login_attempts(1)
print(user3.login_attempts)
user3.reset_login_attempts(0)
print(user3.login_attempts)