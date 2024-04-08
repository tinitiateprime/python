![Python Tinitiate Image](../../python_tinitiate.png)
# Python Tutorial
&copy; TINITIATE.COM
##### [Back To Context](../../README.md)

# Python Operators
* Operators in Python are symbols that are used to perform operations on operands.
* Operands can be variables, constants, or expressions.

## Basic Operators In Python
* Python supports various types of operators.
### Arithmetic Operators
* Arithmetic operators are used to perform mathematical operations.
    * Addition: `+`
    * Subtraction: `-`
    * Multiplication: `*`
    * Division: `/`
    * Floor Division: `//` (returns the floor value of the division, The "floor value" refers to the largest integer less than or equal to a given number)
    * Modulus: `%` (returns the remainder of the division)
    * Power/Exponentiation: `**`
```python
a = 10
b = 3
# Addition
print(a + b)  # Output: 13

# Subtraction
print(a - b)  # Output: 7

# Multiplication
print(a * b)  # Output: 30

# Division
print(a / b)  # Output: 3.3333333333333335

# Floor Division
print(a // b) # Output: 3

# Modulus
print(a % b)  # Output: 1

# Power/Exponentiation
print(a ** b) # Output: 1000
```
### Comparison Operators
* Comparison operators are used to compare values. They return either `True` or `False`.
    * Equal to: `==`
    * Not equal to: `!=`
    * Greater than: `>`
    * Less than: `<`
    * Greater than or equal to: `>=`
    * Less than or equal to: `<=`
```python
x = 10
y = 5
# Equal to
print(x == y)  # Output: False

# Not equal to
print(x != y)  # Output: True

# Greater than
print(x > y)   # Output: True

# Less than
print(x < y)   # Output: False

# Greater than or equal to
print(x >= y)  # Output: True

# Less than or equal to
print(x <= y)  # Output: False
```
### Assignment Operators
* Assignment operators are used to assign values to variables.
    * Assignment: `=`
    * Addition assignment: `+=`
    * Subtraction assignment: `-=`
    * Multiplication assignment: `*=`
    * Division assignment: `/=`
    * Modulus assignment: `%=`
    * Floor Division assignment: `//=`
    * Exponentiation assignment: `**=`
```python
# Assignment
a = 10
print(a)  # Output: 10

# Addition assignment
a += 5    # Equivalent to a = a + 5
print(a)  # Output: 15

# Subtraction assignment
a -= 3    # Equivalent to a = a - 3
print(a)  # Output: 12

# Multiplication assignment
a *= 2    # Equivalent to a = a * 2
print(a)  # Output: 24

# Division assignment
a /= 4    # Equivalent to a = a / 4
print(a)  # Output: 6.0

# Modulus assignment
a %= 5    # Equivalent to a = a % 5
print(a)  # Output: 1.0

# Floor Division assignment
a //= 2   # Equivalent to a = a // 2
print(a)  # Output: 0.0

# Exponentiation assignment
a **= 3   # Equivalent to a = a ** 3
print(a)  # Output: 0.0 (0 to the power of 3 is still 0)
```
### Logical Operators
* Logical operators are used to combine conditional statements.
    * Logical AND: `and`
    * Logical OR: `or`
    * Logical NOT: `not`
```python
x = 5
y = 10
z = 15

# Logical AND
print(x < y and y < z)  # Output: True

# Logical OR
print(x < y or y > z)   # Output: True

# Logical NOT
print(not(x < y))       # Output: False
```
### Bitwise Operators
* Bitwise operators perform operations on binary representations of integers.
    * Bitwise AND: `&`
    * Bitwise OR: `|`
    * Bitwise XOR: `^`
    * Bitwise NOT: `~`
    * Left shift: `<<`
    * Right shift: `>>`
```python
a = 10
b = 4

# Bitwise AND
print(a & b)   # Output: 0

# Bitwise OR
print(a | b)   # Output: 14

# Bitwise XOR
print(a ^ b)   # Output: 14

# Bitwise NOT
print(~a)      # Output: -11

# Left shift
print(a << 1)  # Output: 20

# Right shift
print(a >> 1)  # Output: 5
```
### Identity Operators
* Identity operators are used to compare the memory locations of two objects.
    * `is`: Returns `True` if both variables point to the same object.
    * `is not`: Returns `True` if both variables point to different objects.
```python
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

# is
print(x is y)     # Output: False 
                  #(Different objects, even though they have the same values)
print(x is z)     # Output: True (Same object, assigned to z)

# is not
print(x is not y) # Output: True
```
### Membership Operators
* Membership operators are used to test if a sequence is present in an object.
    * `in`: Returns True if a sequence with the specified value is present in the object.
    * `not in`: Returns True if a sequence with the specified value is not present in the object.
```python
my_list = [1, 2, 3, 4, 5]

# in
print(3 in my_list)   # Output: True

# not in
print(6 not in my_list) # Output: True
```

##### [Back To Context](../../README.md)