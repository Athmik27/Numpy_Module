# BROADCASTING ALLOWS NUMPY TO PERFORM THE OPERATIONS ON ARRAYS

import numpy as np

array_1=np.array([[1,2,3,4]])
array_2=np.array([[1],[2],[3],[4]])

print(array_1.shape)
print(array_2.shape) 
print(array_1 * array_2)#here we gwt an output because the dimensions for row and column matches or has 1 in either of their rows or column

# row and column mismatch
array_1=np.array([[1,2,3,4],
                  [5,6,7,8]])
array_2=np.array([[1],[2],[3],[4]])

print(array_1.shape)
print(array_2.shape)
print(array_1 * array_2) #here we can see that the row and column dimension do not matches or only column has '1' so it gives an error of "value-error"
# (2, 4) 
# (4, 1)

array_1=np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])
array_2=np.array([[1],[2],[3],[4]])

print(array_1.shape)
print(array_2.shape)
print(array_1 * array_2)
#(4, 4) we get  an output because here the condition is been satisfied either any column or row must have '1' and the rows are of same number(that is 4)
#(4, 1) 

# to check broadcasting rule is to check from right to left (values must be same or any one must have 1)
