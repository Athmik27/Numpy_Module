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
# 0 → start at index 0
# 4 → stop before index 4
# 2 → jump by 2 positions or take every 2nd element.

# or

print(array[::2])
# start → omitted → start from beginning
# stop → omitted → go until the end
# step → 2 → take every 2nd element

print(array[::-1])
# output is in form of reversed manner
# negative step (-1, -2, etc.) means move backward.

#column selection

# for slicing[row_slice : column_slice]

print(array[ : ,0:3])

# : → all rows
# 0:3 → columns 0, 1, 2
# Column 3 is excluded.

#for row and column

#array[row_start:row_stop, column_start:column_stop]
print(array[0:2,0:2])
# array[row,column]



