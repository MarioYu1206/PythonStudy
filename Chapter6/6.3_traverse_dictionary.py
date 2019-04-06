#遍历所有的键值对
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
    }
for key, value in user_0.items(): #声明两个变量key和value，使用字典的items()方法，它返回一个键值对列表。
    print("\nKey: " + key)
    print("Value: " + value)

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")


#遍历字典中的所有键
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
for name in favorite_languages.keys(): #使用keys()方法来获取字典中的键
    print(name.title())
for name in favorite_languages: #此处隐式省略keys()方法，结果和上面的一样，都显示所有的键
    print(name.title()) #也遍历显示所有的键


favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends: #遍历中判断name是否是朋友
        print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print(favorite_languages.keys()) #dict_keys(['jen', 'sarah', 'edward', 'phil']) ， keys()方法返回所有键的列表


#按顺序遍历字典中的所有键
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
for name in sorted(favorite_languages.keys()): #使用sorted()方法对字典中的键进行字母顺序排序
    print(name.title() + ",thank you for taking the poll.")


#遍历字典中的所有值
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
print("the following languages have been mentioned:")
for language in favorite_languages.values(): #使用values()方法来获取字典中的值，返回一个值列表，不包含键。这种做法提取字典中的所有值，而没有考虑是否重复。
    print(language.title())

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
print("the following languages have been mentioned:")
for language in set(favorite_languages.values()): #使用set()方法来获的不重复的值，set()类似于列表，但是每个元素都必须是独一无二的。可以使用set()来去重。
    print(language.title()) #C Ruby Python



#练习
#practice 1
vocabularies = {
    'for':"遍历循环",
    'test':"测试",
    }
