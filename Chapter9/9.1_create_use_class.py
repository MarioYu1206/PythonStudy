#创建类
class Dog(): #在Python中，首字母大写的名称指的是类，类定义中的括号是空的，因为要从空白开始创建这个类
    """一次模拟小狗的简单尝试"""
    # 每当你创建累的新实例是，会自动运行__init__()方法。
    def __init__(self, name, age): #形参self必不可少，还必须在最前面。它是一个指向实例本身的引用，让实例能访问类中的属性和方法。
        """初始化属性name和age"""
        self.name = name #以self为前缀的变量都可供类中的所有方法使用，可以通过类的任何实例来访问这些变量
        self.age = age #这种可通过实例访问的变量称为属性。
    def sit(self): #方法
        """模拟小狗被命令时坐下"""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """模拟小狗被命令是打滚"""
        print(self.name.title() + " rolled over!")

#根据类创建实例
my_dog = Dog('while', 6) #命名约定很有用，通常大写的表示类，小写表示实例
print("My dog's name is " + my_dog.name.title() + ".") #my_dog.name来访问属性
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit() #调用方法，指定实例的名称和要调用的方法
my_dog.roll_over()

your_dog = Dog('lucy', 3) #可以创建任意数量的实例
print("Your dog's name is " + your_dog.name.title() + ".") #my_dog.name来访问属性
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit() #调用方法，指定实例的名称和要调用的方法
your_dog.roll_over()


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
restaurant = Restaurant("Mario's kitchen",'chuancai')
print(restaurant.restaurant_name,restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

#practice 2
restaurant1 = Restaurant("jane's kitchen",'dongbeicai')
restaurant1.describe_restaurant()
restaurant2 = Restaurant("Tom's kitchen",'xiangcai')
restaurant2.describe_restaurant()
restaurant3 = Restaurant("kate's kitchen",'yuecai')
restaurant3.describe_restaurant()

#practice 3
class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title())
    def greet_user(self):
        print("Hello, " + self.first_name.title() + " " + self.last_name.title())
user1 = User('mario','yu')
user2 = User('shanshan','liu')
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()