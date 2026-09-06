#FILTERING: an process of selecting elements from array that match the condition
# numpy uses C style operations.
import numpy as np

ages=np.array([[20,25,30],
               [35,40,45]])

adults=ages[ages>30]
print(adults)

# note to remember 
adults=ages[(ages>=25) & (ages<=40)]
adults=ages[(ages>=25) | (ages<=40)]

print(adults)

# when we print the array if we need to preserve an original shape we use 'where()' func
adults=np.where(ages>20,ages,0) 
# syntax :
# np.where(condition, value_if_true, value_if_false)
print(adults)
