food_list = [
    # 12, 10, 45, 30, 38
]

print(f'Welcome to the Hiral"s restaurant.')

size = int(input('Enter the size of list\n'))
for i in range(size):
    food_list.append(int(input('Enter the list item')))

print(f'Following are the food items:\n{food_list}\n')

# print('1st method to reverse list using inbuilt method')
# food_list2 = food_list[:]  # This will save copy of food_list in food_list2
# food_list.reverse()
# print(food_list)

# print('\n2nd method to reverse list using slicing trick')
# print(food_list[::-1])


# print('\n3rd method to reverse list using swapping')
#
# loop_range = 0
# if len(food_list) % 2 == 0:
#     loop_range = len(food_list) / 2
# else:
#     loop_range = (len(food_list) / 2) + 1
#
# for i in range(int(loop_range)):
#     i2 = len(food_list) - 1 - i
#     temp = food_list[i]
#     food_list[i] = food_list[i2]
#     food_list[i2] = temp
#
# print(food_list)


# OR


print('\n3rd method to reverse list using swapping')
food_list3 = food_list[:]
for i in range(len(food_list3) // 2):
    food_list3[i], food_list3[len(food_list3) - 1 - i] = food_list3[len(food_list3) - 1 - i], food_list3[i]

print(food_list3)
