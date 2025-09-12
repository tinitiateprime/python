![Python Tinitiate Image](../python_tinitiate.png)

# Python Interview QnA
&copy; TINITIATE.COM

##### [Back To Contents](./README.md)

# 100 Python Interview Questions & Answers

## Q1. What are the main features of Python?
**Answer:**  
- Interpreted  
- High-level  
- Dynamically typed  
- Object-Oriented  
- Large standard library

## Q2. What is PEP 8?
**Answer:**  
PEP 8 is Python’s official style guide, providing conventions for writing readable code.

## Q3. How is Python interpreted?
**Answer:**  
Python code is compiled into bytecode, then executed by the Python Virtual Machine (PVM).

## Q4. What are Python data types?
**Answer:**  
`int`, `float`, `complex`, `str`, `list`, `tuple`, `dict`, `set`, `frozenset`, `bool`, `NoneType`.

## Q5. What is the difference between `is` and `==`?
**Answer:**  
- `is` → checks identity (same object in memory).  
- `==` → checks equality of values.

## Q6. How do you check Python version?
**Answer:**  
```bash
python --version
```

## Q7. What is Python’s GIL?
**Answer:**  
The Global Interpreter Lock ensures only one thread executes Python bytecode at a time, limiting multi-threaded CPU-bound tasks.

## Q8. What are Python namespaces?
**Answer:**  
Namespaces map names to objects. Types: local, enclosing, global, built-in (LEGB).

## Q9. What are Python scopes?
**Answer:**  
The part of a program where a variable is accessible. Follows the LEGB rule.

## Q10. What are Python decorators?
**Answer:**  
Functions that modify the behavior of other functions or methods. Defined with `@`.

## Q11. What is a lambda function?
**Answer:**  
An anonymous, single-expression function.  
```python
f = lambda x: x*x
```

## Q12. What are Python iterators?
**Answer:**  
Objects with `__iter__()` and `__next__()`. Used in loops.

## Q13. What are Python generators?
**Answer:**  
Functions using `yield` to produce values lazily, pausing and resuming execution.

## Q14. What is the difference between `deepcopy` and `copy`?
**Answer:**  
- `copy()` → shallow copy (references nested objects).  
- `deepcopy()` → completely independent copy.

## Q15. What is the difference between list and tuple?
**Answer:**  
- List → mutable.  
- Tuple → immutable.

## Q16. How do you remove duplicates from a list?
**Answer:**  
Convert to a set: `list(set(mylist))`.

## Q17. What is monkey patching in Python?
**Answer:**  
Dynamically modifying a class or module at runtime.

## Q18. What is duck typing?
**Answer:**  
Python focuses on object behavior, not type. “If it walks like a duck and quacks like a duck, it’s a duck.”

## Q19. What is Python’s `__str__` vs `__repr__`?
**Answer:**  
- `__str__` → user-friendly string.  
- `__repr__` → developer/debugging representation.

## Q20. What is Python’s `with` statement?
**Answer:**  
Context manager for resource management. Calls `__enter__` and `__exit__`.

## Q21. How do you handle exceptions?
**Answer:**  
Using `try-except` blocks.

## Q22. What is `finally` used for?
**Answer:**  
Executes regardless of exception (used for cleanup).

## Q23. How do you raise an exception?
**Answer:**  
```python
raise ValueError("Invalid value")
```

## Q24. How do you define custom exceptions?
**Answer:**  
Subclass `Exception`.

## Q25. What is Python OOP?
**Answer:**  
A paradigm that models code as objects with attributes and methods.

## Q26. What is inheritance?
**Answer:**  
Mechanism where one class derives from another.

## Q27. What is multiple inheritance?
**Answer:**  
A class inheriting from more than one base class.

## Q28. What is method overriding?
**Answer:**  
A child class providing its own implementation of a parent method.

## Q29. What is polymorphism?
**Answer:**  
Different classes implementing the same interface or method in different ways.

## Q30. What is encapsulation?
**Answer:**  
Restricting access to data (e.g., using private variables `__var`).

## Q31. What is Python’s `super()`?
**Answer:**  
Used to call parent class methods.

## Q32. What is method resolution order (MRO)?
**Answer:**  
The order Python searches for methods/attributes in inheritance. Checked with `.mro()`.

## Q33. What are static methods?
**Answer:**  
Methods not bound to instance or class, defined with `@staticmethod`.

## Q34. What are class methods?
**Answer:**  
Methods bound to the class, take `cls` as first parameter. Declared with `@classmethod`.

## Q35. What is the difference between Python2 and Python3?
**Answer:**  
- Python3 → print is a function, Unicode by default, better division handling.  
- Python2 → print statement, ASCII default, legacy support.

## Q36. What are Python virtual environments?
**Answer:**  
Isolated environments for dependencies using `venv`.

## Q37. How do you create a virtual environment?
**Answer:**  
```bash
python -m venv myenv
```

## Q38. What are Python data structures?
**Answer:**  
List, Tuple, Set, Dictionary.

## Q39. How do you merge two dictionaries?
**Answer:**  
```python
d1={"a":1}; d2={"b":2}
merged={**d1,**d2}
```

## Q40. How do you sort a dictionary by keys?
**Answer:**  
```python
dict(sorted(my_dict.items()))
```

## Q41. How do you sort a dictionary by values?
**Answer:**  
```python
dict(sorted(my_dict.items(), key=lambda x:x[1]))
```

## Q42. How do you reverse a list?
**Answer:**  
`list[::-1]` or `list.reverse()`.

## Q43. How do you check memory size of an object?
**Answer:**  
Use `sys.getsizeof()`.

## Q44. How do you swap two variables?
**Answer:**  
`a,b = b,a`

## Q45. What is slicing in Python?
**Answer:**  
Extracting subsequences from sequences: `seq[start:end:step]`.

## Q46. What are Python comprehensions?
**Answer:**  
Concise ways to create collections: list, dict, set comprehensions.

## Q47. What are Python closures?
**Answer:**  
Functions that capture variables from enclosing scopes.

## Q48. What are Python’s `*args` and `**kwargs`?
**Answer:**  
- `*args` → variable-length positional arguments.  
- `**kwargs` → variable-length keyword arguments.

## Q49. What is Python’s `zip()`?
**Answer:**  
Pairs elements from multiple iterables.

## Q50. What is Python’s `enumerate()`?
**Answer:**  
Returns index and element while looping.

## Q51. What is the difference between `map`, `filter`, and `reduce`?
**Answer:**  
- `map()` → applies function to all items.  
- `filter()` → selects items by condition.  
- `reduce()` → aggregates to a single value.

## Q52. What is Python’s `any()` and `all()`?
**Answer:**  
- `any()` → True if any element is True.  
- `all()` → True if all elements are True.

## Q53. What is Python’s `id()`?
**Answer:**  
Returns memory address of object.

## Q54. What are Python built-in data conversion functions?
**Answer:**  
`int()`, `float()`, `str()`, `list()`, `tuple()`, `dict()`, `set()`.

## Q55. How do you handle JSON in Python?
**Answer:**  
Using the `json` module.

## Q56. How do you open a file in Python?
**Answer:**  
```python
f = open("file.txt","r")
```

## Q57. What is the difference between `read()`, `readline()`, and `readlines()`?
**Answer:**  
- `read()` → entire file.  
- `readline()` → one line.  
- `readlines()` → list of all lines.

## Q58. What are Python file modes?
**Answer:**  
`r`, `w`, `a`, `rb`, `wb`, etc.

## Q59. How do you use `with open`?
**Answer:**  
Ensures automatic closing of files.

## Q60. How do you check if a file exists?
**Answer:**  
Use `os.path.exists()`.

## Q61. How do you delete a file?
**Answer:**  
Use `os.remove()`.

## Q62. How do you list files in a directory?
**Answer:**  
Use `os.listdir()`.

## Q63. What is the difference between `os` and `sys` modules?
**Answer:**  
- `os` → interacts with operating system.  
- `sys` → interacts with Python runtime.

## Q64. What is Python’s `subprocess` module?
**Answer:**  
Used to run external commands.

## Q65. What is the difference between `append()` and `extend()` for lists?
**Answer:**  
- `append()` → adds single item.  
- `extend()` → adds multiple items.

## Q66. What is Python’s `collections.Counter`?
**Answer:**  
A dict subclass for counting hashable objects.

## Q67. What is Python’s `defaultdict`?
**Answer:**  
Provides default values for missing keys.

## Q68. What is Python’s `OrderedDict`?
**Answer:**  
Dict that remembers insertion order (pre-Python 3.7).

## Q69. What is Python’s `namedtuple`?
**Answer:**  
Tuple subclass with named fields.

## Q70. What is Python’s `deque`?
**Answer:**  
Double-ended queue supporting fast appends/pops.

## Q71. What is the difference between `threading` and `multiprocessing`?
**Answer:**  
- `threading` → multiple threads in same memory space.  
- `multiprocessing` → multiple processes with separate memory.

## Q72. What is the difference between synchronous and asynchronous code?
**Answer:**  
- Sync → tasks run sequentially.  
- Async → tasks can run concurrently using `async/await`.

## Q73. What is Python’s `asyncio`?
**Answer:**  
A library for asynchronous programming using coroutines.

## Q74. What is the difference between `deepcopy` and assignment?
**Answer:**  
- Assignment → points to same object.  
- Deepcopy → creates a new independent object.

## Q75. How do you serialize objects in Python?
**Answer:**  
Using `pickle` or `json`.

## Q76. What is Python’s `logging` module?
**Answer:**  
Used to record logs for debugging and monitoring.

## Q77. What are Python metaclasses?
**Answer:**  
Classes of classes; define behavior of class creation.

## Q78. What is `__slots__` used for?
**Answer:**  
Restricts dynamic creation of attributes, saving memory.

## Q79. What is the difference between `@staticmethod` and `@classmethod`?
**Answer:**  
- `staticmethod` → no access to class or instance.  
- `classmethod` → access to class via `cls`.

## Q80. What is `property()` used for?
**Answer:**  
Used to create managed attributes (getters/setters).

## Q81. What are Python f-strings?
**Answer:**  
String literals with embedded expressions prefixed by `f`.

## Q82. How do you reverse a string?
**Answer:**  
`s[::-1]`

## Q83. How do you check if a string is palindrome?
**Answer:**  
`s == s[::-1]`

## Q84. How do you count words in a string?
**Answer:**  
```python
len(s.split())
```

## Q85. How do you find substrings?
**Answer:**  
Use `in`, `find()`, or `index()`.

## Q86. What is regex in Python?
**Answer:**  
Regular expressions, handled with `re` module.

## Q87. How do you match a pattern with regex?
**Answer:**  
```python
import re
re.match(r"\d+","123")
```

## Q88. What are Python docstrings?
**Answer:**  
String literals used for documentation inside functions, classes, or modules.

## Q89. How do you check object type?
**Answer:**  
Use `type()` or `isinstance()`.

## Q90. What is Python’s `help()`?
**Answer:**  
Interactive help utility to see documentation.

## Q91. What are Python unit tests?
**Answer:**  
Automated tests using the `unittest` module.

## Q92. What is pytest?
**Answer:**  
A popular third-party testing framework.

## Q93. What is Python’s `argparse`?
**Answer:**  
Library for parsing command-line arguments.

## Q94. How do you connect to a database in Python?
**Answer:**  
Using connectors like `sqlite3`, `psycopg2`, `pyodbc`.

## Q95. What is Python’s `requests` library?
**Answer:**  
A library for sending HTTP requests.

## Q96. How do you send a GET request using `requests`?
**Answer:**  
```python
import requests
r = requests.get("https://api.github.com")
```

## Q97. What is Python’s `pandas` library used for?
**Answer:**  
For data analysis and manipulation.

## Q98. How do you create a DataFrame in pandas?
**Answer:**  
```python
import pandas as pd
df = pd.DataFrame({"a":[1,2],"b":[3,4]})
```

## Q99. What is Python’s `numpy` library used for?
**Answer:**  
For numerical computing, arrays, and linear algebra.

## Q100. What is the use of Python in real-world applications?
**Answer:**  
- Web development  
- Data science  
- AI/ML  
- Automation/Scripting  
- Game development  
- Scientific computing

##### [Back To Contents](./README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
