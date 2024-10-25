import numpy as np

"""
-->   |||
-->   |||
-->   vvv
"""

matrix1 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
matrix2 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(type((1)))
print(type((1,)))
print(type({}))
print(type({1,2}))

print(list(zip([1,2,3, 4, 5], [4,5,6])))
print(list(enumerate([7,5,2], 3)))

list1 = [1,2,3]
list2, = [4,5,6]
for i in range(min(len(list1), len(list2))):
    print((list1[i], list2[i]))

c = 3
for i in range(len(list1)):
    print((i+c, list1[i]))

def transpose(matrix):
    result = []
    for row in range(len(matrix)):
        # new sublist for new row
        result.append([])
        for column in range(len(matrix[0])):
            # add to last sublist (last row)
            result[-1].append(matrix[column][row])
    return result

def multiply(matrix1, matrix2):
    result = [[0]*len(matrix2[0]) for _ in range(len(matrix1))]
    """
    [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    """
    for i, row in enumerate(matrix1):
        for j, column in enumerate(transpose(matrix2)):
            for a, b in zip(row, column):
                result[i][j] += a * b
    return result
"""
print(multiply(matrix1, matrix2))
print(np.matmul(matrix1, matrix2))
"""