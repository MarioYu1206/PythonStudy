class Employee():
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, incr_salary = 5000):
        self.salary += incr_salary
        return self.salary


# new_employee = Employee('mario','yu',10000)
# new_employee.give_raise()