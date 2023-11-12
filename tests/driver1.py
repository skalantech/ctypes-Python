import ctypes
import os
import time

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

path = os.getcwd()
clib = ctypes.CDLL(os.path.join(path, 'test1.so'))

start = time.perf_counter()
value = clib.fib(30)
end = time.perf_counter()
print("Ctypes result:", value, " time taken:", end-start)

start = time.perf_counter()
value = fib(30)
end = time.perf_counter()
print("Python result:", value, " time taken:", end-start)