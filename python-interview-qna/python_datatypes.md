![Python Tinitiate Image](../python_tinitiate.png)

# Python Interview QnA
&copy; TINITIATE.COM

##### [Back To Contents](./README.md)

# Python Datatypes

## Q1. What are Python’s built-in data types?
**Answer:**  
Python provides built-in types such as:
- Numeric (int, float, complex)  
- Sequence (str, list, tuple)  
- Mapping (dict)  
- Set types (set, frozenset)  
- Boolean (bool)  
- None type (NoneType)

## Q2. What is the difference between `int`, `float`, and `complex`?
**Answer:**  
- `int`: Whole numbers (`10`)  
- `float`: Decimal numbers (`10.5`)  
- `complex`: Numbers with real + imaginary part (`3+5j`)

## Q3. How do you check the type of a variable?
**Answer:**  
Use `type()` function.  
```python
x = 10
print(type(x))  # <class 'int'>
```

## Q4. How do you convert between datatypes?
**Answer:**  
Use casting functions: `int()`, `float()`, `str()`, `list()`, etc.  
```python
print(int(3.7))     # 3
print(float("5"))   # 5.0
print(list("abc"))  # ['a','b','c']
```

## Q5. What is the difference between `list` and `tuple`?
**Answer:**  
- **List**: Mutable, ordered collection.  
- **Tuple**: Immutable, ordered collection.

## Q6. How do you create a dictionary?
**Answer:**  
```python
d = {"name": "Alice", "age": 25}
print(d["name"])  # Alice
```

## Q7. What is the difference between `set` and `frozenset`?
**Answer:**  
- `set`: Mutable and supports add/remove operations.  
- `frozenset`: Immutable, hashable, can be used as dict keys.

## Q8. What is the Boolean type in Python?
**Answer:**  
`bool` has only two values: `True` and `False`. It is a subclass of `int`.

## Q9. What is `None` in Python?
**Answer:**  
`None` represents the absence of a value. It is of type `NoneType`.

## Q10. How do you check if a variable is iterable?
**Answer:**  
Use `iter()` inside `try/except`.  
```python
try:
    iter([1,2,3])
    print("Iterable")
except TypeError:
    print("Not iterable")
```

## Q11. How do you test data type equality?
**Answer:**  
Use `isinstance()`.  
```python
print(isinstance(10, int))  # True
print(isinstance("abc", str))  # True
```

## Q12. What is the difference between mutable and immutable datatypes?
**Answer:**  
- Mutable: Can be changed after creation (`list`, `dict`, `set`).  
- Immutable: Cannot be changed (`int`, `str`, `tuple`, `frozenset`).

## Q13. How do you create a complex number?
**Answer:**  
Use `complex(real, imag)`.  
```python
z = complex(2, 3)
print(z)  # (2+3j)
```

## Q14. How does Python handle large integers?
**Answer:**  
Python automatically converts large integers into arbitrary-precision integers without overflow.

## Q15. What is the difference between `str()` and `repr()` for type conversion?
**Answer:**  
- `str()`: User-friendly output.  
- `repr()`: Developer/debugging representation.

## Q16. Can Python datatypes be nested?
**Answer:**  
Yes, datatypes can be nested.  
```python
data = {"user": ["Alice", "Bob"], "scores": (10, 20)}
```

## Q17. What happens if you compare different datatypes?
**Answer:**  
- Some types can be compared (`int` and `float`).  
- Others raise `TypeError` (`int` and `str`).

## Q18. How do you find the memory size of an object?
**Answer:**  
Use `sys.getsizeof()`.  
```python
import sys
print(sys.getsizeof(10))  # e.g., 28 bytes
```

## Q19. What are sequence datatypes?
**Answer:**  
They are ordered collections: `str`, `list`, `tuple`. They support indexing, slicing, iteration.

## Q20. How do you check if a key exists in a dictionary?
**Answer:**  
Use the `in` keyword.  
```python
d = {"a": 1, "b": 2}
print("a" in d)  # True
```

##### [Back To Contents](./README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
