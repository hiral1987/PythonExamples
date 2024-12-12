
f = open('hir.txt')

try:
    # f1 = open('hir1.txt')
    print('executed try successfully')

except IOError as e1:
    print(e1)

except Exception as e2:
    print(e2)

else:
    print('except block not executed.. so executing else block')

finally:
    f.close()
    print('executed finally block')