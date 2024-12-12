class Student:
    no_of_leaves = 8

    # constructor
    def __init__(self, aname):
        self.name = aname

    def print_details(self):
        return f"name is {self.name}"


# harry = Student()
#
# harry.name = 'harry'
#
# larry = Student()

# print(larry, harry)
# output: <__main__.Student object at 0x0000026984580750> <__main__.Student object at 0x0000026984580710>

# print(harry.name)
# output: harry

# print(harry.no_of_leaves)  # output: 8
# print(larry.no_of_leaves)  # output: 8
# print(Student.no_of_leaves)  # output: 8

# harry.no_of_leaves = 9
# print(harry.no_of_leaves)  # output: 9
# print(Student.no_of_leaves)  # output: 8

# Student.no_of_leaves = 10
# print(harry.no_of_leaves)  # output: 10
# print(Student.no_of_leaves)  # output: 10

# print(harry.__dict__)  # output: {'name': 'harry'}
# print(Student.__dict__)
# output: {'__module__': '__main__', 'no_of_leaves': 8, '__dict__': <attribute '__dict__' of 'Student' objects>,
# '__weakref__': <attribute '__weakref__' of 'Student' objects>, '__doc__': None}


# print(harry.print_details())  # output: name is harry


harry = Student("Harry")
print(harry.name)