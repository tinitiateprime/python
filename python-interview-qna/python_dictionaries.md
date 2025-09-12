![Python Tinitiate Image](../python_tinitiate.png)

# Python Interview QnA
&copy; TINITIATE.COM

##### [Back To Contents](./README.md)

# Python Dictionaries

## Q1. What is a dictionary in Python?
**Answer:**  
A dictionary is an unordered, mutable collection of key–value pairs.

## Q2. How do you create a dictionary?
**Answer:**  
```python
d1 = {"name": "Alice", "age": 25}
d2 = dict([("x", 1), ("y", 2)])
empty = {}
```

## Q3. What are valid dictionary keys?
**Answer:**  
Keys must be immutable and hashable types (e.g., strings, numbers, tuples).

## Q4. How do you access dictionary elements?
**Answer:**  
- `d[key]`  
- `get(key, default)`  
```python
d = {"a": 1, "b": 2}
print(d["a"])        # 1
print(d.get("c", 0)) # 0
```

## Q5. How do you modify dictionary values?
**Answer:**  
Assign to an existing key.  
```python
d = {"a":1}
d["a"] = 10
```

## Q6. How do you add new key–value pairs?
**Answer:**  
```python
d = {}
d["name"] = "Bob"
```

## Q7. How do you remove dictionary items?
**Answer:**  
- `pop(key)`  
- `popitem()` → removes last inserted item  
- `del d[key]`  
- `clear()` → removes all items

## Q8. How do you iterate over a dictionary?
**Answer:**  
```python
d = {"a":1,"b":2}
for k,v in d.items():
    print(k, v)
```

## Q9. What is the difference between `keys()`, `values()`, and `items()`?
**Answer:**  
- `keys()` → returns all keys  
- `values()` → returns all values  
- `items()` → returns key–value pairs

## Q10. Can dictionaries have duplicate keys?
**Answer:**  
No, assigning a duplicate key overwrites the previous value.

## Q11. What happens if you access a missing key?
**Answer:**  
- `d[key]` → raises `KeyError`  
- `d.get(key)` → returns `None` or default

## Q12. How do you merge two dictionaries?
**Answer:**  
- `update()` method  
- `{**d1, **d2}` unpacking  
```python
d1 = {"a":1}
d2 = {"b":2}
merged = {**d1, **d2}
```

## Q13. How do you copy a dictionary?
**Answer:**  
- Shallow: `copy()`  
- Deep: `copy.deepcopy()`

## Q14. How do you use dictionary comprehensions?
**Answer:**  
```python
squares = {x: x*x for x in range(5)}
```

## Q15. Are dictionaries ordered?
**Answer:**  
Since Python 3.7+, dictionaries maintain insertion order.

## Q16. Can dictionaries be nested?
**Answer:**  
Yes.  
```python
d = {"user": {"name":"Alice","age":25}}
```

## Q17. How do you check if a key exists?
**Answer:**  
Use `in`.  
```python
print("a" in {"a":1})  # True
```

## Q18. Can dictionary keys be mutable?
**Answer:**  
No, keys must be immutable. Lists and sets cannot be keys.

## Q19. What is `defaultdict`?
**Answer:**  
From `collections`, provides default values for missing keys.  
```python
from collections import defaultdict
d = defaultdict(int)
print(d["x"])  # 0
```

## Q20. What are common use cases of dictionaries?
**Answer:**  
- Storing structured data  
- Fast lookups (O(1) average)  
- Counting frequency of items  
- Caching and memoization

##### [Back To Contents](./README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
