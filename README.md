   NUMPY/NUMERICAL PYTHON.

It's an Python library mainly used for working with numerical data and arrays.
NumPy array is known as ndarray .

IMPORT MODULE NUMPY AS:
              import numpy as np

For Example we need to print an number 10,20,30,40,50 through numpy we write as 

  import numpy as np
  numbers = np.array([10, 20, 30, 40, 50])
  print(numbers)

1) np.array() — NUMPY ARRAY:
A NumPy array is a collection of values stored in a structured way so NumPy can perform numerical operations efficiently.

(i) One-Dimensional Array:
For Example:
      a = np.array([10, 20, 30, 40])

(ii) Two-Dimensional Array:
For Example:
      a = np.array([
            [10, 20, 30],
            [40, 50, 60]
            ])



Property	              Meaning
ndim	                  Number of dimensions
shape	                  Size along each dimension
size	                  Total number of elements
dtype	                  Data type of elements

For Example:

a = np.array([
      [10, 20, 30],
      [40, 50, 60]
])

print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)


THE KEYWORD'S USED:

(i) arange(): 
It creates numbers within a specified range.

Syntax:
np.arange(start, stop, step)

eg:a = np.arange(1, 10)


(ii) linspace() 
It's used when you want to create evenly spaced numbers between a starting value and an ending value.

Syntax:
np.linspace(start, stop, num)    num → how many values you want

eg:a = a = np.linspace(0, 10, 5)


There are many-more keyword's which we'll see below

   Function                   Purpose   
    np.array()             Create an array from existing data        
    np.zeros()             Create array filled with `0`              
    np.ones()              Create array filled with `1`              
    np.full()              Create array filled with a specific value 
    np.arange()           Generate values using a step              
    np.linspace()           Generate evenly spaced values             
    np.eye()                Create identity matrix                    
    np.empty()              Create uninitialized array                
    np.random.random()      Random decimal values                    
    np.random.randint()        Random integer values   


  NUMPY INDEXING:

  (i) 1D Indexing :
  Similar to the normal indexing.

  (ii) 2D Indexing :

eg:
  a = np.array([
      [10, 20, 30],
      [40, 50, 60],
      [70, 80, 90]
]) 

we Visualize it like:
            Column
             0    1    2
        ┌──────────────
Row 0   │ 10   20   30
Row 1   │ 40   50   60
Row 2   │ 70   80   90

a[row, column] is the syntax.

SLICING IN NUMPY ARRAY:

a[row_start : row_stop , column_start : column_stop] this is the syntax for slicing in 2D Array.

eg:a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

  a[0:2, 1:3] 
  we need to access this row and column from the 2D Array.

FUNCTION'S USED IN NUMPY:
  
np.sum()       → total
np.min()       → smallest
np.max()       → largest
np.mean()      → average
np.median()    → middle value
np.std()       → standard deviation
np.sqrt()      → square root
np.abs()       → absolute value

NUMPY AXIS:

For example:

import numpy as np
a = np.array([
      [10, 20, 30],
      [40, 50, 60],
      [70, 80, 90]
    ])

axis=0
Think of axis=0 as going down the rows, meaning we calculate column-wise.

For:
np.sum(a, axis=0)

NumPy calculates:
Column 0: 10 + 40 + 70 = 120
Column 1: 20 + 50 + 80 = 150
Column 2: 30 + 60 + 90 = 180


axis=1
s going across the column, meaning we calculate row-wise.

For:
np.sum(a, axis=1)

This calculates across each row.
Row 0: 10 + 20 + 30 = 60
Row 1: 40 + 50 + 60 = 150
Row 2: 70 + 80 + 90 = 240

Note:
axis=0 → move vertically → calculate each column
axis=1 → move horizontally → calculate each row



Table To Remember:

| Code                 | Meaning                |
| -------------------- | ---------------------- |
| `np.sum(a)`          | Sum everything         |
| `np.sum(a, axis=0)`  | Sum each column        |
| `np.sum(a, axis=1)`  | Sum each row           |
| `np.mean(a, axis=0)` | Mean of each column    |
| `np.mean(a, axis=1)` | Mean of each row       |
| `np.max(a, axis=0)`  | Maximum of each column |
| `np.max(a, axis=1)`  | Maximum of each row    |

IMPORTANT TERMS:

(i) NumPy reshape():
reshape() is used to change the shape of an array without changing its data.

eg:

import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
print(a)

print(a.shape)

b = a.reshape(2, 3)
print(b)


(ii) Numpy flatten():
flatten() converts a multidimensional array into a 1D array.

eg:


import numpy as np
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(a.flatten())


(iii) Numpy ravel():
ravel() also converts an array into 1D.

eg:

import numpy as np
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(a.ravel())


(iv) Numpy Transpose .T ⭐
This transpose changes:
Rows to columns and columns to rows
 
eg:

import numpy as np
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(a.T)

(v) np.concatenate():
concatenate() joins arrays along an existing axis.

eg:
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.concatenate((a, b))
print(c)

(vi) vstack() — Vertical Stack:
vstack() means vertical stacking.
It puts arrays one below another.

eg:
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.vstack((a, b))
print(c)

(vii) hstack() — Horizontal Stack
hstack() means horizontal stacking.
It puts arrays side by side.

eg:
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.hstack((a, b))
print(c)

Note:
| Function        | What it does                     |
| --------------- | -------------------------------- |
| `concatenate()` | Joins along an **existing axis** |
| `vstack()`      | Stacks **vertically**            |
| `hstack()`      | Stacks **horizontally**          |
| `stack()`       | Joins along a **new axis**       |


(viii) NumPy split():
np.split() is used to divide one NumPy array into multiple smaller arrays.

Syntax:
np.split(array, number_of_parts)

eg:
import numpy as np
a = np.array([10, 20, 30, 40, 50, 60])

result = np.split(a, 3)
print(result)

(ix) np.hsplit():
hsplit() means Horizontal Split.
It splits an array vertically, creating separate groups of columns.

Syntax:
np.hsplit(array, number_of_parts)

eg:
import numpy as np
a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

result = np.hsplit(a, 2)
print(result)


(x) np.vsplit():
vsplit() means Vertical Split.
It splits an array horizontally, creating separate groups of rows.

Syntax:
np.vsplit(array, number_of_parts)

eg:
import numpy as np
a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

result = np.vsplit(a, 2)
print(result)

(xi) copy():
A copy creates a completely separate array.

eg:
import numpy as np
a = np.array([10, 20, 30])

b = a.copy()
b[0] = 100
print("a =", a)
print("b =", b)

(xii) view():
A view does not create a separate copy of the data.
It gives you another way to access the same underlying data.

eg:
import numpy as np
a = np.array([10, 20, 30])

b = a.view()
b[0] = 100
print("a =", a)
print("b =", b)

(xiii) np.where():
np.where() is used to find positions or select values based on a condition.
It is similar to an if condition, but it works efficiently with NumPy arrays.

Syntax:
np.where(condition)

eg:
import numpy as np
a = np.array([10, 25, 30, 45, 50])

indices = np.where(a > 30)
print(a[indices])

Syntax:
np.where(condition, value_if_true, value_if_false)

eg:
import numpy as np
marks = np.array([35, 80, 45, 90, 20])

result = np.where(marks >= 40, "Pass", "Fail")
print(result)


(xiv)np.sort():

Syntax:
np.sort(array)

eg:
import numpy as np
a = np.array([50, 20, 40, 10, 30])

result = np.sort(a)
print(result) 

result = np.where(a > 30)
print(result)


(xv) np.argsort():
np.argsort() returns the indices that would arrange the array in sorted order.

eg:
import numpy as np
a = np.array([50, 20, 40, 10, 30])

result = np.argsort(a)
print(result)


(xvi) np.unique():
np.unique() is used to find the unique (non-repeated) values in an array.
It removes duplicate values.

Syntax:
np.unique(array)

eg:
import numpy as np
a = np.array([10, 20, 10, 30, 20, 40, 30])

result = np.unique(a)
print(result)

(xvii) np.random.random():
Generates random decimal numbers between 0 and 1.

Syntax:
np.random.random(size)

eg:
import numpy as np
a = np.random.random(5)

print(a)


(xviii) np.random.randint()
Generates random integers.

Syntax:
np.random.randint(start, stop, size)
stop value is not included.

eg:
import numpy as np
a = np.random.randint(1, 10, 5)

print(a)

(xix) np.random.uniform():
Generates random decimal numbers within a specified range.

Syntax:
np.random.uniform(low, high, size)

eg:
import numpy as np
a = np.random.uniform(10, 20, 5)

print(a)


