# n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#
# def num_greater_5(num):
#     return num > 5
#
#
# filter_n = list(filter(num_greater_5, n))
# print(filter_n)
# output: [6, 7, 8, 9]


dic_list = [
    {"name": "Hiral", "gender": "male"},
    {"name": "Foram", "gender": "female"},
    {"name": "Pankaj", "gender": "male"},
    {"name": "Vanita", "gender": "female"},
]


filter_dic_list = list(filter(lambda x: x['gender'] == 'female', dic_list))
print(filter_dic_list)
# # output: [{'name': 'Foram', 'gender': 'female'}, {'name': 'Vanita', 'gender': 'female'}]


