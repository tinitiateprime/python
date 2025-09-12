![Python Tinitiate Image](../python_tinitiate.png)

# Python Interview QnA
&copy; TINITIATE.COM

##### [Back To Contents](./README.md)

# Python Tuples

## Q1. What is a tuple in Python?
**Answer:**  
A tuple is an ordered, immutable collection of items that can hold mixed datatypes.

## Q2. How do you create a tuple?
**Answer:**  
```python
t1 = (1,2,3)
t2 = tuple([4,5,6])
single = (5,)   # must include comma
```

## Q3. How do you access elements in a tuple?
**Answer:**  
Use indexing.  
```python
t = (10,20,30)
print(t[0])   # 10
print(t[-1])  # 30
```

## Q4. How do you access nested tuple elements?
**Answer:**  
```python
t = ((1,2),(3,4))
print(t[1][0])  # 3
```

## Q5. Can tuples be modified?
**Answer:**  
No, tuples are immutable. Items cannot be added, removed, or changed directly.

## Q6. How do you perform tuple packing and unpacking?
**Answer:**  
```python
t = 1, 2, 3   # packing
a, b, c = t   # unpacking
```

## Q7. How do you slice tuples?
**Answer:**  
```python
t = (1,2,3,4,5)
print(t[1:4])   # (2,3,4)
print(t[::-1])  # (5,4,3,2,1)
```

## Q8. What tuple methods are available?
**Answer:**  
- `count()` → occurrences of a value  
- `index()` → position of first occurrence

## Q9. How do you update or delete a tuple?
**Answer:**  
- Update: Not possible directly (immutable).  
- Delete: Entire tuple can be deleted with `del`.

## Q10. Can tuples contain mutable objects?
**Answer:**  
Yes, a tuple can store lists/dicts which are mutable.  
```python
t = (1,[2,3])
t[1].append(4)
print(t)  # (1, [2,3,4])
```

## Q11. How do you check membership in a tuple?
**Answer:**  
Use `in`.  
```python
print(2 in (1,2,3))  # True
```

## Q12. What is tuple comprehension?
**Answer:**  
There’s no direct tuple comprehension; `(x for x in range(5))` creates a generator. Use `tuple()` to convert.

## Q13. How do you concatenate tuples?
**Answer:**  
Use `+`.  
```python
print((1,2)+(3,4))  # (1,2,3,4)
```

## Q14. How do you repeat tuples?
**Answer:**  
Use `*`.  
```python
print((1,2)*3)  # (1,2,1,2,1,2)
```

## Q15. How do you find length of a tuple?
**Answer:**  
Use `len()`.  
```python
print(len((1,2,3)))  # 3
```

## Q16. Are tuples hashable?
**Answer:**  
Yes, if all elements are immutable. Hashable tuples can be used as dictionary keys.

## Q17. What is the performance benefit of tuples over lists?
**Answer:**  
Tuples are faster and use less memory since they are immutable.

## Q18. How do you convert between tuples and lists?
**Answer:**  
```python
t = (1,2,3)
lst = list(t)
back = tuple(lst)
```

## Q19. Can tuples be nested?
**Answer:**  
Yes, tuples can contain tuples.  
```python
t = ((1,2),(3,4))
```

## Q20. What are common use cases of tuples?
**Answer:**  
- Fixed collections (coordinates, config data)  
- Dictionary keys  
- Returning multiple values from a function

##### [Back To Contents](./README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
