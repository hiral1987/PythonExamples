class Emp:

    def __init__(self, aname, asal, arole):
        self.nme = aname
        self.sal = asal
        self.role = arole

    # def print_details(self):
    #     print(f'Name is{self.nme}, Salary is: {self.sal}, Role is: {self.role}')

    def __add__(self, other):
        print(f'Total salary is {self.sal + other.sal}')

    def __truediv__(self, other):
        print(f'Division is {self.sal / other.sal}')

    # def __str__(self):
    #     return f'Name is {self.nme}, Salary is {self.sal}, Role is {self.role}'

    def __repr__(self):
        return f'Emp("{self.nme}", {self.sal}, "{self.role}")'


emp1 = Emp('Rohan', 50000, 'Programmer')
# emp2 = Emp('Mohan', 20000, 'Cleaner')

# emp1 + emp2
# output 1 :
# adding two objects using + sign without __add__ method, it will throw error as below:
# TypeError: unsupported operand type(s) for +: 'Emp' and 'Emp'

# output 2 :
# adding two objects using + sign with __add__ method, it will throw error as below:
# Total salary is 70000


# emp1 / emp2
# output:
# dividing two objects using / sign with __truediv__ method, it will throw error as below:
# Division is 2.5

# -------------------------------------------------------------------------------------
# after overriding __str__ & __repr__ method & print emp1 object
# print(str(emp1))
# output: Name is Rohan, Salary is 50000, Role is Programmer

# -------------------------------------------------------------------------------------
# commenting __str__ method
print(str(emp1))
# output: Emp("Rohan", 50000, "Programmer")
