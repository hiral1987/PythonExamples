def next_palindrome(n):
    n = n + 1

    while not is_palindrome(n):
        n += 1

    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == '__main__':
    size = int(input('Enter the size of list\n'))
    mylist = []
    for i in range(size):
        mylist.append(int(input('Enter the element\n')))

    print(f'My list is : {mylist}')

    print(f'Output: {[i if i < 10 else next_palindrome(i) for i in mylist]}')

    # for i in mylist:
    #     if i > 10:
    #         m = next_palindrome(i)
    #         print(f'Next palindrome of number {i} is {m}')
    #     else:
    #         print(f'{i} is less than equal to 10')

    # while True:
    #     if str(i) == str(i)[::-1]:
    #         print(f'Next palindrome of number {n} is {i}')
    #         exit()
    #
    #     else:
    #         i = i + 1
    #         continue
