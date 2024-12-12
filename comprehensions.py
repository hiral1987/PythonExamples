# ls = []
#
# for i in range(100):
#     if i % 3 == 0:
#         ls.append(i)
# output: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51,
# 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]


# ls = [i for i in range(100) if i % 3 == 0]
# print('printing.........................')
# print(ls)

# output: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51,
# 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]


dict1 = {i: f'item{i}' for i in range(5)}
# print(dict1)
# output: {0: 'item0', 1: 'item1', 2: 'item2', 3: 'item3', 4: 'item4'}

dict1 = {value: key for key, value in dict1.items()}
print(dict1)
# output: {'item0': 0, 'item1': 1, 'item2': 2, 'item3': 3, 'item4': 4}
