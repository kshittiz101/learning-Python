# **Python List – Complete Notes**

## 1. Introduction

A **list** in Python is an **ordered, mutable (changeable)** collection that can hold **heterogeneous data types** (integers, strings, floats, etc.).
Lists are one of the most commonly used **sequence data structures** in Python.

**Syntax:**

```python
my_list = [1, 2, 3, "Hello", 4.5]
```

---

## 2. Characteristics of Lists

| Feature       | Description                             |
| ------------- | --------------------------------------- |
| Ordered       | Maintains the order of elements         |
| Mutable       | Elements can be changed after creation  |
| Heterogeneous | Can store different data types          |
| Index-based   | Access elements using indices (0-based) |
| Dynamic       | Can grow or shrink in size              |

---

## 3. Creating Lists

```python
# Empty list
a = []

# With elements
b = [1, 2, 3, 4]

# Using list() constructor
c = list((10, 20, 30))

# Nested list
d = [[1, 2], [3, 4]]
```

---

## 4. Accessing Elements

```python
nums = [10, 20, 30, 40, 50]

# Positive index
print(nums[0])   # 10

# Negative index
print(nums[-1])  # 50

# Nested access
nested = [[1, 2], [3, 4]]
print(nested[1][0])  # 3
```

---

## 5. List Slicing

```python
data = [0, 1, 2, 3, 4, 5, 6]

print(data[1:5])   # [1,2,3,4]
print(data[:4])    # [0,1,2,3]
print(data[3:])    # [3,4,5,6]
print(data[::2])   # [0,2,4,6]
print(data[::-1])  # [6,5,4,3,2,1,0]
```

---

## 6. Modifying Lists

```python
nums = [1, 2, 3]
nums[1] = 10           # Replace element
nums.append(4)         # Add at end
nums.insert(1, 5)      # Insert at position
nums.extend([6, 7])    # Add multiple
nums.remove(10)        # Remove by value
nums.pop(2)            # Remove by index
nums.clear()           # Remove all
```

---

## 7. Iterating Through Lists

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

Or with **index:**
The enumerate() function in Python is a built-in function that adds a counter to an iterable and returns it as an enumerate object. This object can then be used in loops to access both the index (or count) and the value of each item in the iterable simultaneously. 

```python
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

---

## 8. List Comprehension (Pythonic Way)

A concise way to create lists.

```python
# Squares of numbers
squares = [x**2 for x in range(5)]  # [0,1,4,9,16]

# Even numbers
evens = [x for x in range(10) if x % 2 == 0]
```

---

## 9. Useful List Methods

| Method             | Description             | Example                       |
| ------------------ | ----------------------- | ----------------------------- |
| `append(x)`        | Adds element at end     | `[1,2].append(3)` → `[1,2,3]` |
| `extend(iterable)` | Adds multiple elements  | `[1].extend([2,3])`           |
| `insert(i, x)`     | Insert at index         | `[1,2].insert(1,5)`           |
| `remove(x)`        | Remove by value         | `[1,2,3].remove(2)`           |
| `pop(i)`           | Remove & return element | `[1,2,3].pop(1)` → `2`        |
| `clear()`          | Removes all items       | `[1,2].clear()`               |
| `sort()`           | Sort ascending          | `[3,1,2].sort()`              |
| `reverse()`        | Reverse list            | `[1,2,3].reverse()`           |
| `count(x)`         | Count occurrences       | `[1,1,2].count(1)`            |
| `index(x)`         | Get index of element    | `[10,20,30].index(20)`        |
| `copy()`           | Shallow copy            | `new = old.copy()`            |

---

## 10. List Operations

```python
a = [1, 2, 3]
b = [4, 5]

print(a + b)       # Concatenation → [1,2,3,4,5]
print(a * 2)       # Repetition → [1,2,3,1,2,3]
print(3 in a)      # Membership → True
print(len(a))      # Length → 3
```

---

## 11. Nested Lists and 2D Lists

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
]

print(matrix[1][2])  # 6

# Flatten using comprehension
flat = [num for row in matrix for num in row]
```

---

## 12. Copying Lists

```python
a = [1, 2, 3]
b = a               # same reference
c = a.copy()        # shallow copy
d = a[:]            # slicing copy
```

---

## 13. Built-in Functions with Lists

| Function         | Description           |
| ---------------- | --------------------- |
| `len(list)`      | Returns length        |
| `sum(list)`      | Sum of elements       |
| `max(list)`      | Maximum value         |
| `min(list)`      | Minimum value         |
| `sorted(list)`   | Returns a sorted copy |
| `list(iterable)` | Converts to list      |

---

## 14. Example Program

```python
# Filter odd numbers and square them
numbers = [1, 2, 3, 4, 5, 6]
result = [n**2 for n in numbers if n % 2 != 0]
print(result)  # [1, 9, 25]
```

---

## 15. Summary

* Lists are ordered, mutable, and dynamic.
* Support slicing and nesting.
* Offer a wide range of methods and operations.
* Essential for most Python data handling tasks.

---
