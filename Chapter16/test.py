import pygal.maps.world  # 导入世界地图包pygal_maps_world

# 定义函数，返回适用于pygal的两位国别码
def get_country_code(country_name):
     # pygal两位国别码列表表示法：pygal.maps.world.COUNTRIES.items()
    for code,name in pygal.maps.world.COUNTRIES.items():
        if name == country_name:
            return code
    return None

print(get_country_code('Albania'))