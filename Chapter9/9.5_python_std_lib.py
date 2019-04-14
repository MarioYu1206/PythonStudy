from collections import OrderedDict

favorite_languages = OrderedDict() #创建了OrderedDict类的一个实例，有序字典
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'd'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + " | " + language.title())
#这是一个很不错的类， 它兼具列表和字典的主要优点（在将信息关联起来的同时保留原来的顺序） 。 等你开始对关心的现实情形建模时， 可能会发现有序字典正好能够满足需求。


#练习
#practice 1
vocabularies = {
    'cat':"猫",
    'dog':"狗",
    'pig':"猪",
    }
for name, desc in vocabularies.items():
    print(name , desc)

vocabularies = OrderedDict()
vocabularies['cat'] = '猫'
vocabularies['dog'] = '狗'
vocabularies['pig'] = '猪'
for name, desc in vocabularies.items():
    print(name, desc)

#practice 2
from random import randint
x = randint(1,6) #包含6
class Die():
    def __init__(self, roll_times = 10, sides = 6):
        self.sides = sides
        self.roll_times = roll_times
    def roll_die(self):
        i = 0
        while i < self.roll_times:
            print(randint(1,self.sides))
            i += 1
    def update_roll_times(self, change_num):
        self.roll_times = change_num

my_die = Die()
my_die.roll_die()
my_die.update_roll_times(5)
my_die.roll_die()