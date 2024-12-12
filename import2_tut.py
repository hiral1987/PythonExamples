def print_something(s):
    return f"hi this is printing str : {s}"


def add(num1, num2):
    return num1 + num2


# Below code will execute only if execute from same file
# this will not execute if we import this file in other module


if __name__ == '__main__':
    print(print_something("Hiral"))
    print(add(10, 15))
