
#  What is NumPy?

**NumPy** stands for:

> **Numerical Python**

It is a Python library mainly used for:

* Numerical computation
* Arrays
* Mathematical operations
* Statistics
* Linear algebra
* Random number generation
* Scientific computing
* Machine Learning


#  Why NumPy?

Python lists can store numbers:

```python
numbers = [10, 20, 30, 40]
```

But NumPy arrays are designed specifically for numerical operations.

```python
import numpy as np

numbers = np.array([10, 20, 30, 40])
```

You can perform operations directly:

```python
numbers * 2
```

Result:

```text
[20 40 60 80]
```

This is one of the major advantages of NumPy.

---

#  NumPy Array

The main data structure in NumPy is the:

> **ndarray**

Example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr)
```

Output:

```text
[10 20 30 40]
```

Check its type:

```python
print(type(arr))
```

Output:

```text
<class 'numpy.ndarray'>
```

---

# Creating Arrays

## From a Python list

```python
arr = np.array([1, 2, 3, 4, 5])
```

---

## 2D array

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

Output:

```text
[[1 2 3]
 [4 5 6]]
```

---

## 3D array

```python
arr = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])
```

---

## `zeros()`

Creates an array filled with zero.

```python
np.zeros(5)
```

Output:

```text
[0. 0. 0. 0. 0.]
```

2D:

```python
np.zeros((2, 3))
```

---

## `ones()`

```python
np.ones(5)
```

2D:

```python
np.ones((2, 3))
```

---

## `full()`

Create an array filled with a specific value:

```python
np.full(5, 10)
```

Output:

```text
[10 10 10 10 10]
```

---

## `arange()`

Creates values within a range.

```python
np.arange(1, 10)
```

Output:

```text
[1 2 3 4 5 6 7 8 9]
```

With step:

```python
np.arange(1, 10, 2)
```

Output:

```text
[1 3 5 7 9]
```

Syntax:

```python
np.arange(start, stop, step)
```

The `stop` value is normally excluded.

---

## `linspace()`

Creates evenly spaced numbers.

```python
np.linspace(0, 10, 5)
```

Output:

```text
[ 0.   2.5  5.   7.5 10. ]
```

Syntax:

```python
np.linspace(start, stop, number_of_values)
```

Unlike `arange()`, the endpoint is included by default.

---

#  Array Dimensions

NumPy arrays can have different dimensions.

## 0D

A single value:

```python
arr = np.array(10)
```

---

## 1D

```python
arr = np.array([1, 2, 3])
```

Think:

```text
[1 2 3]
```

---

## 2D

```python
arr = np.array([
    [1, 2],
    [3, 4]
])
```

Think:

```text
1 2
3 4
```

---

## 3D

An array containing multiple 2D arrays.

---

## Check dimensions

Use:

```python
arr.ndim
```

Example:

```python
arr = np.array([
    [1, 2],
    [3, 4]
])

print(arr.ndim)
```

Output:

```text
2
```

---

#  Array Attributes

These are extremely important.

```python
arr.shape
arr.ndim
arr.size
arr.dtype
arr.itemsize
```

---

## `shape`

Tells you the size along each dimension.

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.shape)
```

Output:

```text
(2, 3)
```

Meaning:

```text
2 rows
3 columns
```

---

## `ndim`

Number of dimensions:

```python
print(arr.ndim)
```

---

## `size`

Total number of elements:

```python
print(arr.size)
```

For:

```text
[[1 2 3]
 [4 5 6]]
```

result:

```text
6
```

---

## `dtype`

Data type:

```python
print(arr.dtype)
```

---

## `itemsize`

Number of bytes used by one element:

```python
print(arr.itemsize)
```

---

#  Data Types

NumPy supports many data types:

```text
int
float
bool
complex
string
```

Example:

```python
arr = np.array([1, 2, 3])

print(arr.dtype)
```

Specify a type:

```python
arr = np.array(
    [1, 2, 3],
    dtype="float64"
)
```

---

## Change data type

Use:

```python
astype()
```

Example:

```python
arr = np.array([1, 2, 3])

new_arr = arr.astype(float)
```

---

# Indexing

Indexing starts at `0`.

```python
arr = np.array([10, 20, 30, 40])
```

```python
print(arr[0])
```

Output:

```text
10
```

```python
print(arr[2])
```

Output:

```text
30
```

---

## Negative indexing

```python
print(arr[-1])
```

Output:

```text
40
```

```python
print(arr[-2])
```

Output:

```text
30
```

---

#  Slicing

Syntax:

```python
array[start:stop:step]
```

Example:

```python
arr = np.array([10, 20, 30, 40, 50])
```

```python
arr[1:4]
```

Result:

```text
[20 30 40]
```

---

## Step

```python
arr[::2]
```

Result:

```text
[10 30 50]
```

---

## Reverse

```python
arr[::-1]
```

Result:

```text
[50 40 30 20 10]
```

---

#  2D Array Indexing

Example:

```python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
```

Access first row:

```python
arr[0]
```

Output:

```text
[10 20 30]
```

Access first row, second column:

```python
arr[0, 1]
```

Output:

```text
20
```

General syntax:

```python
arr[row, column]
```

---

## Select a row

```python
arr[1, :]
```

---

## Select a column

```python
arr[:, 1]
```

---

#  3D Arrays

A 3D array has:

```text
depth
rows
columns
```

Example:

```python
arr = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])
```

Shape:

```python
print(arr.shape)
```

Output:

```text
(2, 2, 2)
```

Meaning:

```text
2 blocks
2 rows
2 columns
```

---

#  Changing Array Values

```python
arr = np.array([10, 20, 30, 40])

arr[1] = 100

print(arr)
```

Output:

```text
[ 10 100  30  40]
```

For 2D:

```python
arr[0, 1] = 999
```

---

# 15. Copy vs View

This is important.

## Copy

Creates a separate array.

```python
copy_arr = arr.copy()
```

Changes to the copy do not affect the original.

---

## View

A view shares the underlying data.

```python
view_arr = arr.view()
```

Changes to the view can affect the original array.

Remember:

```text
copy() → independent data
view() → shared data
```

---

# 16. Array Shape

You can inspect shape:

```python
arr.shape
```

Example:

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.shape)
```

Output:

```text
(2, 3)
```

---

# 17. Reshape

`reshape()` changes the shape without changing the data.

Example:

```python
arr = np.array([1, 2, 3, 4, 5, 6])

new_arr = arr.reshape(2, 3)
```

Result:

```text
[[1 2 3]
 [4 5 6]]
```

Important:

The total number of elements must remain the same.

```text
6 elements
↓
2 × 3 = 6
```

Therefore:

```python
arr.reshape(3, 2)
```

also works.

But:

```python
arr.reshape(4, 2)
```

❌ doesn't work because:

```text
4 × 2 = 8
```

and the original has only 6 elements.

---

## `-1` in reshape

NumPy can calculate one dimension automatically.

```python
arr.reshape(2, -1)
```

If there are 6 elements:

```text
2 × 3
```

NumPy calculates `-1` as `3`.

---

# 18. Flatten and Ravel

Convert a multidimensional array into 1D.

## `flatten()`

```python
arr.flatten()
```

Returns a copy.

## `ravel()`

```python
arr.ravel()
```

Usually returns a view when possible.

Remember:

```text
flatten() → copy
ravel()   → view when possible
```

---

# 19. Iteration

## 1D

```python
arr = np.array([10, 20, 30])

for x in arr:
    print(x)
```

---

## 2D

```python
arr = np.array([
    [1, 2],
    [3, 4]
])

for row in arr:
    print(row)
```

---

## Iterate every element

```python
for row in arr:
    for value in row:
        print(value)
```

For multidimensional arrays, `np.nditer()` is useful:

```python
for x in np.nditer(arr):
    print(x)
```

---

# 20. Joining Arrays

## `concatenate()`

```python
a = np.array([1, 2])
b = np.array([3, 4])

result = np.concatenate((a, b))
```

Result:

```text
[1 2 3 4]
```

---

## 2D concatenation

```python
np.concatenate(
    (a, b),
    axis=0
)
```

or:

```python
np.concatenate(
    (a, b),
    axis=1
)
```

The shapes must be compatible with the chosen axis.

---

## `stack()`

```python
np.stack((a, b))
```

Creates a new dimension.

---

## `vstack()`

Vertical stacking:

```python
np.vstack((a, b))
```

---

## `hstack()`

Horizontal stacking:

```python
np.hstack((a, b))
```

---

# 21. Splitting Arrays

## `array_split()`

```python
arr = np.array([1, 2, 3, 4, 5, 6])

np.array_split(arr, 3)
```

Result:

```text
[1 2]
[3 4]
[5 6]
```

---

## `split()`

```python
np.split(arr, 3)
```

`split()` requires equal-sized splits.

`array_split()` can handle uneven splits.

---

# 22. Searching Arrays

Use:

```python
np.where()
```

Example:

```python
arr = np.array([10, 20, 30, 40])

np.where(arr == 30)
```

It returns the index where the condition is true.

---

## Find values greater than 20

```python
np.where(arr > 20)
```

---

# 23. Filtering Arrays

Boolean filtering:

```python
arr = np.array([10, 20, 30, 40, 50])

result = arr[arr > 25]
```

Result:

```text
[30 40 50]
```

Multiple conditions:

```python
arr[(arr > 20) & (arr < 50)]
```

Remember:

```text
& → AND
| → OR
~ → NOT
```

---

# 24. `where()`

`np.where()` can also replace values conditionally.

```python
arr = np.array([10, 20, 30, 40])

result = np.where(
    arr > 25,
    100,
    0
)
```

Meaning:

```text
If value > 25 → 100
Otherwise      → 0
```

Result:

```text
[  0   0 100 100]
```

Syntax:

```python
np.where(condition, value_if_true, value_if_false)
```

---

# 25. Sorting

```python
arr = np.array([30, 10, 50, 20])

np.sort(arr)
```

Result:

```text
[10 20 30 50]
```

Original array is not modified.

---

## 2D sorting

```python
np.sort(arr, axis=0)
```

Sort columns.

```python
np.sort(arr, axis=1)
```

Sort rows.

---

# 26. Arithmetic Operations

NumPy supports element-wise arithmetic.

```python
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
```

Addition:

```python
a + b
```

Result:

```text
[11 22 33]
```

Subtraction:

```python
a - b
```

Multiplication:

```python
a * b
```

Division:

```python
a / b
```

Power:

```python
a ** 2
```

---

# 27. Broadcasting

**Broadcasting** allows NumPy to perform operations between arrays with compatible shapes.

Example:

```python
arr = np.array([10, 20, 30])

arr + 5
```

Result:

```text
[15 25 35]
```

NumPy effectively treats `5` as:

```text
[5 5 5]
```

---

## 2D example

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

arr + 10
```

Result:

```text
[[11 12 13]
 [14 15 16]]
```

---

## Broadcasting rule

Shapes are compared from the **rightmost dimension**.

Two dimensions are compatible if:

```text
They are equal
OR
One of them is 1
OR
One dimension does not exist
```

Example:

```text
(2, 3)
(3,)
```

Compatible.

Result:

```text
(2, 3)
```

---

# 28. Universal Functions

NumPy provides mathematical functions that work element-by-element.

```python
np.sqrt(arr)
np.abs(arr)
np.exp(arr)
np.log(arr)
np.sin(arr)
np.cos(arr)
np.round(arr)
```

---

## Square root

```python
np.sqrt([4, 9, 16])
```

Result:

```text
[2. 3. 4.]
```

---

## Absolute value

```python
np.abs([-10, -20, 30])
```

Result:

```text
[10 20 30]
```

---

# 29. Aggregate Functions

These calculate summary values.

```python
arr = np.array([10, 20, 30, 40])
```

Sum:

```python
np.sum(arr)
```

Mean:

```python
np.mean(arr)
```

Minimum:

```python
np.min(arr)
```

Maximum:

```python
np.max(arr)
```

Standard deviation:

```python
np.std(arr)
```

Variance:

```python
np.var(arr)
```

Median:

```python
np.median(arr)
```

Product:

```python
np.prod(arr)
```

---

# 30. Axis

**Axis is one of the most important NumPy concepts.**

For a 2D array:

```text
       columns
         ↓
      1  2  3
      4  5  6
      7  8  9
```

```text
axis=0 → down the rows
axis=1 → across the columns
```

Example:

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

### `axis=0`

```python
np.sum(arr, axis=0)
```

Result:

```text
[5 7 9]
```

Calculation:

```text
1 + 4 = 5
2 + 5 = 7
3 + 6 = 9
```

### `axis=1`

```python
np.sum(arr, axis=1)
```

Result:

```text
[ 6 15]
```

Calculation:

```text
1 + 2 + 3 = 6
4 + 5 + 6 = 15
```

### Remember

```text
axis=0 → operate DOWN
axis=1 → operate ACROSS
```

---

# 31. Random Module

NumPy provides:

```python
np.random
```

for generating random numbers.

---

# 32. Random Integer

```python
np.random.randint(1, 10)
```

Generates one random integer from:

```text
1 to 9
```

Generate multiple:

```python
np.random.randint(
    1,
    10,
    size=5
)
```

---

## 2D random integers

```python
np.random.randint(
    1,
    10,
    size=(2, 3)
)
```

Creates:

```text
2 rows
3 columns
```

---

# 33. Random Float

```python
np.random.random()
```

Generates a random floating-point number between:

```text
0 and 1
```

Multiple:

```python
np.random.random(5)
```

---

## `uniform()`

Generates random values from a uniform distribution.

```python
np.random.uniform(
    low=10,
    high=20,
    size=5
)
```

Values are between 10 and 20.

---

# 34. Random Normal Distribution

```python
np.random.normal(
    loc=50,
    scale=10,
    size=100
)
```

Meaning:

```text
loc   → mean
scale → standard deviation
size  → number of values
```

This is useful for:

* Statistics
* Simulations
* Data analysis
* Machine Learning

---

# 35. Random Choice

Select random elements:

```python
arr = np.array(
    ["Python", "Java", "C"]
)

np.random.choice(arr)
```

Select multiple:

```python
np.random.choice(
    arr,
    size=5
)
```

---

# 36. Random Seed

Random numbers normally change every time.

Use a seed for reproducible results:

```python
np.random.seed(42)
```

Then:

```python
np.random.randint(1, 100, 5)
```

will produce the same sequence each time with that seed.

### Why?

Useful when:

* Testing
* Debugging
* Machine Learning
* Sharing code

---

# 37. Linear Algebra

NumPy provides many linear algebra operations.

Import:

```python
import numpy as np
```

Matrix:

```python
A = np.array([
    [1, 2],
    [3, 4]
])
```

---

## Matrix transpose

```python
A.T
```

---

## Matrix multiplication

Use:

```python
A @ B
```

or:

```python
np.matmul(A, B)
```

---

## Dot product

```python
np.dot(a, b)
```

---

# 38. Matrix Operations

## Determinant

```python
np.linalg.det(A)
```

## Inverse

```python
np.linalg.inv(A)
```

## Eigenvalues

```python
np.linalg.eig(A)
```

## Solve equations

```python
np.linalg.solve(A, b)
```

These are more advanced but important for numerical computing and ML.

---

# 39. Handling NaN and Infinity

NumPy can represent missing numerical values using:

```python
np.nan
```

Example:

```python
arr = np.array([
    10,
    20,
    np.nan,
    40
])
```

Check NaN:

```python
np.isnan(arr)
```

---

## Sum with NaN

Normal:

```python
np.sum(arr)
```

may produce `nan`.

Use:

```python
np.nansum(arr)
```

This ignores NaN values.

Similarly:

```python
np.nanmean(arr)
np.nanmin(arr)
np.nanmax(arr)
np.nanmedian(arr)
```

---

## Infinity

```python
np.inf
```

Negative infinity:

```python
-np.inf
```

Check:

```python
np.isinf(arr)
```

---

# 40. Statistical Functions

Common functions:

```python
np.mean(arr)
np.median(arr)
np.std(arr)
np.var(arr)
np.min(arr)
np.max(arr)
np.percentile(arr, 25)
np.quantile(arr, 0.25)
```

---

## Percentile

```python
np.percentile(
    arr,
    25
)
```

Finds the 25th percentile.

---

# 41. Unique Values

```python
arr = np.array([
    1, 2, 2, 3, 3, 3
])

np.unique(arr)
```

Result:

```text
[1 2 3]
```

---

## Unique with counts

```python
values, counts = np.unique(
    arr,
    return_counts=True
)
```

---

# 42. Set Operations

NumPy provides set-like operations.

## Union

```python
np.union1d(a, b)
```

## Intersection

```python
np.intersect1d(a, b)
```

## Difference

```python
np.setdiff1d(a, b)
```

---

# 43. Saving and Loading Arrays

## Save

```python
np.save(
    "data.npy",
    arr
)
```

## Load

```python
arr = np.load(
    "data.npy"
)
```

---

## Save multiple arrays

```python
np.savez(
    "data.npz",
    arr1=arr1,
    arr2=arr2
)
```

---

# 44. Performance

One major advantage of NumPy is **speed**.

Python loop:

```python
numbers = [1, 2, 3, 4, 5]

result = []

for x in numbers:
    result.append(x * 2)
```

NumPy:

```python
numbers = np.array([
    1, 2, 3, 4, 5
])

result = numbers * 2
```

NumPy performs operations using optimized numerical routines.

### General rule

Prefer:

```python
NumPy vectorized operations
```

over unnecessary Python loops.

---

# 45. NumPy for Machine Learning

NumPy is extremely important in Machine Learning.

Typical ML data:

```text
Features → X
Target   → y
```

Example:

```python
X = np.array([
    [20, 170],
    [25, 175],
    [30, 180]
])

y = np.array([
    0,
    1,
    1
])
```

Here:

```text
X → input features
y → target/output
```

---

## Train/test data

Scikit-learn commonly works with NumPy arrays:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

---

## Normalization

A common ML operation:

```python
X_normalized = (
    X - np.mean(X, axis=0)
) / np.std(X, axis=0)
```

This demonstrates why understanding:

```text
mean()
std()
axis
broadcasting
```

is important.

---

# 46. Common Errors

## Shape mismatch

Example:

```python
a = np.array([1, 2, 3])
b = np.array([1, 2])

a + b
```

❌ Shapes are incompatible.

---

## Reshape error

```python
arr.reshape(3, 3)
```

If the array has only 6 elements:

❌ Cannot reshape 6 elements into 9 positions.

---

## IndexError

```python
arr[100]
```

when the array has only 10 elements.

---

## Broadcasting error

If shapes cannot satisfy NumPy's broadcasting rules:

```text
ValueError
```

will occur.

---

# 47. Important Functions

## ⭐⭐⭐⭐⭐ MUST KNOW

### Creating arrays

```python
np.array()
np.zeros()
np.ones()
np.full()
np.arange()
np.linspace()
```

### Array properties

```python
arr.shape
arr.ndim
arr.size
arr.dtype
```

### Indexing

```python
arr[0]
arr[-1]
arr[0, 1]
```

### Slicing

```python
arr[start:stop]
arr[::step]
arr[::-1]
```

### Reshaping

```python
arr.reshape()
arr.flatten()
arr.ravel()
```

### Searching/filtering

```python
np.where()
arr[condition]
```

### Sorting

```python
np.sort()
```

### Aggregation

```python
np.sum()
np.mean()
np.min()
np.max()
np.median()
np.std()
np.var()
```

### Axis

```python
axis=0
axis=1
```

### Combining

```python
np.concatenate()
np.stack()
np.vstack()
np.hstack()
```

### Splitting

```python
np.split()
np.array_split()
```

### Random

```python
np.random.randint()
np.random.random()
np.random.uniform()
np.random.normal()
np.random.choice()
np.random.seed()
```

---

# 48. NumPy Learning Path

Learn NumPy in this order:

```text
1.  What is NumPy?
        ↓
2.  np.array()
        ↓
3.  1D / 2D / 3D arrays
        ↓
4.  ndim / shape / size / dtype
        ↓
5.  Indexing
        ↓
6.  Slicing
        ↓
7.  Array operations
        ↓
8.  Reshape
        ↓
9.  Axis
        ↓
10. Aggregate functions
        ↓
11. Boolean filtering
        ↓
12. np.where()
        ↓
13. Broadcasting
        ↓
14. concatenate / stack
        ↓
15. split
        ↓
16. sort
        ↓
17. Random module
        ↓
18. Statistics
        ↓
19. Linear algebra
        ↓
20. NumPy + Pandas
        ↓
21. NumPy + Machine Learning
```

---

# 49. Quick Revision Cheat Sheet

```python
import numpy as np

# Create array
arr = np.array([1, 2, 3, 4])

# Create 2D array
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Array properties
arr.ndim
arr.shape
arr.size
arr.dtype

# Create arrays
np.zeros(5)
np.ones(5)
np.full(5, 10)

# Ranges
np.arange(1, 10)
np.arange(1, 10, 2)
np.linspace(0, 10, 5)

# Indexing
arr[0]
arr[0, 1]
arr[-1]

# Slicing
arr[1:4]
arr[::2]
arr[::-1]

# Reshape
arr.reshape(2, 3)
arr.reshape(3, 2)
arr.reshape(2, -1)

# Flatten
arr.flatten()
arr.ravel()

# Copy / View
arr.copy()
arr.view()

# Arithmetic
arr + 10
arr - 10
arr * 2
arr / 2
arr ** 2

# Filtering
arr[arr > 10]

# Where
np.where(arr > 10)
np.where(arr > 10, 1, 0)

# Sorting
np.sort(arr)

# Aggregation
np.sum(arr)
np.mean(arr)
np.min(arr)
np.max(arr)
np.median(arr)
np.std(arr)
np.var(arr)

# Axis
np.sum(arr, axis=0)
np.sum(arr, axis=1)

# Combining
np.concatenate((a, b))
np.stack((a, b))
np.vstack((a, b))
np.hstack((a, b))

# Splitting
np.split(arr, 2)
np.array_split(arr, 3)

# Unique
np.unique(arr)

# Random
np.random.randint(1, 10, 5)
np.random.random(5)
np.random.uniform(10, 20, 5)
np.random.normal(50, 10, 5)
np.random.choice(arr)

# Reproducibility
np.random.seed(42)

# NaN
np.isnan(arr)
np.nansum(arr)
np.nanmean(arr)

# Statistics
np.percentile(arr, 25)
np.quantile(arr, 0.25)

# Linear algebra
np.dot(a, b)
a @ b
np.linalg.det(A)
np.linalg.inv(A)
np.linalg.solve(A, b)

# Save / Load
np.save("data.npy", arr)
arr = np.load("data.npy")
```


Once you understand **NumPy + Pandas**, you're building a strong foundation for **Data Science and Machine Learning in Python**.
