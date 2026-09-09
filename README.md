#  NumPy Module 

NumPy is a Python library used for **numerical operations and working with arrays**.

```python
import numpy as np
```

---

# 1. Create NumPy Array 

```python
a = np.array([1, 2, 3, 4, 5])
```

2D array:

```python
a = np.array([[1, 2], [3, 4]])
```

---

# 2. Array Properties 

```python
a.ndim       # number of dimensions
a.shape      # rows and columns
a.size       # total elements
a.dtype      # data type
```

Example:

```python
a = np.array([[1, 2], [3, 4]])

print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
```

---

# 3. Create Special Arrays 

```python
np.zeros(5)
np.ones(5)
np.full(5, 10)
```

2D:

```python
np.zeros((2, 3))
np.ones((2, 3))
```

---

# 4. `arange()` 

Creates values with a step.

```python
np.arange(0, 10, 2)
```

Output:

```text
[0 2 4 6 8]
```

Syntax:

```python
np.arange(start, stop, step)
```

---

# 5. `linspace()` 

Creates evenly spaced values.

```python
np.linspace(0, 10, 5)
```

---

# 6. Indexing 

```python
a = np.array([10, 20, 30, 40])

a[0]
a[2]
a[-1]
```

2D:

```python
a[0, 1]
```

---

# 7. Slicing 

```python
a[1:4]
```

Syntax:

```python
array[start:stop:step]
```

Example:

```python
a[::2]
```

---

# 8. Reshape 

Change the shape of an array.

```python
a = np.array([1, 2, 3, 4, 5, 6])

a.reshape(2, 3)
```

Important:

```text
Number of elements must remain the same.
```

---

# 9. Flatten 

Convert multidimensional array into 1D.

```python
a.flatten()
```

---

# 10. Mathematical Operations 

```python
np.sum(a)
np.mean(a)
np.median(a)
np.min(a)
np.max(a)
np.std(a)
np.var(a)
```

---

# 11. Axis 

For:

```python
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

Column-wise:

```python
np.sum(a, axis=0)
```

Row-wise:

```python
np.sum(a, axis=1)
```

### Remember

```text
axis=0 → down the rows → column result
axis=1 → across columns → row result
```

---

# 12. Sorting 

```python
np.sort(a)
```

---

# 13. Searching 

Find positions:

```python
np.where(a > 5)
```

Find maximum position:

```python
np.argmax(a)
```

Find minimum position:

```python
np.argmin(a)
```

---

# 14. Filtering 

```python
a[a > 5]
```

Multiple conditions:

```python
a[(a > 5) & (a < 10)]
```

---

# 15. `where()` 

```python
np.where(a > 5, "High", "Low")
```

Meaning:

```text
condition → value if True → value if False
```

---

# 16. Random Numbers 

```python
np.random.rand(5)
```

Random integers:

```python
np.random.randint(1, 10, 5)
```

Uniform random values:

```python
np.random.uniform(1, 10, 5)
```

Normal distribution:

```python
np.random.normal(loc=50, scale=10, size=5)
```

---

# 17. Broadcasting 

NumPy allows operations between arrays of compatible shapes.

```python
a = np.array([1, 2, 3])
b = 10

a + b
```

Output:

```text
[11 12 13]
```

---

# 18. Array Arithmetic 

```python
a + b
a - b
a * b
a / b
a ** 2
```

Element-wise operations are performed.

---

# 19. Matrix Multiplication 

Element-wise multiplication:

```python
a * b
```

Matrix multiplication:

```python
a @ b
```

or:

```python
np.matmul(a, b)
```

---

# 20. Concatenate 

Join arrays:

```python
np.concatenate((a, b))
```

For 2D arrays:

```python
np.concatenate((a, b), axis=0)
```

---

# 21. Copy 

```python
b = a.copy()
```

Creates an independent copy.

Avoid:

```python
b = a
```

because both variables can refer to the same array.

---

# 22. Common NumPy Functions 

| Function              | Use                   |
| --------------------- | --------------------- |
| `np.array()`          | Create array          |
| `np.zeros()`          | Array of zeros        |
| `np.ones()`           | Array of ones         |
| `np.full()`           | Fill with value       |
| `np.arange()`         | Values with step      |
| `np.linspace()`       | Evenly spaced values  |
| `np.reshape()`        | Change shape          |
| `np.flatten()`        | Convert to 1D         |
| `np.sum()`            | Sum                   |
| `np.mean()`           | Average               |
| `np.median()`         | Median                |
| `np.min()`            | Minimum               |
| `np.max()`            | Maximum               |
| `np.sort()`           | Sort                  |
| `np.where()`          | Conditional selection |
| `np.argmax()`         | Position of maximum   |
| `np.argmin()`         | Position of minimum   |
| `np.concatenate()`    | Join arrays           |
| `np.random.randint()` | Random integers       |
| `np.random.uniform()` | Uniform random values |
| `np.random.normal()`  | Normal distribution   |

---

# CHEAT SHEET

```python
import numpy as np

a = np.array([1, 2, 3])

a.ndim
a.shape
a.size
a.dtype

np.zeros(5)
np.ones(5)
np.arange(0, 10, 2)
np.linspace(0, 10, 5)

a[0]
a[1:4]

a.reshape(2, 3)
a.flatten()

np.sum(a)
np.mean(a)
np.max(a)
np.min(a)
np.median(a)
np.std(a)

np.sum(a, axis=0)
np.sum(a, axis=1)

a[a > 5]
np.where(a > 5)

np.argmax(a)
np.argmin(a)

np.random.randint(1, 10, 5)
np.random.uniform(1, 10, 5)
np.random.normal(50, 10, 5)

a + b
a * b
a @ b

np.concatenate((a, b))
```


