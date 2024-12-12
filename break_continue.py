# i = 0

# while True:
#
#     if i + 1 < 5:
#         i += 1
#         continue
#
#     print(i, end=" ")
#     if i == 9:
#         break  # break the loop or exit loop
#     i += 1

# print("After exiting loop")

while True:
    inp = int(input("Enter a Number\n"))
    if inp > 100:
        print("You have entered no greater than 100")
        break
    else:
        print("Try again!")
        continue
