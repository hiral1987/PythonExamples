var = "Harry is a good boy 123"

# print(len(var))  # print length of string
#
# print(var[0:5])  # print only Harry
#
# print(var[:5])  # print only Harry if first parameter not specified default is 0
#
# print(var[0:])  # print "Harry is a good boy", if second parameter not specified it will print whole string

# print "Hry", if third parameter specified it will print every number character specified in 3rd
# parameter
# print(var[0:5:2])

# if 3rd parameter not specified then default is 1 then it will print whole string
# print(var[0:5:])


# Negative Index

# 0  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
# H  a r r y   i s   a    g  o  o  d     b  o  y
# -19                                          -1


# print(var[::-1])  # this will reverse the string "yob doog a si yrraH"


print(var.replace(" ", "").isalnum())
print(var.replace(" ", "").isalpha())
