
users = ['Rohan', 'Shubham', 'Ram', 'Priya',]

computer = ['Com 1', 'Com 2', 'Com 3', 'Com 4']

# template = 'Computer used by {} is {}'
template = 'Computer used by {1} is {0}'

for i in range(len(users)):
    # print(template.format(users[i], computer[i]))  # output: Computer used by Rohan is Com 1
    print(template.format(users[i], computer[i]))  # output: Computer used by Com 1 is Rohan
