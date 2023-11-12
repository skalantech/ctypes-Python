import ctypes
import os
import time
from random import randint

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1

def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)

path = os.getcwd()
clib = ctypes.CDLL(os.path.join(path, 'test3.so'))

array = (ctypes.c_int * 100)()
for i in range(100):
    array[i] = randint(0, 1000)

start = time.perf_counter()
clib.quick_sort(array, 0, 99)
end = time.perf_counter()
print("Ctypes time taken:", end-start)

new_array = []
for i in range(100):
    new_array.append(randint(0, 1000))

start = time.perf_counter()
value = quick_sort(new_array, 0, 99)
end = time.perf_counter()
print("Python time taken:", end-start)