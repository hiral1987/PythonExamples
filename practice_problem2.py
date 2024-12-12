n = int(input('Enter the no of apples harry got\n'))

print(f'Harry got {n} apples\n')

mn = int(input('Enter the minimum number\n'))
mx = int(input('Enter the maximum number\n'))

print(f'Minimum number is {mn} & maximum number is {mx}\n')

if mn == mx:
    print(f'Minimum & Maximum numbers are same. This is not a range\n')
    if n % mn == 0:
        print(f'{mn} is a divisor of {n}')
    else:
        print(f'{mn} is not a divisor of {n}')

elif mx < mn:
    print(f'Maximum number should not be less than minimum number')

else:
    for i in range(mn, mx + 1):
        if n % i == 0:
            print(f'{i} is a divisor of {n}')
        else:
            print(f'{i} is not a divisor of {n}')
