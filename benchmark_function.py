from time import perf_counter
from timeit import timeit
import ctypes

def work():
    data = [i*i for i in range(100000000)]

time_start = perf_counter()

work()

time_end = perf_counter()

time_duration = time_end - time_start

# time_duration_2 = timeit("work()", globals=globals(), number=1)

print(f'Took {time_duration} seconds')
# print(f'Took {time_duration_2} seconds')

clibrary = ctypes.CDLL("./clibrary.so")
clibrary.work.restype = ctypes.POINTER(ctypes.c_int)

time_start1 = perf_counter()

cdata1 = clibrary.work(100000000)
data_list = cdata1[:100000000]
clibrary.free_array(cdata1)

time_end1 = perf_counter()
time_duration1 = time_end1 - time_start1

time_duration_3 = timeit("clibrary.work(100000000)", globals=globals(), number=1)
# memory leak

print(f'Took {time_duration1} seconds')
print(f'Took {time_duration_3} seconds')