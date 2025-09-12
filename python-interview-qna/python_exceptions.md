![Python Tinitiate Image](../python_tinitiate.png)

# Python Interview QnA
&copy; TINITIATE.COM

##### [Back To Contents](./README.md)

# Python Exceptions

## Q1. What is an exception in Python?
**Answer:**  
An exception is an error that occurs during program execution, which disrupts the normal flow of instructions.

## Q2. What is the difference between syntax errors and exceptions?
**Answer:**  
- Syntax errors → detected before execution (compile-time).  
- Exceptions → occur during execution (runtime).

## Q3. How do you handle exceptions in Python?
**Answer:**  
Using `try-except`.  
```python
try:
    x = 1/0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

## Q4. Can you handle multiple exceptions?
**Answer:**  
Yes, by specifying multiple `except` blocks.  
```python
try:
    x = int("abc")
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Divide by zero")
```

## Q5. How do you catch multiple exceptions in one line?
**Answer:**  
Use a tuple.  
```python
try:
    x = int("abc")
except (ValueError, TypeError):
    print("Error occurred")
```

## Q6. What is the use of `else` in exception handling?
**Answer:**  
The `else` block executes if no exception occurs.  
```python
try:
    x = 5/1
except ZeroDivisionError:
    print("Error")
else:
    print("No error")
```

## Q7. What is the use of `finally` in exception handling?
**Answer:**  
It executes regardless of whether an exception occurs, typically for cleanup.  
```python
try:
    f = open("file.txt")
except FileNotFoundError:
    print("Not found")
finally:
    print("Closing resources")
```

## Q8. How do you raise an exception manually?
**Answer:**  
Using `raise`.  
```python
raise ValueError("Invalid input")
```

## Q9. How do you create a custom exception?
**Answer:**  
Subclass `Exception`.  
```python
class MyError(Exception): pass
raise MyError("Something went wrong")
```

## Q10. What is the base class for all exceptions in Python?
**Answer:**  
`BaseException`

## Q11. What is the difference between `Exception` and `BaseException`?
**Answer:**  
- `BaseException` → root of all exceptions.  
- `Exception` → base for most user-defined/runtime exceptions (excluding `SystemExit`, `KeyboardInterrupt`, etc.).

## Q12. What is `StopIteration`?
**Answer:**  
Raised when `next()` is called on an exhausted iterator.

## Q13. What is `KeyboardInterrupt`?
**Answer:**  
Raised when user interrupts program execution (Ctrl+C).

## Q14. What is `SystemExit`?
**Answer:**  
Raised when `sys.exit()` is called to terminate a program.

## Q15. What is the difference between `assert` and `raise`?
**Answer:**  
- `assert` → checks condition and raises `AssertionError` if false.  
- `raise` → explicitly raises an exception.

## Q16. What is exception chaining?
**Answer:**  
When one exception is raised while handling another, indicated by `__cause__` or `__context__`.

## Q17. Can you re-raise the last exception?
**Answer:**  
Yes, using `raise` without arguments.  
```python
try:
    1/0
except:
    raise
```

## Q18. What is `try-except-else-finally` flow?
**Answer:**  
- `try`: run code  
- `except`: handle error  
- `else`: run if no error  
- `finally`: run always

## Q19. What is the difference between checked and unchecked exceptions in Python?
**Answer:**  
Python does not enforce checked exceptions (unlike Java). All exceptions are unchecked.

## Q20. What are best practices for exception handling?
**Answer:**  
- Catch specific exceptions  
- Avoid bare `except`  
- Use `finally` for cleanup  
- Use custom exceptions for clarity  
- Don’t suppress exceptions silently

##### [Back To Contents](./README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
