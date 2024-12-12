
class Student:
    no_of_leaves = 8

    # constructor
    def __init__(self, aname):
        self.name = aname

    def print_details(self):
        return f"name is {self.name}"

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves


harry = Student("harry")

harry.change_leaves(15)

print(harry.no_of_leaves)
print(Student.no_of_leaves)
