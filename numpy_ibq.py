# number to be printed is greater than 40.
import numpy as np
arr = np.array([10, 25, 30, 45, 50, 65, 70])
var_num=arr[arr>40]
print(var_num)

# Write NumPy code to replace every element greater than 30 with 0.
arr = np.array([10, 20, 30, 40, 50])
arr[arr>30]=0
print(arr)

# NumPy code to find the sum of all elements greater than 30.
arr = np.array([10, 20, 30, 40, 50, 60])
num=arr[arr>30]
# print(num)
nums=np.sum(arr[arr>30])
print(nums)


# Write NumPy code to find the maximum value among the elements greater than 30.
arr = np.array([12, 45, 7, 89, 23, 56, 91, 34])
nums=np.max(arr[arr>30])
print(nums)

# Write NumPy code to calculate the average (mean) of elements that are greater than 30.
arr = np.array([10, 20, 30, 40, 50, 60])
nums=np.average(arr[arr>30]) #or instead of average np.mean(arr[arr > 30])
print(nums)

# Replace all values greater than 50 with 100.
arr = np.array([10, 25, 30, 45, 50, 65, 70])
arr[arr>50]=100
print(arr)


# NumPy code to find how many elements are greater than 40.
arr = np.array([10, 20, 30, 40, 50, 60, 70])
num=arr[arr>40]
print(num)
nums=np.count_nonzero(arr>40) # this counts the number of the digits in the nparray.
print(nums)


# NumPy code to find the number of elements that are between 20 and 50 inclusive.
arr = np.array([10, 20, 30, 40, 50, 60])
num=arr[(arr>20) & (arr<=50)]
print(num)
nums=np.count_nonzero((arr>20) & (arr<=50)) 
print(nums)
# in NumPy for multiple conditions:

# (condition1) & (condition2)
# np.count_nonzero(condition)

# NumPy code to replace all even numbers with -1
import numpy as np
arr = np.array([12, 25, 8, 45, 30, 67, 19, 50])
arr[arr % 2 == 0] = -1
print(arr)
# # or
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        arr[i] = -1

# # NumPy code to replace all values greater than 40 AND less than 70 with 0.
arr = np.array([10, 25, 30, 45, 50, 65, 70])
arr[(arr>40)&(arr<70)]=0
print(arr)

# average of all even numbers.
import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60])
arr[arr % 2==0]
print(np.mean(arr[arr % 2==0]))

# Count how many numbers are odd.
arr = np.array([10, 25, 30, 45, 50, 65, 70])
print(np.count_nonzero(arr[arr%2!=0]))

# Find the sum of all odd numbers.
arr = np.array([10, 25, 30, 45, 50, 65, 70])
print(np.sum(arr[arr % 2!=0]))

# Find the maximum value among the odd numbers.
arr = np.array([10, 25, 30, 45, 50, 65, 70])
print(np.max(arr[arr % 2!=0]))

# Find the minimum value among the numbers greater than 30.
arr = np.array([10, 25, 30, 45, 50, 65, 70])
print(np.min(arr[arr>30]))

# Find the average of all numbers greater than 30
arr = np.array([10, 25, 30, 45, 50, 65, 70])
print(np.mean((arr[arr>30])))

# Count how many numbers are greater than 30 AND even.
arr = np.array([10, 25, 30, 45, 50, 65, 70])
print(np.count_nonzero((arr>30) & (arr % 2 ==0)))
# [] → used for indexing/filtering: arr[condition]
# () → used for grouping conditions: (condition1) & (condition2)


# Replace all odd numbers with -1.
import numpy as np
arr = np.array([10, 25, 30, 45, 50, 65, 70])
arr[arr %2 !=0]=-1
print(arr)

# Replace all values between 20 and 50 (inclusive) with 100.
arr = np.array([10, 25, 30, 45, 50, 65, 70])
arr[(arr >= 20) & (arr <= 50)] = 100
print(arr)

# Find the standard deviation of all values greater than 30.
arr = np.array([10, 25, 30, 45, 50, 65, 70])
print(np.std(arr[arr>30]))

# # Find the variance of all values less than 50.
arr = np.array([10, 25, 30, 45, 50, 65, 70])
print(np.var(arr[arr<50]))


# Replace all values greater than the mean with 0
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
nums = np.mean(arr)
arr[arr > nums] = 0
print(arr)

# Normalize the array by dividing every value by the maximum value.(imp)
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
max_value = np.max(arr)
result = arr / max_value
print(result)