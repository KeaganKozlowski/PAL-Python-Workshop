#Importing library
import numpy as np

#Creating arrays - Basics
np.array([1, 2, 3])            #1D array
np.array([[1, 2], [3, 4]])      #2D array
np.zeros((2, 2))                #2x2 array of 0s
np.ones((2, 3))                 #2x3 array of 1s
np.arange(0, 10, 2)             #Array: [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)            #5 values between 0 and 1
np.random.rand(2, 2)            #2x2 array of random values [0, 1)

#Array operations
## Arithmetic operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
a + b                           #Element-wise addition
a * b                           #Element-wise multiplication
np.dot(a, b)                    #Dot product

## Aggregate functions
a.sum(), a.mean(), a.max()      #Sum, Mean, Max
np.sqrt(a)                      #Element-wise square root
np.exp(a)                       #Element-wise exponential

#Indexing and slicing
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr[1, 2]                       #Access element at row 1, col 2
arr[:, 1]                       #Access all rows, column 1
arr[0, :]                       #Access row 0, all columns
arr[0:2, 1:3]                   #Subarray from rows 0-1, cols 1-2

#Reshaping and Transposing
arr.reshape(3, 2)               #Change shape to 3x2
arr.flatten()                   #Flatten array to 1D
arr.T                           #Transpose array (swap rows/cols)

#Masking and Filtering
arr = np.array([1, 2, 3, 4, 5])
arr[arr > 3]                    #Elements > 3
np.where(arr > 3, arr, 0)       #If arr > 3, keep arr; else 0

#Common Statistical Functions
data = np.array([1, 2, 3, 4, 5])
np.mean(data)                   #Mean
np.median(data)                 #Median
np.std(data)                    #Standard deviation
np.percentile(data, 50)         #50th percentile

