![Python Tinitiate Image](../python_tinitiate.png)

# Python Interview QnA
&copy; TINITIATE.COM

##### [Back To Contents](./README.md)

# Python Sets

## Q1. What is a set in Python?
**Answer:**  
A set is an unordered, mutable collection of unique elements.

## Q2. How do you create a set?
**Answer:**  
```python
s1 = {1,2,3}
s2 = set([1,2,3])
empty = set()
```

## Q3. What happens if you create `{}` without `set()`?
**Answer:**  
It creates an empty dictionary, not a set. Use `set()` for empty sets.

## Q4. Can sets contain duplicate values?
**Answer:**  
No, duplicates are automatically removed.  
```python
s = {1,2,2,3}
print(s)  # {1,2,3}
```

## Q5. Are sets ordered?
**Answer:**  
No, sets are unordered and do not support indexing.

## Q6. How do you add elements to a set?
**Answer:**  
Use `add()` for single elements, `update()` for multiple.  
```python
s = {1,2}
s.add(3)
s.update([4,5])
```

## Q7. How do you remove elements from a set?
**Answer:**  
- `remove()` → KeyError if not found  
- `discard()` → Safe (no error)  
- `pop()` → Removes arbitrary element  
- `clear()` → Removes all elements

## Q8. How do you test set membership?
**Answer:**  
Use `in` / `not in`.  
```python
print(2 in {1,2,3})  # True
```

## Q9. How do you perform union of sets?
**Answer:**  
Use `|` or `union()`.  
```python
print({1,2}|{2,3})  # {1,2,3}
```

## Q10. How do you perform intersection of sets?
**Answer:**  
Use `&` or `intersection()`.  
```python
print({1,2,3}&{2,3,4})  # {2,3}
```

## Q11. How do you perform difference of sets?
**Answer:**  
Use `-` or `difference()`.  
```python
print({1,2,3}-{2})  # {1,3}
```

## Q12. How do you perform symmetric difference of sets?
**Answer:**  
Use `^` or `symmetric_difference()`.  
```python
print({1,2,3}^{2,3,4})  # {1,4}
```

## Q13. How do you check if one set is subset of another?
**Answer:**  
Use `issubset()`.  
```python
print({1,2}.issubset({1,2,3}))  # True
```

## Q14. How do you check if one set is superset of another?
**Answer:**  
Use `issuperset()`.  
```python
print({1,2,3}.issuperset({1,2}))  # True
```

## Q15. What is the difference between `remove()` and `discard()`?
**Answer:**  
- `remove()`: Raises error if element not found.  
- `discard()`: Does nothing if element not found.

## Q16. What are frozensets?
**Answer:**  
Immutable sets. They cannot be modified after creation but support all set operations.  
```python
fs = frozenset([1,2,3])
```

## Q17. Can sets contain mutable objects?
**Answer:**  
No, only immutable (hashable) objects are allowed (e.g., numbers, strings, tuples).

## Q18. How do you copy a set?
**Answer:**  
Use `copy()`.  
```python
s1 = {1,2,3}
s2 = s1.copy()
```

## Q19. How do you find length of a set?
**Answer:**  
Use `len()`.  
```python
print(len({1,2,3}))  # 3
```

## Q20. What are common use cases of sets?
**Answer:**  
- Removing duplicates from lists  
- Membership testing  
- Mathematical set operations  
- Fast lookups compared to lists

##### [Back To Contents](./README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
