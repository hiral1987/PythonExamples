# Multilevel inheritance example

class Employee:
    no_of_leaves = 10

    def __init__(self, aname, asal, adesg):
        self.name = aname
        self.sal = asal
        self.desg = adesg

    def print_details(self):
        print(f'name is {self.name} & salary is : {self.sal} & designation is {self.desg}')


class GovernmentEmployee(Employee):
    govt_id_card = True
    no_of_leaves = 15

    def __init__(self, aname, asal, adesg):
        super().__init__(aname, asal, adesg)

    def print_details(self):
        print(f'name is  {self.name}')


class Programmer(GovernmentEmployee):
    no_of_leaves = 20


# ge = GovernmentEmployee('Hiral', 15000, 'Sr. Programmer')
# ge.print_details()
# output: name is  Hiral


# -----------------------------------------------------------------
# here 'print_details' method available in GovernmentEmployee & Employee class,
# calling 'print_details' method on programmer instance then it will call method of
# GovernmentEmployee class
# -------------------------- OR --------------------------------------
# If 'print_details' method available only in Employee class & calling
# 'print_details' method on programmer instance then it will call method of
# Employee class

# First check variable or method in parent class, if not available then it will
# check in parent of parent class & so on till he finds that variable or method

# ge = Programmer('Hiral', 15000, 'Sr. Programmer')
# ge.print_details()
# output: name is  Hiral


# ------------------------------------------------------------------

