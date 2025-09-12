![Python Tinitiate Image](../python_tinitiate.png)

# Python Interview QnA
&copy; TINITIATE.COM

##### [Back To Contents](./README.md)

# Python Variables

## Q1. What is a variable in Python?
**Answer:**  
A variable is a named reference to a value stored in memory. It allows reusing and manipulating data.

## Q2. How do you declare and assign a variable?
**Answer:**  
Simply use the `=` operator.  
```python
x = 10
name = "Alice"
```

## Q3. Can you reassign a variable in Python?
**Answer:**  
Yes, variables are dynamically typed and can be reassigned to a different type.  
```python
x = 10
x = "hello"  # now x is a string
```

## Q4. How do you delete a variable?
**Answer:**  
Use the `del` statement.  
```python
x = 10
del x
```

## Q5. What are variable naming rules in Python?
**Answer:**  
- Must start with a letter or underscore.  
- Cannot start with a digit.  
- Can contain letters, digits, underscores.  
- Case-sensitive.  
- Cannot use reserved keywords.

## Q6. How do you check defined variables in the current scope?
**Answer:**  
Use `locals()` or `globals()`.  
```python
x = 5
print("x" in locals())  # True
```

## Q7. What is the difference between global and local variables?
**Answer:**  
- **Local variable**: Declared inside a function.  
- **Global variable**: Declared outside and accessible throughout the program.

## Q8. How do you access a global variable inside a function?
**Answer:**  
Use the `global` keyword.  
```python
x = 10
def change():
    global x
    x = 20
change()
print(x)  # 20
```

## Q9. What is the difference between `id()` and `type()` functions?
**Answer:**  
- `id()`: Returns memory address of object.  
- `type()`: Returns datatype of object.

## Q10. What is variable shadowing?
**Answer:**  
When a local variable has the same name as a global variable, it hides the global one within the function scope.

## Q11. How are variables stored in Python?
**Answer:**  
Variables are references to objects stored in memory. Python uses reference counting and garbage collection.

## Q12. What are constants in Python?
**Answer:**  
Python doesn’t have true constants, but by convention uppercase names are treated as constants.  
```python
PI = 3.14159
```

## Q13. Can variables point to functions?
**Answer:**  
Yes, functions are first-class objects.  
```python
def greet(): print("Hello")
f = greet
f()
```

## Q14. How do you check if a variable exists?
**Answer:**  
Use `in locals()` or `in globals()`.  
```python
if "x" in globals():
    print("x exists")
```

## Q15. What are reserved keywords in Python?
**Answer:**  
They are predefined identifiers like `for`, `if`, `class`. Check using `keyword` module.  
```python
import keyword
print(keyword.kwlist)
```

## Q16. What is dynamic typing in Python?
**Answer:**  
Variables don’t need explicit type declaration; type is assigned at runtime.

## Q17. How do you swap two variables?
**Answer:**  
Use tuple unpacking.  
```python
a, b = 10, 20
a, b = b, a
```

## Q18. Can variables reference other variables?
**Answer:**  
Yes, variables can hold references to the same object.  
```python
a = [1,2]
b = a
b.append(3)
print(a)  # [1,2,3]
```

## Q19. What are scope levels in Python?
**Answer:**  
LEGB rule: Local → Enclosing → Global → Built-in.

## Q20. What is the difference between `is` and `==` when comparing variables?
**Answer:**  
- `==`: Compares values.  
- `is`: Compares memory identity (object references).  
```python
x = [1,2]
y = [1,2]
print(x == y)  # True
print(x is y)  # False
```

##### [Back To Contents](./README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
