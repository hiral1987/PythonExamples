from functools import reduce

n = [1, 2, 3, 4, 5]

# num = 0
# for i in n:
#     num = num + i


# Above code can be written using reduce function

num = reduce(lambda x, y: (x + y), n)

print(num)
# output: 15
