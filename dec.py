# def function1():
#     print("Print something")
#
#
# function2 = function1
# del function1
# function2()  # output: Print something


# def fnc(num):
#     if num == 0:
#         return print
#     elif num == 1:
#         return sum
#
#
# a = fnc(1)
# print(a)
# output:
# passing 0: <built-in function print>,
# passing 1: <built-in function sum>


# def somefunc(func):
#     func("printing..........")
#
#
# somefunc(print)
# # output: printing..........


def func1(func):
    def func2():
        print('Executing....')
        func()
        print('Executed....')
    return func2


# def some_func():
#     print("Printing inside some_func")
# some_func = func1(some_func)

# Above lines can be replaced by following code
@func1
def some_func():
    print("Printing inside some_func")


some_func()



