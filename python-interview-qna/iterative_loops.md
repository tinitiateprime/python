![Python Tinitiate Image](../python_tinitiate.png)

# Python Interview QnA
&copy; TINITIATE.COM

##### [Back To Contents](./README.md)

# Iterative Loops

## Q1. What are loops in Python?
**Answer:**  
Loops allow repeating a block of code multiple times until a condition is met.

## Q2. What are the two main types of loops in Python?
**Answer:**  
- `for` loop → iterates over a sequence.  
- `while` loop → runs while a condition is true.

## Q3. How does a `for` loop work?
**Answer:**  
Iterates over items in a sequence.  
```python
for x in [1,2,3]:
    print(x)
```

## Q4. How does a `while` loop work?
**Answer:**  
Runs until condition becomes false.  
```python
i = 0
while i < 3:
    print(i)
    i += 1
```

## Q5. What is the difference between `for` and `while` loops?
**Answer:**  
- `for` → when number of iterations is known.  
- `while` → when looping depends on a condition.

## Q6. Can loops be nested?
**Answer:**  
Yes, loops can be inside other loops.  
```python
for i in range(2):
    for j in range(2):
        print(i, j)
```

## Q7. How do you loop through a range of numbers?
**Answer:**  
Use `range()`.  
```python
for i in range(1,6):
    print(i)
```

## Q8. How do you loop through dictionary keys and values?
**Answer:**  
```python
d = {"a":1,"b":2}
for k,v in d.items():
    print(k, v)
```

## Q9. How do you loop with index in Python?
**Answer:**  
Use `enumerate()`.  
```python
for i, val in enumerate(["a","b"]):
    print(i, val)
```

## Q10. What is the use of `break` in loops?
**Answer:**  
Terminates the loop prematurely.

## Q11. What is the use of `continue` in loops?
**Answer:**  
Skips the current iteration and moves to next.

## Q12. What is the use of `pass` in loops?
**Answer:**  
Acts as a placeholder when no code is needed.

## Q13. How do you iterate over a string?
**Answer:**  
```python
for ch in "abc":
    print(ch)
```

## Q14. How do you use `else` with loops?
**Answer:**  
Executes when loop finishes normally (no `break`).  
```python
for i in range(3):
    print(i)
else:
    print("Done")
```

## Q15. How do infinite loops occur?
**Answer:**  
If condition never becomes false in a `while` loop.  
```python
while True:
    print("infinite")
```

## Q16. How to exit infinite loops safely?
**Answer:**  
Use `break` with a condition.

## Q17. How do you use list comprehensions as loops?
**Answer:**  
```python
squares = [x*x for x in range(5)]
```

## Q18. How do you iterate in reverse order?
**Answer:**  
Use `reversed()`.  
```python
for i in reversed([1,2,3]):
    print(i)
```

## Q19. How do you loop with steps other than 1?
**Answer:**  
Use `range(start,end,step)`.  
```python
for i in range(0,10,2):
    print(i)
```

## Q20. What are use cases of loops?
**Answer:**  
- Traversing collections  
- Repeating tasks  
- Searching/filtering data  
- Automating repetitive actions

##### [Back To Contents](./README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
