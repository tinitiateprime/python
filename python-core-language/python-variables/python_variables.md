![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# Python Variables
* In Python, Variables are memory locations that are used to store and manipulate data.
* They provide a way to give names to values, making the code more readable and manageable.
* Variables can hold various types of data, such as numbers, text, and more complex data structures, and their values can be changed during the execution of a program.

## Variable Declaration and Assignment
* In Python, there is no specific variable declaration and variable initialization.
* The declaration happens automatically when you assign a value to a variable.
* To assign a value to a variable, you simply use the assignment operator `=`
### Simple Creation
```python
variable1 = 1;          # Integer
variable2 = "test";     # String
variable3 = 100.4;      # float value

# Print all the three variables 
print("variable1 : ", variable1)
print("variable2 : ", variable2)
print("variable3 : ", variable3)

# OUTPUT:
# variable1 :  1
# variable2 :  test
# variable3 :  100.4
```
### Reassign and Delete
```python
variable1 = 1;          # Integer
variable2 = "test";     # String
variable3 = 100.4;      # float value

# Reassign a value to a variable
variable1 = 4;          # Integer
print("variable1 reassigned value: ", variable1)
# OUTPUT:
# variable1 reassigned value:  4

# Reassign a variable value to a variable
variable1 = variable2
print("variable1 again reassigned value: ", variable1)
# OUTPUT:
# variable1 again reassigned value:  test

# Deleting a single or multiple variables by using the del statement.
del variable1
# Use comma(,) after variable for multiple deletes
# Using the variable after deleting will raise an error
# Remove comment symbol (#) and try to print the below statement,
# it will raise an error
# print("variable1 reassigned value: ", variable1)
```
### Syntax Variations
```python
# Variation 1:
var1 = var2 = 100
print("var1 : ", var1)
print("var2 : ", var2)
# OUTPUT:
# var1 :  100
# var2 :  100

# Variation 2:
var100, var200 = 100, 200
print("var100 : ", var100)
print("var200 : ", var200)
# OUTPUT:
# var100 :  100
# var200 :  200
```

## Variable Naming Rules
* Variable names can contain letters (a-z, A-Z), digits (0-9), and underscores (_).
* Variable names cannot start with a digit.
* Python variable names are case-sensitive.
* Variable names cannot be Python keywords.

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
