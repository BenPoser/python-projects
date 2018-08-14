class Employee:
    # class variables
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # Use 'Employee.' rather than 'self' as there is unlikely to be a use case where we want to override class
        # variable for a single instance of the class
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def details(self):
        return 'Name:{} {} Pay:{} Email:{}'.format(self.first, self.last, self.pay, self.email)

    # hard coding in the raise amount
    def apply_raise_hardcoded(self):
        self.pay = int(self.pay*1.04)

    # accessing raise amount through the class 'Employee.raise_amount' or 'self.raise_amount' if we use 'self.'
    # then we can change the variable for a single instance, if we use 'Employee.' then it will always change it
    # for the class 'self' also allows sub classes to override the class variable
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


print(Employee.num_of_emps)

emp_1 = Employee('Ben', 'Poser', 35000)
emp_2 = Employee('Tara', 'Watson', 40000)

print(emp_1.pay)
emp_1.apply_raise_hardcoded()
print(emp_1.pay)
print(Employee.raise_amount)
print(emp_1.raise_amount)
# no raise amount in list
print(emp_1.__dict__)
# class contains raise amount
print(Employee.__dict__)
# can change the raise amount variable for whole class
Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
# can change it for just one instance creating the variable in the instance
emp_1.raise_amount= 1.02
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_1.__dict__)

print(Employee.num_of_emps)
