# importing for is weekday static method
import datetime


class Employee:
    # class variables
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def details(self):
        return 'Name:{} {} Pay:{} Email:{}'.format(self.first, self.last, self.pay, self.email)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # class method decorator - alters the functionality of the method so we receive class (cls) as first argument
    # instead of the instance (self), convention is cls because we can't use the word class (reserved word)
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # using class method as alternate constructor for specific use cases
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # static methods don't take instance or class as first argument but they are included in a class because they have a
    # logical connection to it. If you don't access instance or class then use static method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Ben', 'Poser', 35000)
emp_2 = Employee('Tara', 'Watson', 40000)

print(Employee.raise_amount)
print(emp_1.raise_amount)

# working with the class instead of the instance
Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)

# trying to run class method with instance still changes for whole class
emp_1.set_raise_amt(1.07)

print(Employee.raise_amount)
print(emp_1.raise_amount)

# using alternate constructor to allow us to split up strings to create new instances of the class
emp_str_1 = "John-Doe-70000"
emp_str_2 = "Joe-Don-40000"
emp_str_3 = "James-Dill-30000"

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

# sunday
my_date = datetime.date(2016, 7, 10)
# monday
my_date2 = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))
print(Employee.is_workday(my_date2))