
# i = 0
l1 = ['Hiral', 'Foram', 'Vanita', 'Pankaj']

# for item in l1:
#     if i % 2 != 0:   # if i % 2 is not 0
#         print(f'My name is {item}')
#     i += 1

# To reduce above code we will use enumerate function

for index, item in enumerate(l1):
    if (index % 2) != 0:
        print(f'My name is {item}')
