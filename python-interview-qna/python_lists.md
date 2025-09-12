![Python Tinitiate Image](../python_tinitiate.png)

# Python Interview QnA
&copy; TINITIATE.COM

##### [Back To Contents](./README.md)

# Python Lists

## Q1. What is a list in Python?
**Answer:**  
A list is a mutable, ordered collection of items that can store different datatypes.

## Q2. How do you create a list?
**Answer:**  
```python
lst = [1, 2, 3]
empty = []
mixed = [1, "hello", 3.14]
```

## Q3. How do you access elements in a list?
**Answer:**  
Use indexing.  
```python
lst = [10, 20, 30]
print(lst[0])   # 10
print(lst[-1])  # 30
```

## Q4. How do you access nested list elements?
**Answer:**  
```python
lst = [[1,2],[3,4]]
print(lst[1][0])  # 3
```

## Q5. How do you slice lists?
**Answer:**  
Use `[start:end:step]`.  
```python
lst = [1,2,3,4,5]
print(lst[1:4])  # [2,3,4]
print(lst[::-1]) # [5,4,3,2,1]
```

## Q6. How do you modify elements in a list?
**Answer:**  
Assign new values.  
```python
lst = [1,2,3]
lst[1] = 20
print(lst)  # [1,20,3]
```

## Q7. How do you add elements to a list?
**Answer:**  
- `append()` → adds one element  
- `extend()` → adds multiple elements  
- `insert()` → adds at specific index  
```python
lst = [1,2]
lst.append(3)
lst.extend([4,5])
lst.insert(1,10)
```

## Q8. How do you remove elements from a list?
**Answer:**  
- `remove(value)`  
- `pop(index)`  
- `del list[index]`  
- `clear()`  
```python
lst = [1,2,3,4]
lst.remove(2)
lst.pop()
del lst[0]
lst.clear()
```

## Q9. What is the difference between `append()` and `extend()`?
**Answer:**  
- `append()`: Adds a single object.  
- `extend()`: Iterates and adds elements.  
```python
a = [1,2]; a.append([3,4])  # [1,2,[3,4]]
b = [1,2]; b.extend([3,4])  # [1,2,3,4]
```

## Q10. How do you check if an element exists in a list?
**Answer:**  
Use `in`.  
```python
print(3 in [1,2,3])  # True
```

## Q11. How do you iterate over a list?
**Answer:**  
```python
for x in [1,2,3]:
    print(x)
```

## Q12. How do you sort a list?
**Answer:**  
- `sort()` (in-place)  
- `sorted()` (returns new list)  
```python
lst = [3,1,2]
lst.sort()
print(sorted([3,1,2]))
```

## Q13. How do you find min, max, and sum of a list?
**Answer:**  
```python
nums = [1,2,3,4]
print(min(nums))  # 1
print(max(nums))  # 4
print(sum(nums))  # 10
```

## Q14. How do you copy a list?
**Answer:**  
- Shallow: `copy()`, slicing  
- Deep: `copy.deepcopy()`  
```python
import copy
a = [1,[2,3]]
b = copy.deepcopy(a)
```

## Q15. How do you use list comprehensions?
**Answer:**  
```python
squares = [x*x for x in range(5)]
```

## Q16. What is the difference between shallow copy and deep copy?
**Answer:**  
- Shallow: Copies references of nested objects.  
- Deep: Creates independent nested objects.

## Q17. How do you find index of an element?
**Answer:**  
Use `index()`.  
```python
lst = ["a","b","c"]
print(lst.index("b"))  # 1
```

## Q18. How do you count occurrences of an element?
**Answer:**  
Use `count()`.  
```python
lst = [1,2,2,3]
print(lst.count(2))  # 2
```

## Q19. How do you reverse a list?
**Answer:**  
- `reverse()` method  
- slicing with `[::-1]`  
```python
lst = [1,2,3]
lst.reverse()
print(lst[::-1])
```

## Q20. What is the difference between `list()` and `[]`?
**Answer:**  
Both create lists, but `[]` is literal syntax and faster; `list()` is a constructor that can convert iterables.

##### [Back To Contents](./README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
