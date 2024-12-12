
# a = input('What is your name')
#
# if a.isnumeric():
#     raise Exception('Nos. are not allowed')  # You can raise any type of exception here


c = input('Enter your name')

try:
    print(a)

except Exception as e:
    if c == 'harry':
        raise ValueError('Harry is blocked')

    print('Printed..')
