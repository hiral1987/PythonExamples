# Multiple inheritance example

class Employee:
    # this is class variable
    no_of_leaves = 10

    def __init__(self, aname, asal, adesg):
        # this is instance variable
        self.name = aname
        self.sal = asal
        self.desg = adesg

    def print_details(self):
        print(f'name is {self.name} & salary is : {self.sal} & designation is {self.desg}')


class GovernmentEmployee:
    govt_id_card = True
    no_of_leaves = 15

    def __init__(self, name):
        self.name = name

    def print_details(self):
        print(f'name is  {self.name}')


class Programmer(GovernmentEmployee, Employee):
    pass

# In this multiple inheritance example, inheritance sequence matters eg :(Employee, GovernmentEmployee)

# --------------------------------------------------------------------------------
# Creating instance of programmer, if first inheritance class is Employee then we must pass arguments
# define by Employee constructor(__init__)

# programmer = Programmer('Hiral', 5000, 'programmer')
# programmer.print_details()
# output: name is Hiral & salary is : 5000 & designation is programmer

# ---------------------------------------------------------------------------------
# Creating instance of programmer, if first inheritance class is GovernmentEmployee, so we must pass arguments
# define by GovernmentEmployee constructor(__init__)

# programmer = Programmer('Hiral')
# programmer.print_details()
# output: name is  Hiral


# ------------------------------------------------------------------------------------
# Here printing 'no_of_leaves' variable defined only in Employee class & creating instance of Programmer
# with first inheritance class is GovernmentEmployee,

# programmer = Programmer('Hiral')
# print(programmer.no_of_leaves)
# output: 10


# ------------------------------------------------------------------------------------
# Here printing 'no_of_leaves' variable defined in Employee as well as GovernmentEmployee class &
# creating instance of Programmer with first inheritance class is GovernmentEmployee,

# programmer = Programmer('Hiral')
# print(programmer.no_of_leaves)
# output: 15
