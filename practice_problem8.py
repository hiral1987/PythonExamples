import random


def multiplicationNumber(n):
    wrong = random.randint(0, 9)
    t = [i * n for i in range(1, 11)]
    t[wrong] = t[wrong] + random.randint(0, 10)
    return t


def getIncorrectIndex(t, n):

    for i in range(1, 11):
        if t[i - 1] != (i * n):
            return i - 1

    return None


if __name__ == '__main__':
    # print(multiplicationNumber(7))
    number = int(input('Enter a number'))
    table = multiplicationNumber(number)
    print(table)
    index = getIncorrectIndex(table, number)

    print(f'Wrong value at index: {index}')
