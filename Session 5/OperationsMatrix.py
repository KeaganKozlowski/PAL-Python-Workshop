import numpy as np
#Addition and Subtraction
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = A + B   #Addition
D = A - B   #Subtraction

#Multiplication
##Element wise multiplication
C = A * B
##Dot multiplication
C = np.dot(A, B)

#Transposition
##Switches rows and columns
A_transpose = A.T
print(A_transpose) #Output: [[1 3][2 4]]


