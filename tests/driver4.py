import ctypes
import os
import time
from random import randint

def calc_sum(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

path = os.getcwd()
clib = ctypes.CDLL(os.path.join(path, 'test4.so'))

start = time.perf_counter()
value = clib.calc_sum(20000)
end = time.perf_counter()
print("Ctypes result:", value, " time taken:", end-start)

start = time.perf_counter()
value = calc_sum(20000)
end = time.perf_counter()
print("Python result:", value, " time taken:", end-start)