yearAge = int(input('Enter your birth year or age\n'))

isAge = False

if yearAge < 125:
    isAge = True
elif yearAge > 2023:
    print('You are not yet born')
    exit()
elif yearAge > 1900:
    pass
elif yearAge < 1900:
    print('You are oldest person alive')
    exit()

else:
    print('Invalid age or birth year')
    exit()

if isAge:
    yearAge = 2023 - yearAge

print(f'You will be 100 years old in ${yearAge + 100}')

iYear = int(input('Enter the year you want to know your age\n'))

print(f'You wil be {iYear - yearAge} years old in {iYear}')
