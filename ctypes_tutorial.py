import ctypes
import os

clibrary = ctypes.CDLL("./clibrary.so")
cpplibrary = ctypes.CDLL("D:/p_win/py/ctypes/cpplibrary.so", winmode=0)

clibrary.display(b"John", 18)
func = clibrary.display
func.argtypes = [ctypes.c_char_p, ctypes.c_int]
func.restype = ctypes.c_char_p
func(b"John", 18)

print(clibrary.add(5, 6))
py_add = clibrary.add
py_add.argtypes = [ctypes.c_int, ctypes.c_int]
py_add.restypes = ctypes.c_int
print(py_add(5, 6))

s1 = ctypes.c_char_p(b"Hello world\n")
print(s1)
s1.value = b"Hello Universe\n"
print(s1)
clibrary.show(s1)

s2 = ctypes.create_string_buffer(100)
s2.value = b"Carlos Alfredo\n"
print(s2)
clibrary.show(s2)
s2.value = b"Alfredo Carlos\n"
print(s2)
clibrary.show(s2)

alloc_func = clibrary.alloc_memory
alloc_func.restype = ctypes.POINTER(ctypes.c_char_p)

free_func = clibrary.free_memory
free_func.argtypes = [ctypes.POINTER(ctypes.c_char_p)]

cstr_pointer = alloc_func()
cstr = ctypes.c_char_p.from_buffer(cstr_pointer)
print(cstr.value)
free_func(cstr_pointer)
print("END!")

# slower
num = ctypes.c_int(100)
ptr = ctypes.pointer(num)
print(ptr.contents)

# faster
num2 = ctypes.c_int(200)
ptr2 = ctypes.POINTER(ctypes.c_int)
ptr2.contents = num
print(ptr2.contents)
ptr2.contents = num2
print(ptr2.contents)

# CPP
cpplibrary.func_v()
cpplibrary.func_i(1)
cpplibrary.func_s(b"Carlos")

# Arrays
path = os.getcwd()
clibrary_path = ctypes.CDLL(os.path.join(path, "clibrary.so"))

values = (ctypes.c_int * 10)()
for i in range(len(values)):
    values[i] = i
sum = clibrary_path.sumArray(values, len(values))
print("Sum:", sum)

clibrary_path.incArray.restype = ctypes.POINTER(ctypes.c_int)
result = clibrary_path.incArray(values, len(values))
print(result.contents)
for i in range(len(values)):
    print(result[i])

# create python list from C-array
clibrary_path.work.restype = ctypes.POINTER(ctypes.c_int)
result1 = clibrary_path.work(10)
print(result1.contents)
mylist = []
for i in range(10):
    mylist.append(result1[i]) # SLOW
    print(result1[i])
mylist_fast = result1[:10] # FASTER
clibrary_path.free_array(result1)
print(mylist)
print(mylist_fast)


# structs
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]


p = Point(5, 6)
clibrary_path.printPoint(p)
print("x:", p.x, "y:", p.y)

clibrary_path.getPoint.restype = ctypes.POINTER(Point)
p1 = clibrary_path.getPoint()
print("x:", p1.contents.x, "y:", p1.contents.y)


class Student(ctypes.Structure):
    _fields_ = [("name", ctypes.c_char_p)]

name = "Carlos Alfredo Escalante Castillo"
s = Student(bytes(name, 'utf-8'))
clibrary_path.printStudentDetails(s)

# when returning a pointer from a function do this...
clibrary_path.getStudent.restype = ctypes.POINTER(Student)
s = clibrary_path.getStudent()
print(s)
print(s.contents)
print(s.contents.name.decode('utf-8'))
clibrary_path.free_struct(s)


class PointArray(ctypes.Structure):
    _fields_ = [("points", Point * 3)]


points = (Point(1, 1), Point(2, 3), Point(5, 10))
pa = PointArray(points)
clibrary_path.printPointArray(pa)