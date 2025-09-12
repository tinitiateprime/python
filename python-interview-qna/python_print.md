![Python Tinitiate Image](../python_tinitiate.png)

# Python Interview QnA
&copy; TINITIATE.COM

##### [Back To Contents](./README.md)

# Python Print

## Q1. What is the purpose of the `print()` function in Python?
**Answer:**  
The `print()` function outputs data to the standard output device (usually the console). It is primarily used for displaying messages, debugging, and presenting results.

## Q2. What are the default parameters of `print()`?
**Answer:**  
`print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`

- `sep`: Separator between objects (default = space).  
- `end`: String appended at the end (default = newline).  
- `file`: Output stream (default = `sys.stdout`).  
- `flush`: Boolean to force flushing.

## Q3. How do you print without a newline?
**Answer:**  
Use `end=''` in `print()`.  
```python
print("Hello", end="")
print("World")
# Output: HelloWorld
```

## Q4. How do you print with a custom separator?
**Answer:**  
Use the `sep` argument.  
```python
print("2025", "09", "12", sep="-")
# Output: 2025-09-12
```

## Q5. What is the difference between `print()` in Python 2 and Python 3?
**Answer:**  
- Python 2: `print` is a statement (`print "Hello"`).  
- Python 3: `print()` is a function requiring parentheses.

## Q6. How do you print using C-style formatting?
**Answer:**  
Use `%` formatting.  
```python
print("Name: %s, Age: %d" % ("Alice", 25))
```

## Q7. What is `.format()` in print statements?
**Answer:**  
It allows positional and keyword formatting.  
```python
print("Hello {}, you are {} years old".format("Bob", 30))
```

## Q8. What are f-strings in Python?
**Answer:**  
Introduced in Python 3.6, f-strings allow inline expression evaluation.  
```python
name, age = "Charlie", 22
print(f"{name} is {age} years old")
```

## Q9. How to print Unicode/emoji in Python?
**Answer:**  
Ensure encoding is UTF-8 and directly include characters.  
```python
print("Smiley: 😀")
```

## Q10. Can you redirect `print()` output to a file?
**Answer:**  
Yes, using `file` argument.  
```python
with open("output.txt", "w") as f:
    print("Hello File", file=f)
```

## Q11. What is `flush=True` in print()?
**Answer:**  
It forces the buffer to flush immediately, useful in real-time logging.

## Q12. How to suppress spaces between multiple print arguments?
**Answer:**  
Set `sep=''`.  
```python
print("Hello", "World", sep="")
# Output: HelloWorld
```

## Q13. How do you print formatted numbers?
**Answer:**  
Use formatting methods.  
```python
print("{:.2f}".format(3.14159))  # 3.14
print(f"{1234:,}")              # 1,234
```

## Q14. How to print raw strings with escape characters?
**Answer:**  
Prefix with `r`.  
```python
print(r"C:\Users\Name")
```

## Q15. How to print in multiple lines with one call?
**Answer:**  
Use triple quotes.  
```python
print("""Line1
Line2
Line3""")
```

## Q16. How do you combine `print()` with loops?
**Answer:**  
```python
for i in range(3):
    print("Iteration", i)
```

## Q17. What’s the difference between `repr()` and `str()` in print?
**Answer:**  
- `str()`: Human-readable form.  
- `repr()`: Debug/official form.  
```python
print(str("Hello"))   # Hello
print(repr("Hello"))  # 'Hello'
```

## Q18. How to print dynamically evaluated expressions?
**Answer:**  
Using f-strings or `eval()`.  
```python
x = 5
print(f"Square is {x*x}")
```

## Q19. How to print variables without spaces?
**Answer:**  
Concatenate using `+`.  
```python
a, b = "Py", "thon"
print(a + b)  # Python
```

## Q20. How do you print a progress bar or overwrite the same line?
**Answer:**  
Use carriage return `\r`.  
```python
import time
for i in range(5):
    print(f"Progress: {i}/5", end="\r")
    time.sleep(1)
```

##### [Back To Contents](./README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
