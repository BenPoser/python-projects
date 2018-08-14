class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # repr method implicitly called when we use repr(object), unambiguous representation of object meant for other
    # developers, good way to use is to get it to return something that you could copy and paste
    # back into python to recreate the object
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    # str more readable version meant for users
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    # a way to add together two employees pay or other parts of objects, there are other special methods for other
    # mathematical operations - subtracting, multiplying, dividing etc.
    def __add__(self, other):
        return self.pay + other.pay

    # a way to use the len function to check the length of part of the instance
    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Ben', 'Poser', 35000)
emp_2 = Employee('Tara', 'Watson', 40000)


# without the str method would do the repr, can still call them how we choose
print(emp_1)
print(repr(emp_1))
print(str(emp_1))

# what it is really doing - calling special methods directly
print(emp_1.__repr__())
print(emp_1.__str__())

# __add__
print(1+2)
print(int.__add__(1, 2))
print(str.__add__('a', 'b'))

# adding two pays with special __add__ method
print(emp_1 + emp_2)

