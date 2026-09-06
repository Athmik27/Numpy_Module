# AGGREGATE FUNCTION this summarize the data andd return the single value

import numpy as np

array=np.array([[1,2,3],
                [4,5,6]])
print(np.sum(array))

# we can use keyword such as:

#   mean
#   std
#   var
#   min
#   max
#   argmin
#   argmax
#   median (middle value of array)

# sum function

print(np.sum(array, axis=0))  # column-wise sum
print(np.sum(array, axis=1) ) # row-wise sum



