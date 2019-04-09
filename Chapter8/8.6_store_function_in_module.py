#函数的优点之一是可将代码块与主程序分离
#导入整个模块
import pizza #貌似模块不能以数字开头来命名。。。
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms','green peppers','extra cheese')

#导入特定函数
from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms','green peppers','extra cheese')

#使用as给函数指定别名
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms','green peppers','extra cheese')

#使用as给模块指定别名
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms','green peppers','extra cheese')

#导入模块中的所有函数
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms','green peppers','extra cheese')