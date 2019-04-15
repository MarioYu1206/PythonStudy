import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase): #创建一个测试类
    """test name_function.py"""
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self): #可以创建两个测试方法
        formatted_name = get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')

if __name__ == '__main__': #需要加入这一句
    unittest.main()