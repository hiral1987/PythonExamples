# k = ["3", "4", "5", "6"]

# print(k)
# output: ['3', '4', '5', '6']

# for n in range(len(k)):
#     k[n] = int(k[n])
# output: [3, 4, 5, 6]

# print(k[2] + 1)
# output: 6

# Above for loop can be replaced by map function as below:

# k2 = list(map(int, k))
#
# print(k2)
# output: [3, 4, 5, 6]


ln = [2, 3, 4, 5, 6, 7, 8, 9]


# def sqr(a):
#     return a * a


# k3 = list(map(sqr, ln))

# 'sqr' function can be replaced by lambda
# k3 = list(map(lambda x: (x * x), ln))

# print(k3)
# output: [4, 9, 16, 25, 36, 49, 64, 81]


def square(a):
    return a * a


def cube(a):
    return a * a * a


func_list = [square, cube]

for i in range(len(ln)):
    val = list(map(lambda x: x(ln[i]), func_list))
    print(val)
