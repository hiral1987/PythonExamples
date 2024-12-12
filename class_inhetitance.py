
class Student:
    no_of_leaves = 8

    # constructor
    def __init__(self, aname, asal, arole):
        self.name = aname
        self.salary = asal
        self.role = arole

    def print_details(self):
        return f"name is {self.name}"

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    # class methods as alternative constructor
    @classmethod
    def getInstance(cls, str2):
        # params = str2.split('-')
        # return cls(params[0], params[1], params[2])
        return cls(*str2.split('-'))


harry = Student("harry", 10000, "manager")

# harry.change_leaves(15)
#
# print(harry.no_of_leaves)  # output: 15
# print(Student.no_of_leaves)  # output: 15

# student = Student.getInstance(f"Mohan-{25500}-assistant")
#
# print(student.salary)
