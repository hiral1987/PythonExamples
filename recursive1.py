def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i + 1)
    return fac


def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


def fibonacci_recursive(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


num = int(input("Enter Number"))
print(fibonacci_recursive(num))
# print(factorial_iterative(num))
# print(factorial_recursive(num))
