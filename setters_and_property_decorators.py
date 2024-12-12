class Emp:

    def __init__(self, aname, asal, arole):
        self.nme = aname
        self.sal = asal
        self.role = arole
        # self.email = f'{aname}@gmail.com'

    # def print_details(self):
    #     print(f'Name is{self.nme}, Salary is: {self.sal}, Role is: {self.role}')

    def explain(self):
        return f'Employee is {self.nme}'

    @property  # decorator
    def email(self):
        if self.nme is None:
            return 'Email is not set'
        return f'{self.nme}@gmail.com'

    @email.setter
    def email(self, emailid):
        self.nme = emailid.split('@')[0]

    @email.deleter
    def email(self):
        self.nme = None

    # def __add__(self, other):
    #     print(f'Total salary is {self.sal + other.sal}')

    # def __truediv__(self, other):
    #     print(f'Division is {self.sal / other.sal}')

    # def __str__(self):
    #     return f'Name is {self.nme}, Salary is {self.sal}, Role is {self.role}'

    # def __repr__(self):
    #     return f'Emp("{self.nme}", {self.sal}, "{self.role}")'


emp1 = Emp('Rohan', 50000, 'Programmer')
# emp2 = Emp('Mohan', 20000, 'Cleaner')


# ------------------------------------------------------------------
# print(emp1.explain())  # output: Employee is Rohan
# print(emp1.email)  # output: Rohan@gmail.com

# emp1.nme = 'Sohan'

# After changing name still print old email id
# print(emp1.email)  # output: Rohan@gmail.com


# ------------------------------------------------------------------
# print(emp1.explain())  # output: Employee is Rohan
# print(emp1.email())  # output: Rohan@gmail.com

# emp1.nme = 'Sohan'

# After changing name still print old email id
# print(emp1.email())  # output: Sohan@gmail.com


# ------------------------------------------------------------------
# calling email method without round bracket & without @property annotation
# print(emp1.email)  # output: <bound method Emp.email of <__main__.Emp object at 0x000001BB4A5A4810>>

# emp1.nme = 'Sohan'

# After changing name still print old email id
# print(emp1.email)  # output: <bound method Emp.email of <__main__.Emp object at 0x000001BB4A5A4810>>


# calling email method without round bracket & with @property decorator
# print(emp1.email)  # output: Rohan@gmail.com

# emp1.nme = 'Sohan'

# After changing name still print old email id
# print(emp1.email)  # output: Sohan@gmail.com

# ------------------------------------------------------------------
emp1.email = "this.that@gmail.com"
# output: AttributeError: property 'email' of 'Emp' object has no setter

# After adding email.setter
# print(emp1.nme)  # output: this.that
# print(emp1.email)  # output: this.that@gmail.com
#

# deleting email attribute using deleter decorator
# del emp1.email
# print(emp1.email)  # output: None@gmail.com or Email is not set
