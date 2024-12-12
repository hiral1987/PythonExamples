import bisect

number = 5
lst = [1, 2, 4, 6, 7, 8]

# to bisect, your list should be sorted else bisect module will not work properly

print(bisect.bisect(lst, number))
bisect.insort(lst, number)
print(lst)
