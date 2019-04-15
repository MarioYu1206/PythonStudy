import unittest
from employee import Employee

class TestGiveRaise(unittest.TestCase):
    def setUp(self):
        self.new_employee = Employee('mario', 'yu', 10000)

    def test_give_default_raise(self):
        salary = self.new_employee.give_raise()
        self.assertEqual(salary,self.new_employee.salary)
        print("should be 15000")
        print(self.new_employee.salary)

    def test_give_custom_raise(self):
        incr_salary = 2000
        salary = self.new_employee.give_raise(incr_salary)
        self.assertEqual(salary, self.new_employee.salary)
        print("should be 12000")
        print(self.new_employee.salary)