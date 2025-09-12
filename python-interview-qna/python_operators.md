![Python Tinitiate Image](../python_tinitiate.png)

# Python Interview QnA
&copy; TINITIATE.COM

##### [Back To Contents](./README.md)

# Python Operators

## Q1. What are operators in Python?
**Answer:**  
Operators are special symbols or keywords used to perform operations on variables and values (e.g., `+`, `-`, `*`, `and`, `is`).

## Q2. What are the categories of operators in Python?
**Answer:**  
- Arithmetic  
- Comparison  
- Assignment  
- Logical  
- Bitwise  
- Identity  
- Membership

## Q3. What are arithmetic operators in Python?
**Answer:**  
Used for mathematical operations:  
- `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division),  
- `%` (modulus), `**` (power), `//` (floor division).

## Q4. What is the difference between `/` and `//`?
**Answer:**  
- `/`: Floating-point division.  
- `//`: Floor division (truncates result).  
!```python
print(5/2)   # 2.5
print(5//2)  # 2
!```

## Q5. What is the modulus operator used for?
**Answer:**  
It returns the remainder of division.  
!```python
print(10 % 3)  # 1
!```

## Q6. What is the difference between `==` and `is`?
**Answer:**  
- `==`: Compares values.  
- `is`: Compares object identity (memory address).  
!```python
a = [1,2]; b = [1,2]
print(a == b)  # True
print(a is b)  # False
!```

## Q7. What are comparison operators?
**Answer:**  
They compare values:  
- `==`, `!=`, `<`, `>`, `<=`, `>=`

## Q8. What are assignment operators?
**Answer:**  
Used to assign values with shorthand:  
- `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `**=`, `%=`

## Q9. How do logical operators work in Python?
**Answer:**  
- `and` → True if both conditions are True  
- `or` → True if at least one is True  
- `not` → Negates the condition

## Q10. What is short-circuit evaluation in logical operators?
**Answer:**  
Python stops evaluating if the result is already determined.  
!```python
print(False and print("hi"))  # Does not print "hi"
!```

## Q11. What are bitwise operators in Python?
**Answer:**  
Work on binary representations:  
- `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (left shift), `>>` (right shift).

## Q12. What is the difference between `&` and `and`?
**Answer:**  
- `&`: Bitwise operator, works on bits.  
- `and`: Logical operator, works on boolean expressions.

## Q13. What are identity operators?
**Answer:**  
- `is`: Checks if two variables point to same object.  
- `is not`: Opposite of `is`.

## Q14. What are membership operators?
**Answer:**  
- `in`: Returns True if element is in a sequence.  
- `not in`: Returns True if element is not in sequence.  
!```python
print(2 in [1,2,3])  # True
!```

## Q15. What is operator precedence in Python?
**Answer:**  
It defines the order in which operators are evaluated (e.g., `**` > `*` > `+`).

## Q16. How can you override operators in Python?
**Answer:**  
By defining special methods in classes (`__add__`, `__eq__`, etc.).  
!```python
class Num:
    def __init__(self,v): self.v=v
    def __add__(self,o): return self.v + o.v
print(Num(2)+Num(3))  # 5
!```

## Q17. What does the `~` operator do?
**Answer:**  
Bitwise NOT: flips bits. Equivalent to `-(x+1)`.  
!```python
print(~5)  # -6
!```

## Q18. How does Python evaluate chained comparisons?
**Answer:**  
They are evaluated as logical AND.  
!```python
print(1 < 2 < 3)   # True
print(1 < 2 > 3)   # False
!```

## Q19. What is the difference between `+=` and `=+`?
**Answer:**  
- `+=`: Increment operator.  
- `=+`: Assigns a positive value.  
!```python
x = 5; x += 2  # 7
y = 5; y =+ 2  # 2
!```

## Q20. How do you check precedence of operators?
**Answer:**  
Use `help("operator precedence")` or refer to documentation. Parentheses can override precedence.

##### [Back To Contents](./README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
