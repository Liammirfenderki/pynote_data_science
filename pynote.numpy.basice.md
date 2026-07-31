
## Create Arrays

```python
a = np.array([1, 2, 3])              # 1D
b = np.array([[1, 2], [3, 4]])       # 2D (matrix)
```

From range:

```python
arr = np.arange(0, 10, 2)            # [0, 2, 4, 6, 8]
```

Zeros / ones / constant:

```python
z = np.zeros((3, 4))                 # 3x4 zeros
o = np.ones((2, 2))                  # 2x2 ones
c = np.full((2, 3), 7)               # 2x3 filled with 7
```

Identity:

```python
I = np.eye(3)                        # 3x3 identity matrix
```

Random:

```python
r = np.random.rand(3, 4)             # uniform [0,1), shape 3x4
n = np.random.randn(3, 4)            # normal (mean=0, std=1)
```

---

## Array Info

```python
a.shape      # dimensions, e.g. (3,)
b.shape      # e.g. (2, 2)
a.ndim       # number of dimensions
a.dtype      # data type
a.size       # total elements
```

---

## Indexing & Slicing

```python
a = np.array([10, 20, 30, 40, 50])

a[0]         # first element
a[-1]        # last element
a[1:4]       # slice: elements 1..3
a[:3]        # first 3
a[3:]        # from index 3 to end
```

2D:

```python
b = np.array([[1, 2, 3],
              [4, 5, 6]])

b[0, 1]      # row 0, col 1 => 2
b[:, 0]      # first column => [1, 4]
b[1, :]      # second row   => [4, 5, 6]
```

---

## Boolean Masking

```python
a = np.array([1, 2, 3, 4, 5])

mask = a > 2
# [False, False, True, True, True]

a_filtered = a[mask]  # [3, 4, 5]

a_even = a[a % 2 == 0]  # [2, 4]
```

---

## Basic Math (Vectorized)

Element‑wise operations:

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b       # [5, 7, 9]
a - b       # [-3, -3, -3]
a * b       # [4, 10, 18]
a / b       # [0.25, 0.4, 0.5]
a ** 2      # [1, 4, 9]
```

Broadcasting:

```python
a + 10      # [11, 12, 13]
b * 2       # [8, 10, 12]
```

---

## Aggregate Functions

```python
a = np.array([1, 2, 3, 4])

np.sum(a)      # 10
np.mean(a)     # 2.5
np.min(a)      # 1
np.max(a)      # 4
np.std(a)      # standard deviation
np.var(a)      # variance
```

Axis‑wise (for 2D):

```python
b = np.array([[1, 2, 3],
              [4, 5, 6]])

np.sum(b, axis=0)   # column sums => [5, 7, 9]
np.sum(b, axis=1)   # row sums    => [6, 15]
```

---

## Linear Algebra

Dot product:

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.dot(a, b)   # 1*4 + 2*5 + 3*6 = 32
```

Matrix multiplication:

```python
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

C = A @ B      # matrix product
# or: C = np.matmul(A, B)
```

Transpose:

```python
A_T = A.T
```

Inverse (square, non‑singular):

```python
import numpy.linalg as LA

A_inv = LA.inv(A)
```

Determinant:

```python
det_A = LA.det(A)
```

Eigenvalues/vectors:

```python
vals, vecs = LA.eig(A)
```

---

## Reshape & Flatten

```python
a = np.arange(12)         # [0..11]
b = a.reshape(3, 4)       # 3x4
c = a.reshape(-1, 1)      # column vector

flat = b.ravel()          # view as 1D
flat2 = b.flatten()       # copy as 1D
```

---

## Stack & Concatenate

```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

h = np.hstack([x, y])     # [1, 2, 3, 4, 5, 6]
v = np.vstack([x, y])     # [[1,2,3],
                          #  [4,5,6]]
```

General concat (axis):

```python
A = np.ones((2, 2))
B = np.zeros((2, 2))

C = np.concatenate([A, B], axis=0)  # stack rows
D = np.concatenate([A, B], axis=1)  # add columns
```

---

## Random Utilities

Set seed (reproducible):

```python
np.random.seed(42)
```

Integers:

```python
r_int = np.random.randint(0, 10, size=(3, 3))
```

Choice:

```python
choices = np.array([10, 20, 30])
sample = np.random.choice(choices, size=5)
```

---

## Useful Helpers

Where:

```python
a = np.array([1, 2, 3, 4])

idx = np.where(a > 2)     # indices where condition is True
# (array([2, 3]),)
```

Unique:

```python
u = np.unique(a)
```

Clip:

```python
clipped = np.clip(a, 1, 3)  # values <1 =>1, >3=>3
```

---

## Quick Pattern: NumPy for Fast Computation

```python
import numpy as np

# large array
x = np.random.randn(1_000_000)

mean = np.mean(x)
std  = np.std(x)

# standardize
x_std = (x - mean) / std
```

