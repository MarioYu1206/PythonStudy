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
from pygal.maps.world import COUNTRIES
print(COUNTRIES)
for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])

def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        return None
print(get_country_code('China'))
print(get_country_code('United States'))
print(get_country_code('Uzbekistan')) 还有问题