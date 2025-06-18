
# 🧮 NumPy Arrays in Python

## What is NumPy?

[NumPy](https://numpy.org/) (short for *Numerical Python*) is a powerful Python library used for numerical and scientific computing. It provides support for **arrays**, mathematical functions, linear algebra, random number generation, and more.

They are similar to lists but are more efficient and simpler to use in multiple dimensions.


## Importing NumPy

You will need to import numpy into your code to use it

```python
import numpy as np
```

> `np` is a common alias used for NumPy.

## Creating a NumPy Array

### From a Python List

```python
import numpy as np

my_list = [1, 2, 3]
my_array = np.array(my_list)

print(my_array)
# Output: [1 2 3]
```

### 2D arrays

(This is how your connect4 board is represented)

```python
nested_list = [[1, 2, 3], [4, 5, 6]]
array_2d = np.array(nested_list)

print(array_2d)
# Output:
# [[1 2 3]
#  [4 5 6]]
```

## Array Properties

```python
print(array_2d.shape)   # (2, 3) - 2 rows, 3 columns
print(array_2d.ndim)    # 2     - 2-dimensional
```


## Indexing and Slicing

```python
a = np.array([10, 20, 30, 40])

print(a[1])       # 20
print(a[1:3])     # [20 30]
```

### 2D Indexing

```python
b = np.array([[1, 2, 3], [4, 5, 6]])

print(b[0, 1])    # 2
print(b[:, 1])    # [2 5] - all rows, column 1
```

## Array Operations

```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(x + y)      # [5 7 9]
print(x * y)      # [4 10 18]
```
