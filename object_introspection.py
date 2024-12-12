class Emp:

    def __init__(self, aname, asal, arole):
        self.nme = aname
        self.sal = asal
        self.role = arole

    def print_details(self):
        print(f'Name is{self.nme}, Salary is: {self.sal}, Role is: {self.role}')

    def __add__(self, other):
        print(f'Total salary is {self.sal + other.sal}')

    def __truediv__(self, other):
        print(f'Division is {self.sal / other.sal}')

    def __str__(self):
        return f'Name is {self.nme}, Salary is {self.sal}, Role is {self.role}'

    def __repr__(self):
        return f'Emp("{self.nme}", {self.sal}, "{self.role}")'


emp = Emp('Rohan', 50000, 'Programmer')

# print(type(emp))  # output: <class '__main__.Emp'>
# print(id(emp))  # output: 1676458675088 --> identity of object


# This print all methods & variables of class
# print(dir(emp))
# output:
# ['__add__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
# '__truediv__', '__weakref__', 'nme', 'print_details', 'role', 'sal']


import inspect

print(inspect.getmembers(emp))

# output: [('__add__', <bound method Emp.__add__ of Emp("Rohan", 50000, "Programmer")>), ('__class__',
# <class '__main__.Emp'>), ('__delattr__', <method-wrapper '__delattr__' of Emp object at 0x000001E61AB75890>),
# ('__dict__', {'nme': 'Rohan', 'sal': 50000, 'role': 'Programmer'}), ('__dir__', <built-in method __dir__ of Emp
# object at 0x000001E61AB75890>), ('__doc__', None), ('__eq__', <method-wrapper '__eq__' of Emp object at
# 0x000001E61AB75890>), ('__format__', <built-in method __format__ of Emp object at 0x000001E61AB75890>), ('__ge__',
# <method-wrapper '__ge__' of Emp object at 0x000001E61AB75890>), ('__getattribute__', <method-wrapper
# '__getattribute__' of Emp object at 0x000001E61AB75890>), ('__getstate__', <built-in method __getstate__ of Emp
# object at 0x000001E61AB75890>), ('__gt__', <method-wrapper '__gt__' of Emp object at 0x000001E61AB75890>),
# ('__hash__', <method-wrapper '__hash__' of Emp object at 0x000001E61AB75890>), ('__init__', <bound method
# Emp.__init__ of Emp("Rohan", 50000, "Programmer")>), ('__init_subclass__', <built-in method __init_subclass__ of
# type object at 0x000001E61AD5E8D0>), ('__le__', <method-wrapper '__le__' of Emp object at 0x000001E61AB75890>),
# ('__lt__', <method-wrapper '__lt__' of Emp object at 0x000001E61AB75890>), ('__module__', '__main__'), ('__ne__',
# <method-wrapper '__ne__' of Emp object at 0x000001E61AB75890>), ('__new__', <built-in method __new__ of type object
# at 0x00007FFB8F6B8DF0>), ('__reduce__', <built-in method __reduce__ of Emp object at 0x000001E61AB75890>),
# ('__reduce_ex__', <built-in method __reduce_ex__ of Emp object at 0x000001E61AB75890>), ('__repr__', <bound method
# Emp.__repr__ of Emp("Rohan", 50000, "Programmer")>), ('__setattr__', <method-wrapper '__setattr__' of Emp object at
# 0x000001E61AB75890>), ('__sizeof__', <built-in method __sizeof__ of Emp object at 0x000001E61AB75890>), ('__str__',
# <bound method Emp.__str__ of Emp("Rohan", 50000, "Programmer")>), ('__subclasshook__', <built-in method
# __subclasshook__ of type object at 0x000001E61AD5E8D0>), ('__truediv__', <bound method Emp.__truediv__ of Emp(
# "Rohan", 50000, "Programmer")>), ('__weakref__', None), ('nme', 'Rohan'), ('print_details', <bound method
# Emp.print_details of Emp("Rohan", 50000, "Programmer")>), ('role', 'Programmer'), ('sal', 50000)]

