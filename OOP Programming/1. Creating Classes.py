class Employee:

    # Initialising class
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    # methods that take the instance 'self' as first argument
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def details(self):
        return 'Name:{} {} Pay:{} Email:{}'.format(self.first, self.last, self.pay, self.email)


emp_1 = Employee('Ben', 'Poser', 35000)
emp_2 = Employee('Tara', 'Watson', 40000)

# only prints the object or class
print(emp_1)
print(Employee)

# prints detail
print(emp_1.first)

# prints method
print(emp_2.fullname)

# prints output of method
print(emp_2.fullname())
print(Employee.fullname(emp_1))

# printing all the details
print(emp_1.first, emp_1.last, emp_1.pay, emp_1.email)
print(emp_2.details())
print(emp_1.__dict__)

