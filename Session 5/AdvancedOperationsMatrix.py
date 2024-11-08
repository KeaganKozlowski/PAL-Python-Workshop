#Setting up the file
import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

#Determinant of a Matrix
##Used to find linear equations in solving systems
det_A = np.linalg.det(A)
print(det_A) #Output: -2.0000000000000004

#Inverse of Matrix
##Only works for sequare matrices with non-zero determinant
A_inv = np.linalg.inv(A)
print(A_inv) #Output: [[-2.   1. ][ 1.5 -0.5]]

#Eigenvalues and Eigenvectors
##Used in data reduction and scientific applications
eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues) #Output:[-0.37228132  5.37228132]
print(eigenvectors) #Output:[[-0.82456484 -0.41597356][ 0.56576746 -0.90937671]]

#Solving linear equations
##Eg: Ax = B, solve for x
x = np.linalg.solve(A, B)
print(x) #Output:[[-3. -4.][ 4.  5.]]
