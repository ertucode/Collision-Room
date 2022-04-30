# import time

# start = time.time()
# e = 2.718281828459045
# for i in range(10000000):
#     x = (e**(0.1*1j)).imag

# print(time.time() - start)

from vector import Vector2

x = Vector2(0,2)

x **= (0,2)

print(x)
print(x ** (0, 2))
print(x ** (0,2.3))







