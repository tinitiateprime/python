![Python Tinitiate Image](../python_tinitiate.png)

# Python Interview QnA
&copy; TINITIATE.COM

##### [Back To Contents](./README.md)

# Python Strings

## Q1. What is a string in Python?
**Answer:**  
A string is a sequence of Unicode characters enclosed in single quotes, double quotes, or triple quotes.

## Q2. How do you create strings in Python?
**Answer:**  
```python
s1 = 'hello'
s2 = "world"
s3 = '''multi
line'''
```

## Q3. How do you access characters in a string?
**Answer:**  
Use indexing.  
```python
s = "Python"
print(s[0])   # P
print(s[-1])  # n
```

## Q4. How do you slice strings?
**Answer:**  
Use `[start:end:step]`.  
```python
s = "Python"
print(s[0:4])   # Pyth
print(s[::-1])  # nohtyP
```

## Q5. Are strings mutable in Python?
**Answer:**  
No, strings are immutable. Any modification creates a new string.

## Q6. How do you concatenate strings?
**Answer:**  
Use `+` or `join()`.  
```python
a, b = "Hello", "World"
print(a + " " + b)  
print(" ".join([a, b]))
```

## Q7. What are some common string methods?
**Answer:**  
- Case conversion: `upper()`, `lower()`, `title()`.  
- Stripping: `strip()`, `lstrip()`, `rstrip()`.  
- Searching: `find()`, `index()`, `count()`.  
- Checking: `isdigit()`, `isalpha()`, `startswith()`, `endswith()`.

## Q8. What is the difference between `find()` and `index()`?
**Answer:**  
- `find()`: Returns `-1` if not found.  
- `index()`: Raises `ValueError` if not found.

## Q9. How do you check if a substring exists in a string?
**Answer:**  
Use `in`.  
```python
print("Py" in "Python")  # True
```

## Q10. How do you format strings?
**Answer:**  
- `format()`  
- f-strings  
- `%` formatting  
```python
name, age = "Alice", 25
print(f"{name} is {age} years old")
```

## Q11. How do you repeat a string?
**Answer:**  
Use `*` operator.  
```python
print("Hi" * 3)  # HiHiHi
```

## Q12. How to split and join strings?
**Answer:**  
```python
s = "a,b,c"
parts = s.split(",")  # ['a','b','c']
print("-".join(parts))  # a-b-c
```

## Q13. How do you remove whitespace from a string?
**Answer:**  
Use `strip()`.  
```python
print("  hello  ".strip())  # hello
```

## Q14. What is the difference between `isalpha()`, `isdigit()`, `isalnum()`?
**Answer:**  
- `isalpha()`: Only letters.  
- `isdigit()`: Only digits.  
- `isalnum()`: Letters + digits.

## Q15. How do you replace substrings?
**Answer:**  
Use `replace()`.  
```python
s = "I like Java"
print(s.replace("Java", "Python"))
```

## Q16. How do you check string length?
**Answer:**  
Use `len()`.  
```python
print(len("Python"))  # 6
```

## Q17. How do you escape special characters in strings?
**Answer:**  
Use `\`.  
```python
print("He said \"Hello\"")
```

## Q18. How do raw strings work?
**Answer:**  
Prefix with `r` to ignore escape sequences.  
```python
print(r"C:\newfolder\test")
```

## Q19. What is string interning?
**Answer:**  
Python reuses immutable string objects with the same content to save memory.  
```python
a = "hello"
b = "hello"
print(a is b)  # True
```

## Q20. How do you encode and decode strings?
**Answer:**  
Use `.encode()` and `.decode()`.  
```python
s = "hello"
b = s.encode("utf-8")
print(b)           # b'hello'
print(b.decode())  # hello
```

##### [Back To Contents](./README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
