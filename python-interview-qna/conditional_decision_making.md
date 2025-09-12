![Python Tinitiate Image](../python_tinitiate.png)

# Python Interview QnA
&copy; TINITIATE.COM

##### [Back To Contents](./README.md)

# Conditional Decision Making

## Q1. What is conditional decision making in Python?
**Answer:**  
It is the process of executing different blocks of code based on conditions using statements like `if`, `if-else`, `if-elif-else`, etc.

## Q2. What is the syntax of a simple `if` statement?
**Answer:**  
```python
x = 10
if x > 5:
    print("x is greater than 5")
```

## Q3. How does an `if-else` statement work?
**Answer:**  
If the condition is true, `if` block executes, otherwise `else` block.  
```python
x = 3
if x % 2 == 0:
    print("Even")
else:
    print("Odd")
```

## Q4. How does `if-elif-else` work?
**Answer:**  
Used for multiple conditions.  
```python
score = 75
if score >= 90: print("A")
elif score >= 75: print("B")
else: print("C")
```

## Q5. Can `if` statements be nested?
**Answer:**  
Yes.  
```python
x = 10
if x > 0:
    if x % 2 == 0:
        print("Positive Even")
```

## Q6. What is shorthand `if`?
**Answer:**  
Single-line conditional.  
```python
x = 10
if x > 5: print("Greater than 5")
```

## Q7. What is shorthand `if-else` (ternary operator)?
**Answer:**  
```python
x = 10
msg = "Even" if x % 2 == 0 else "Odd"
print(msg)
```

## Q8. Can logical operators be used inside `if`?
**Answer:**  
Yes.  
```python
x, y = 5, 10
if x > 0 and y > 0:
    print("Both positive")
```

## Q9. What is the difference between `=` and `==` in conditions?
**Answer:**  
- `=` → assignment  
- `==` → equality check

## Q10. What happens if condition is not a boolean?
**Answer:**  
Python evaluates its truthiness (e.g., non-empty string = True, `0` = False).  
```python
if "abc": print("True")  # Executes
```

## Q11. Can `if` be used without `else`?
**Answer:**  
Yes, `else` is optional.

## Q12. Can `elif` be used without `else`?
**Answer:**  
Yes, `elif` can follow `if` without `else`.

## Q13. What is the difference between `elif` and nested `if`?
**Answer:**  
- `elif`: Part of the same decision chain.  
- Nested `if`: Inner condition inside outer `if`.

## Q14. Can conditions check membership?
**Answer:**  
Yes, using `in`.  
```python
if "a" in ["a","b","c"]:
    print("Found")
```

## Q15. Can conditions check identity?
**Answer:**  
Yes, using `is`.  
```python
x = None
if x is None: print("x is None")
```

## Q16. How to combine multiple conditions?
**Answer:**  
Use `and`, `or`, `not`.

## Q17. What happens if multiple conditions are true in `if-elif-else`?
**Answer:**  
Only the first true block executes.

## Q18. Can you use functions in conditions?
**Answer:**  
Yes.  
```python
def is_even(n): return n%2==0
if is_even(4): print("Even")
```

## Q19. Can conditions evaluate expressions?
**Answer:**  
Yes.  
```python
if (5+3)*2 > 10:
    print("Yes")
```

## Q20. What are use cases of conditional statements?
**Answer:**  
- Decision making  
- Validations  
- Data filtering  
- Control program flow

##### [Back To Contents](./README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
