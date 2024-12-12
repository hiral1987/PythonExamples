# passing normal arguments

# def print_function(name, age, address, phone_number):
#     print(name, age, address, phone_number)
#
#
# print_function('Hiral', 35, 'Dombivli', 9821087355)


# passing *args (dynamic arguments) with normal arguments & **kwargs

def funargs(normal, *args, **kwargs):
    # print(type(args))
    print(normal)
    for item in args:
        print(item)

    for key, value in kwargs.items():
        print(f"{key} is a {value}")


names = ['Hiral', 'Foram']

names2 = {"Hiral": "Programmer", "Foram": "Manager"}
funargs(34, *names, **names2)
