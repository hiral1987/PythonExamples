import time

# initial = time.time()
# k = 0
# while k < 100:
#     time.sleep(2) // stop execution of code for specified seconds
#     print('Hello world')
#     k += 1
#
# print('While loop ran in', time.time() - initial, 'seconds')
#
# initial2 = time.time()
#
# for i in range(100):
#     print('Hello world123')
#
# print('For loop ran in', time.time() - initial2, 'seconds')

t = time.time()

t1 = time.localtime(t)

print('t1:', t1)

localtime = time.asctime(t1)

print('localtime:', localtime)
