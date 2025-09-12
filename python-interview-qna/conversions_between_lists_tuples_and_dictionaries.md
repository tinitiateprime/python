![Python Tinitiate Image](../python_tinitiate.png)

# Python Interview QnA
&copy; TINITIATE.COM

##### [Back To Contents](./README.md)

# Conversions Between Lists, Tuples and Dictionaries

## Q1. How do you convert a list to a tuple?
**Answer:**  
Use the `tuple()` constructor.  
```python
lst = [1,2,3]
t = tuple(lst)  # (1,2,3)
```

## Q2. How do you convert a tuple to a list?
**Answer:**  
Use the `list()` constructor.  
```python
t = (1,2,3)
lst = list(t)  # [1,2,3]
```

## Q3. How do you convert a list of tuples into a dictionary?
**Answer:**  
Use `dict()`.  
```python
pairs = [("a",1),("b",2)]
d = dict(pairs)  # {"a":1,"b":2}
```

## Q4. How do you convert a dictionary into a list of tuples?
**Answer:**  
Use `items()`.  
```python
d = {"a":1,"b":2}
lst = list(d.items())  # [("a",1),("b",2)]
```

## Q5. How do you convert a dictionary into a list of keys?
**Answer:**  
Use `list(d.keys())`.

## Q6. How do you convert a dictionary into a list of values?
**Answer:**  
Use `list(d.values())`.

## Q7. How do you convert a list of dictionaries into a single dictionary?
**Answer:**  
By merging.  
```python
lst = [{"a":1},{"b":2}]
d = {k:v for dic in lst for k,v in dic.items()}
```

## Q8. How do you convert a tuple of lists into a dictionary?
**Answer:**  
Pair elements.  
```python
keys = ("a","b")
values = ([1,2],[3,4])
d = dict(zip(keys, values))
```

## Q9. How do you convert a tuple of tuples into a dictionary?
**Answer:**  
```python
t = (("a",1),("b",2))
d = dict(t)
```

## Q10. How do you convert a list of tuples into a tuple of lists?
**Answer:**  
Use `zip()`.  
```python
lst = [("a",1),("b",2)]
keys, vals = zip(*lst)
print(keys)  # ("a","b")
print(vals)  # (1,2)
```

## Q11. How do you convert a tuple of lists into a list of tuples?
**Answer:**  
Use `zip()`.  
```python
t = ([1,2],[3,4])
lst = list(zip(*t))  # [(1,3),(2,4)]
```

## Q12. How do you convert a dictionary into a tuple of lists?
**Answer:**  
```python
d = {"a":1,"b":2}
t = (list(d.keys()), list(d.values()))
```

## Q13. How do you convert a list of key-value pairs into a dictionary with duplicate keys?
**Answer:**  
Use `defaultdict(list)`.  
```python
from collections import defaultdict
pairs = [("a",1),("a",2)]
d = defaultdict(list)
for k,v in pairs: d[k].append(v)
```

## Q14. How do you flatten a list of tuples into a single list?
**Answer:**  
```python
lst = [(1,2),(3,4)]
flat = [x for tup in lst for x in tup]  # [1,2,3,4]
```

## Q15. How do you convert dictionary keys and values to separate lists?
**Answer:**  
```python
d = {"a":1,"b":2}
keys = list(d.keys())
values = list(d.values())
```

## Q16. How do you create a dictionary from two lists?
**Answer:**  
Use `zip()`.  
```python
keys = ["a","b"]
vals = [1,2]
d = dict(zip(keys, vals))
```

## Q17. How do you convert a dictionary into JSON-like string?
**Answer:**  
Use `json.dumps()`.  
```python
import json
d = {"a":1}
print(json.dumps(d))  # '{"a":1}'
```

## Q18. How do you convert a tuple to a string?
**Answer:**  
```python
t = (1,2,3)
s = str(t)  # "(1,2,3)"
```

## Q19. How do you convert a string representation of a list to an actual list?
**Answer:**  
Use `ast.literal_eval()`.  
```python
import ast
s = "[1,2,3]"
lst = ast.literal_eval(s)
```

## Q20. Why are conversions between lists, tuples, and dictionaries important?
**Answer:**  
They allow flexible data manipulation, integration with APIs, serialization, and adapting data structures for performance needs.

##### [Back To Contents](./README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
