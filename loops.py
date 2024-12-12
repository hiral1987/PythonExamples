# name = ["Harry", "larry", "Carry", "Marry"]
#
# for item in name:
#     print(item)

# Output:
# Harry
# larry
# Carry
#


# name = [["Harry", 1], ["larry", 2], ["Carry", 3], ["Marry", 4]]
#
# for item in name:
#     print(item)
#
# Output:
# ['Harry', 1]
# ['larry', 2]
# ['Carry', 3]
# ['Marry', 4]

# name = [["Harry", 1], ["larry", 2], ["Carry", 3], ["Marry", 4]]
#
# for item, no in name:
#     print(item, no)
#
# Output:
# Harry 1
# larry 2
# Carry 3
# Marry 4

name = [["Harry", 1], ["larry", 2], ["Carry", 3], ["Marry", 4]]
dict1 = dict(name)
#
# for item, no in dict1.items():
#     print(item, no)
#
# Output:
# Harry 1
# larry 2
# Carry 3
# Marry 4

# for item in dict1:
#     print(item)
#
# Output:
# Harry
# larry
# Carry
# Marry
