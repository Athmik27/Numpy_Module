#SLICING

import numpy as np

array=np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])

#for slicing we use array[start:end:step]

print(array[0])
print(array[-1])
print(array[0:3]) # here end index is exclusive
print(array[1:])

#row selection
print(array[0:4:2]) 
# or
print(array[::2])
print(array[::-1])# output is in form of reversed manner

#column selection
# for slicing[row:column]
print(array[ : ,0:3])

 #for row and column
print(array[0:2,0:2])# array[row,column]



