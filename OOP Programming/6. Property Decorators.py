class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    # defining it like a method but can access it like an attribute
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    # @property would allow us to take off the brackets for [print(emp1.fullname()) but would stop us from being able to
    # set the fullname so need to use a @property and a @x.setter
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleted Name')
        self.first = None
        self.last = None


emp_1 = Employee('Ben', 'Poser')

print(emp_1.first)
print(emp_1.fullname)
print(emp_1.email)

# If we change first name the fullname method still works but the email stays set as it was originally, don't want to
# use a method because it will break the code for everyone using the class, will have to change every instance -
# can use a property decorator
emp_1.first = 'Bill'

print(emp_1.fullname)
print(emp_1.email)

emp_1.fullname = 'Tara Watson'
print(emp_1.fullname)
print(emp_1.email)