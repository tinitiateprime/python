![Python Tinitiate Image](../../python_tinitiate.png)
# Python Tutorial
&copy; TINITIATE.COM
##### [Back To Context](../../README.md)

# Conditional Decision-Making In Python
* Conditional decision-making in Python refers to the process of making choices in your code based on certain conditions.
* It allows your program to execute different code blocks depending on whether specific conditions are satisfied or not.
* Conditional decision-making in Python is achieved using conditional statements, primarily the `if`, `elif` (else if), and `else` statements. 
* For these statements code blocks should be indented.

## The if Statement
* The `if` statement is used to execute a block of code only if a specified condition is true.
```python
x = 10

if x > 5:
    print("x is greater than 5")
    # Observe the indentation (blankspace before each line)
    # This indentation represents the code belongs to the above if statement
# This line is out of the if statement code block
# Output: x is greater than 5
```

## The if-else Statement
* The `if-else` statement allows you to execute one block of code if a condition is true and another block if the condition is false.
```python
# Example 1:
x = 4

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
# Output: x is not greater than 5


# Example 2:
A = 100
B = 100
C = 200

# Check if A = B, and print a message with if condition
if A == B:
    print('A and B are same !') 
# Output: A and B are same !

# Print with else condition
if B == C:
    print('B and C are same !')
else:
    print('B and C are NOT same !')
# Output: B and C are NOT same !
```

## The if-elif-else Statement
* The `if-elif-else` statement lets you check multiple conditions in a sequence and execute different blocks of code based on the first true condition.
```python
x = 3

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
# Output: x is less than 5
```

## Nested if Statements
* You can also nest `if` statements within other `if` statements to handle more complex decision-making scenarios.
```python
# Example 1:
x = 10
y = 5

if x > 5:
    if y > 3:
        print("Both x and y are greater than their respective thresholds")
    else:
        print("Only x is greater than its threshold")
# Output: Both x and y are greater than their respective thresholds


# Example 2:
A = 100
B = 100
C = 200
if A == 100:
    print('A is 100') 
elif A == 200:
    print('A is 200') 
elif A == 200:
    print('A is 200') 
else:
    print('A value is something else')
# Output: A is 100


# Example 3:
grade = 85

if grade >= 90:
    print("Grade is A")
elif grade >= 80:
    print("Grade is B")
elif grade >= 70:
    print("Grade is C")
else:
    if grade >= 60:
        print("Grade is D")
    else:
        print("Grade is F")
# Output: Grade is B
```

## Short-Hand if Statement
* Python also supports a short-hand form of the `if` statement known as the conditional expression or ternary operator.
```python
# Short-Hand if/Conditional Expression/Ternary Operator
# Example 1:
x = 10
result = "Even" if x % 2 == 0 else "Odd"
print(result)  
# Output: Even

# Example 2:
x = 7
result = "greater than 5" if x > 5 else "not greater than 5"
print(result)
# Output: greater than 5
```

## Use of Logical Operators In Conditional Statements
* You can combine multiple conditions using logical operators such as and, or, and not.
```python
# and operator
x = 10
y = 20

if x > 0 and y > 0:
    print("Both x and y are positive")
else:
    print("At least one of x and y is not positive")
# Output: Both x and y are positive

# or operator
name = "Alice"

if name == "Alice" or name == "Bob":
    print("Hello, Alice or Bob!")
else:
    print("You are not Alice or Bob.")
# Output: Hello, Alice or Bob!

# not operator
is_sunny = False

if not is_sunny:
    print("It's not sunny today.")
else:
    print("It's sunny today.")
# Output: It's not sunny today.
```

## Conclusion
* Conditional decision making in Python allows you to control the flow of your program based on specific conditions. 
* By using if, elif, else statements, and nested structures, you can create versatile, dynamic and responsive programs that execute different codes as needed.

##### [Back To Context](../../README.md)