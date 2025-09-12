![Python Tinitiate Image](../python_tinitiate.png)

# Python Interview QnA
&copy; TINITIATE.COM

##### [Back To Contents](./README.md)

# OOP Built-ins

## Q1. What is the purpose of special (dunder) methods in Python?
**Answer:**  
They allow customization of class behavior, enabling operator overloading and built-in function support.

## Q2. What is the `__init__` method?
**Answer:**  
The constructor that initializes object attributes when a new instance is created.

## Q3. What is the `__del__` method?
**Answer:**  
The destructor, called when an object is about to be destroyed by garbage collection.  
```python
class Demo:
    def __del__(self): print("Object deleted")
```

## Q4. What is the difference between `__str__` and `__repr__`?
**Answer:**  
- `__str__`: User-friendly string representation.  
- `__repr__`: Official/developer representation.  
```python
class Demo:
    def __str__(self): return "str view"
    def __repr__(self): return "repr view"
```

## Q5. What is the `__sizeof__` method?
**Answer:**  
Returns the size of the object in memory (in bytes).  
```python
import sys
print(sys.getsizeof(10))
```

## Q6. What is the `__len__` method?
**Answer:**  
Defines behavior for `len()`.  
```python
class Box:
    def __len__(self): return 5
print(len(Box()))  # 5
```

## Q7. How does `__add__` work?
**Answer:**  
Overloads the `+` operator.  
```python
class Num:
    def __init__(self,x): self.x=x
    def __add__(self,other): return self.x+other.x
print(Num(2)+Num(3))  # 5
```

## Q8. What are `__getitem__` and `__setitem__`?
**Answer:**  
They allow indexing and assignment with `[]`.  
```python
class MyList:
    def __init__(self): self.data={}
    def __getitem__(self,k): return self.data[k]
    def __setitem__(self,k,v): self.data[k]=v
```

## Q9. What is the `__iter__` method?
**Answer:**  
Enables iteration using `for` loops by returning an iterator.

## Q10. What is the difference between `__class__`, `__base__`, and `__bases__`?
**Answer:**  
- `__class__`: Returns the class of an object.  
- `__base__`: First parent class.  
- `__bases__`: Tuple of all base classes.

## Q11. What is the `__dict__` attribute?
**Answer:**  
It stores an object’s writable attributes in a dictionary.

## Q12. What is the `__doc__` attribute?
**Answer:**  
Stores the class or function docstring.  
```python
class Demo:
    """This is a docstring"""
print(Demo.__doc__)
```

## Q13. How do `__eq__`, `__lt__`, and other comparison dunder methods work?
**Answer:**  
They allow operator overloading for `==`, `<`, `>`, etc.

## Q14. What is `__call__` used for?
**Answer:**  
Makes an object callable like a function.  
```python
class Demo:
    def __call__(self): print("Called!")
d=Demo(); d()
```

## Q15. What is `__contains__`?
**Answer:**  
Defines behavior for `in`.  
```python
class Demo:
    def __contains__(self,item): return item==42
print(42 in Demo())  # True
```

## Q16. What is `__enter__` and `__exit__` used for?
**Answer:**  
They define context manager behavior with `with`.  
```python
class Demo:
    def __enter__(self): print("Enter")
    def __exit__(self,a,b,c): print("Exit")
with Demo(): pass
```

## Q17. What is `__new__`?
**Answer:**  
Responsible for creating new instances before `__init__` is called.

## Q18. What is `__hash__`?
**Answer:**  
Defines hash value of an object (required for dictionary/set keys).

## Q19. What is `__bool__`?
**Answer:**  
Defines truthiness of an object when evaluated in conditions.  
```python
class Demo:
    def __bool__(self): return False
print(bool(Demo()))  # False
```

## Q20. Why are built-in methods important in OOP?
**Answer:**  
They provide hooks to integrate custom classes seamlessly with Python’s built-in operators, functions, and idioms.

##### [Back To Contents](./README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
