import ctypes
import os
import time

def fib(n):
    a = 0
    b = 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return b

path = os.getcwd()
clib = ctypes.CDLL(os.path.join(path, 'test2.so'))

start = time.perf_counter()
value = clib.fib(30)
end = time.perf_counter()
print("Ctypes result:", value, " time taken:", end-start)

start = time.perf_counter()
value = fib(30)
end = time.perf_counter()
print("Python result:", value, " time taken:", end-start)