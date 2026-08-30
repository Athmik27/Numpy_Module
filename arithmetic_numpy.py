# ARITHMETIC

import numpy as np

#scalar arithmetic this is an linear arthimetic value
array=np.array([1,2,3])
print(array +1)# this gives each value with+1 to it as an output
print(array -1)
print(array *2)
print(array ** 4)

#vectorised math functions its basically an 1D list

#lets find square root of the each
array=np.array([1,2,3])
print(np.sqrt(array))

print(np.round(array))#round's the number to nearest value

print(np.floor(array))#rounds each value DOWN to the nearest integer.

print(np.ceil(array))#rounds each value UP(go's up )to nearest integer.

#for constant value pi
print(np.pi)

#finding area of circle
radii=np.array([1,2,3])
print(np.pi * radii ** 2) # area=pi*r**2

#ELEMENT WISE ARITHMETIC
#performs arithmetic operations
array_1=np.array([1,2,3])
array_2=np.array([4,5,6])
print(array_1 + array_2)
print(array_1 - array_2)
print(array_1 * array_2)
print(array_1 / array_2)

#COMPARISION OPERATION
scores=np.array([80,75,85,90,95,65])

print(scores == 100 )# gives the boolean answer after checking the condition
scores[scores<80]=0
print(scores)
