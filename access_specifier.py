class Employee:
    # public access specifier, this can be access anywhere & anybody
    available_leave = 10

    # protected access specifier, this will access only in containing class & class
    # who inherit containing class
    _my_leaves = 5

    # private access specifier, this will access only in containing class
    __total_no_leaves = 15

    # This is property access method of protected variable
    @property
    def my_leaves(self):
        return self._my_leaves

    def _print1(self):
        print('This is inside protected method')


emp = Employee()
# print(emp.available_leave)
# output: 10


# print(emp.my_leaves)
# output: 5


# print(emp._Employee__total_no_leaves)
# output: 15

# emp._print1()
# output: This is inside protected method
