#制作世界人口地图
import json
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value'])) #float先转成小数，再转成整数
        print(country_name + ": " + str(population))

#获取两个字母的国别码
import pygal.maps.world
print(pygal.maps.world.COUNTRIES)
for country_code in sorted(pygal.maps.world.COUNTRIES.keys()):
    print(country_code + ' : ' + pygal.maps.world.COUNTRIES[country_code])

def get_country_code(country_name):
    for code, name in pygal.maps.world.COUNTRIES.items():
        if name == 'Yemen, Rep.':
            return  'ye'
        elif name == country_name:
            return code
    return None
print(get_country_code('Yemen'))
print(get_country_code('Andorra'))
print(get_country_code('Afghanistan'))

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            print(code + ": " + str(population))
        else:
            print("Error - " + country_name)

#制作世界地图
import pygal_maps_world
from pygal_maps_world import maps
wm = maps.World()
wm.title = 'North, Central, and South America'
wm.add('North America',['ca','mx','us'])
wm.add('Central America',['bz','cr','gt','hn','ni','pa','sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf','gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.render_to_file('americas.svg')

#在世界地图上呈现数字数据
import pygal_maps_world
from pygal_maps_world import maps
wm = maps.World()
wm.title = 'Population of Countries in North America'
wm.add('North America',{'ca': 34126000, 'us': 309349000, 'mx': 113423000})
wm.render_to_file('americas2.svg')

#绘制完整的世界人口地图
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country)
        print(code)
        if code:
            cc_populations[code] = population
wm = maps.World()
wm.title = 'World Population in 2010, by Country'
wm.add('2010',cc_populations)
wm.render_to_file('world_population.svg')

#根据人口数量将国家分组
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country)
        print(code)
        if code:
            cc_populations[code] = population
cc_pops_1, cc_pops_2, cc_pops_3 = {},{},{}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
print(len(cc_pops_1),len(cc_pops_1),len(cc_pops_1))
wm = maps.World()
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m',cc_pops_1)
wm.add('10m-1bn',cc_pops_2)
wm.add('>1bn',cc_pops_3)
wm.render_to_file('world_population2.svg')

#使用Pygal设置世界地图的样式
import pygal.style
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country)
        print(code)
        if code:
            cc_populations[code] = population
cc_pops_1, cc_pops_2, cc_pops_3 = {},{},{}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
print(len(cc_pops_1),len(cc_pops_1),len(cc_pops_1))
wm_style = pygal.style.RotateStyle('#336699', base_style=pygal.style.LightColorizedStyle)
wm_style2 =  pygal.style.LightColorizedStyle
wm = maps.World(style=wm_style2)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m',cc_pops_1)
wm.add('10m-1bn',cc_pops_2)
wm.add('>1bn',cc_pops_3)
wm.render_to_file('world_population3.svg')


#练习
#practice 2
import json
import pygal.style
import pygal.maps
filename = 'world_gdp.json'
with open(filename) as f:
    gdp_data = json.load(f)
cc_gdps = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == 2016:
        country_name = gdp_dict['Country Name']
        gdp = float(gdp_dict['Value'])
        code = get_country_code(country_name)
        cc_gdps[code] = gdp
# print(cc_gdps)
cc_gdp_1, cc_gdp_2, cc_gdp_3 = {},{},{}
for cc, gdp in cc_gdps.items():
    if gdp < 100000000000:
        cc_gdp_1[cc] = gdp
    elif gdp < 1000000000000:
        cc_gdp_2[cc] = gdp
    else:
        cc_gdp_3[cc] = gdp
print(cc_gdp_1)
print(cc_gdp_2)
print(cc_gdp_3)
wm_style = pygal.style.RotateStyle('#336699', base_style=pygal.style.LightColorizedStyle)
wm_style2 =  pygal.style.LightColorizedStyle
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World GDP in 2016, by Country'
wm.add('0-100bn',cc_gdp_1)
wm.add('100bn-1tn',cc_gdp_2)
wm.add('>1tn',cc_gdp_3)
wm.render_to_file('world_gdp.svg')