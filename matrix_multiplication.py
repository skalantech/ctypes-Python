import numpy as np
matrix_a = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix_b = np.array([[1,2,3],[4,5,6],[7,8,9]])

# transpose Matrix_b
matrix_b = np.transpose(matrix_b)

result = np.array([[0,0,0],[0,0,0],[0,0,0]])

# method 1. by for loop
for index_a, i in enumerate(matrix_a):
    for index_b, j in enumerate(matrix_b):
        result[index_a][index_b] = sum(i * j)

print(result, end='\n\n')

# method 2. by list comprehension
list_comprehension = [[sum(i * j) for j in matrix_b] for i in matrix_a]

for _ in list_comprehension:
    print(_)