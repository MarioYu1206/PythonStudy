#可以在列表中嵌套字典，也可以在字典中嵌套列表，甚至可以在字典中嵌套字典

#字典列表
#创建一个外星人列表，每个外星人都是一个字典
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

#创建一个用于存储外星人的空列表
aliens = []
#创建30个外星人
for alien_number in range(30):
    new_alien = {'color':'green','points':5, 'speed':'slow'}
    aliens.append(new_alien)
#显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")
#显示创建了多少个外星人
print("total number of aliens: " + str(len(aliens)))


aliens = []
for alien_number in range(30):
    new_alien = {'color':'green','points':5, 'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
for alien in aliens[:5]:
    print(alien)
print("...")
for alien in aliens[:10]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'
for alien in aliens[:15]:
    print(alien)
print("...")


#在字典中存储列表
#每当需要在字典中讲一个键关联到多个值时，都可以在字典中嵌套一个列表
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
    }
print("you have ordered a " + pizza['crust'] + "-crust pizza " +
      "with following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
    }
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print("\n" + name.title() + "'s favorite language is:")
        for language in languages:
            print("\t" + language.title())
    else:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())


#在字典中存储字典
users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
        },
    }
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())



#练习
#practice 1
people = [
{
        'first_name':'Shanshan',
        'last_name':'Liu',
        'age':31,
        'city':'Dalian',
        },
    {
        'first_name':'Junlong',
        'last_name':'Yu',
        'age':31,
        'city':'Shanghai',
        }
    ]
for user in people:
    print(user['first_name'] + user['last_name'] + ", " + "Age: " + str(user['age']) + ", City: " + user['city'])

#practice 2
dog = {'type':'dog','master':'mario'}
cat = {'type':'cat','master':'jane'}
rabbit = {'type':'rabbit','master':'tom'}
deer = {'type':'deer','master':'kate'}
pets = [dog, cat, rabbit, deer]
for pet in pets:
    for key, value in pet.items():
        print(key + ": " + value)

#practice 3
favorite_places = {
    'mario':['dalian','shanghai','beijing'],
    'jane':['tokyo','new york','london','beijing'],
    'tom':['shenyang','daqing'],
    }
for friend,places in favorite_places.items():
    print(friend + "'s favorite places are:")
    for place in places:
        print("\t" + place)

#practice 4
lucky_numbers = {
    'mario':[7,8,9],
    'jane':[8,2,5,7],
    'tom':[9],
    'jack':[3],
    'kate':[1,0],
    }
for name, numbers in lucky_numbers.items():
    print(name + "'s lucky numbers are:")
    for number in sorted(numbers):
        print(number)

#practice 5
cities = {
    'dalian':{
        'country':'china',
        'population':6000000,
        'fact':'dongbeimingzhu',
        },
    'london':{
        'country':'great britain',
        'population':10000000,
        'fact':'jinrongzhongxin',
        },
    'toyko':{
        'country':'japan',
        'population':30000000,
        'fact':'yazhouzuifadachengshi',
        },
    }
for city, city_info in cities.items():
    print(city)
    # print(city_info['fact'])
    for key, value in city_info.items():
        print("\t" + key + ": " + str(value))