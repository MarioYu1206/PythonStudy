#使用return语句将值返回到调用函数的代码行

#返回简单值
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)

#让实参变成可选的
def get_formatted_name(first_name, middle_name, last_name):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('john','lee','hooker')
print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('john','hooker')
print(musician)
musician = get_formatted_name('john','hooker', 'lee')
print(musician)

#返回字典
def build_person(first_name, last_name):
    person = {'first':first_name,'last':last_name}
    return person
musician = build_person('jimi','hendrix')
print(musician)

def build_person(first_name, last_name, age=''):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi','hendrix')
print(musician)
musician = build_person('jimi','hendrix',27)
print(musician)

#结合使用函数和while循环
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name: ")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print("\nhello, " + formatted_name + "!")


#练习
#practice 1
def city_country(city,country):
    print(city.title() + ", " + country.title())
city_country('dalian','china')
city_country('LA','USA')
city_country('london','UK')

#practice 2
def make_album(singer,album_name):
    album = {'singer':singer,'album_name':album_name}
    print(album)
make_album('mario','abc')
make_album('jane','def')
make_album('tom','hij')

#practice 3
def make_album(singer,album_name):
    album = {'singer':singer,'album_name':album_name}
    print(album)
active_flg = True
while active_flg:
    singer = input("singer: ")
    if singer == 'q':
        break
    album_name = input("album_name: ")
    if album_name == 'q':
        break
    make_album(singer,album_name)