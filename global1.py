x = 89  # GLOBAL


def print_global():
    x = 20  # LOCAL

    def print2():
        global x
        x = 88

    print2()


print_global()
print(x)
