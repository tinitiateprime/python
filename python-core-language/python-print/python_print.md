![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# Python Print
* In Python, `print()` is a built-in function that is used to output information to the console or terminal.
* It allows you to display text, variables, and other data in a human-readable format.
* The `print()` function takes one or more arguments, which are the values you want to display, and it separates them with a space by default.

## Syntax
```python
# Prints 'Hello World!' to the console
print("Hello World!")
# OUTPUT: Hello World!
```

## Comments
* In Python, comments are annotations within the code that are ignored by the Python interpreter.
* They are used to add explanatory notes or documentation to the code for better understanding.
* Comments help other developers (or even yourself in the future) comprehend the code logic, purpose, and functionality.
### Types of comments
* **Single-line comments:** These comments start with the hash character `#` and continue until the end of the line.
```python
# This is a single-line comment
print("tinitiate.com")  # This comment is beside a code line
# This comment is after a statement
# OUTPUT: tinitiate.com
```
* **Multi-line comments (or docstrings):** Multi-line comments are usually enclosed within triple quotes (`'''` or `"""`) and are often used for documenting functions, classes, or modules. They can span multiple lines.
```python
'''
This is a multi-line comment
It can span multiple lines
Useful for documenting functions, classes, or modules
'''
print("tinitiate.com")
# OUTPUT: tinitiate.com
```

## Print statement variations
* Python's `print()` function offers various ways to customize the output beyond the default behavior using various parameters.
### Print basic variations
* Simple print statement
```python
print("Welcome to tinitiate.com python tutorials")
# OUTPUT: Welcome to tinitiate.com python tutorials
```
* Print statement with append using the `,` , This appends a SPACE
```python
# You can pass multiple objects separated by commas
print("Welcome to tinitiate.com" , 'python tutorials "Appended ," ')
# OUTPUT: Welcome to tinitiate.com python tutorials "Appended ,"
```
* Print statement with append using the `+` , This Does Not append SPACE
```python
print('Welcome to tinitiate.com' + 'python tutorials "Appended +"')
# OUTPUT: Welcome to tinitiate.compython tutorials "Appended +"
```
* Print statement using custom separator, Using the `sep=` parameter we can change the separator between multiple arguments
```python
# By default sep parameter comma is SPACE
print("apple", "banana", "orange")
# OUTPUT: apple banana orange

print("apple", "banana", "orange", sep=", ")
# OUTPUT: apple, banana, orange

print("apple", "banana", "orange", sep="- ")
# OUTPUT: apple- banana- orange
```
* Print a single quote, using escape character `\` backslash 
```python
print('Printing a single quote \'')
# OUTPUT: Printing a single quote '

# Same goes with double quote and backslash
print("Printing a double quote \"")
# OUTPUT: Printing a double quote "
```
* Printing new line character `\n`
```python
print("line1" + '\n' + "line2")
# OUTPUT: line1
#         line2  
```
* Print statement using end parameter, Using end parameter we can specify what character(s) should be printed at the end of the `print()` statement, instead of the default newline character
```python
# Below is Without end parameter
print('First Line')
print('Second Line')
# OUTPUT: First Line
#         Second Line

print('First Line', end="")
print('Second Line')
# OUTPUT: First LineSecond Line

print("tinitiate", end=".")
print("com")
# OUTPUT: tinitiate.com
```
* Printing a string multiple times using the `*` operator
```python
print ("hello " * 3)
# OUTPUT: hello hello hello 
```

### Print "C language" style
* Printing variables and numerics in C language style
```python
# Numerics
print('print a double %5.3f' % (1000.23232))
# OUTPUT: print a double 1000.232

# Variables
strVal = 'tinitiate.com'
intval = 100
print("String = %s Integer = %i" % (strVal, intval))
# OUTPUT: String = tinitiate.com Integer = 100
```

### Print `string.format`
* The `{}` brackets and data enclosed within them are called format fields
* The data is replaced with the objects passed in the `str.format()` method
* The order by default is left to right as in `{}` `{}` and `str.format(Obj1, Obj2)`
```python
print('Welcome to {} training of {} language'.format('tinitiate.com', 'python'))
# OUTPUT: Welcome to tinitiate.com training of python language
```
* The order can be substituted by the numbers `{1}` `{2}` for first and second object in `str.format(Obj1, Obj2)`
```python
print('{0} and {1}'.format('tinitiate.com', 'python'))
# OUTPUT:  tinitiate.com and python

print('{1} and {0}'.format('tinitiate.com', 'python'))
# OUTPUT: python and tinitiate.com
```
* The order of the data can also be in the key-values of the `str.format(key1='value1',key2='value2')`
```python
print('{siteName} teaches {LanguageName}.'.format
    (siteName='tinitiate.com', LanguageName='python'))
# OUTPUT: tinitiate.com teaches python.
```
* Positional and key-value arguments can be arbitrarily combined
```python
print('The site {0} teaches {LanguageName}'.format
    ('tinitiate.com', LanguageName='Python'))
# OUTPUT: The site tinitiate.com teaches Python
```
* Print statement using `f` string, `f` string is similar to `string.format`
```python
l_site = 'tinitiate.com'
l_language_name = 'Python'
l_str = f"The site {l_site} teaches {l_language_name}"
print(l_str)
# OUTPUT: The site tinitiate.com teaches Python
```

### Printing variables and numerics
* Print variables
```python
# Declaring variables
var_integer  = 1                # An integer type variable
var_float    = 10.44            # A float type variable
var_string   = "tinitiate.com"  # A string type variable

print(var_integer, var_float, var_string)
# OUTPUT: 1 10.44 tinitiate.com

print('var_integer', 'var_float', 'var_string')
# OUTPUT: var_integer var_float var_string
```
* Print numerics
```python
print(7)
# OUTPUT: 7

print(7+7)
# OUTPUT: 14

print('7'+'7')
#OUTPUT: 77
```

### Print ASCII and UNICODE strings
* Print ASCII(raw) using `print(r'string')`
```python 
print(r'This is a ASCII string, Has no special characters')
# OUTPUT: This is a ASCII string, Has no special characters

print(r"First line\nSecond line")
# OUTPUT: First line\nSecond line
```
* Print UNICODE using `print(u'string')`
```python
print(u'This is a UNICODE string (\u00DF), and Has special characters')
# OUTPUT: This is a UNICODE string (ß), and Has special characters
```

## Conclusion
These are just a few examples of how you can use the `print()` function in Python to display information. It's a fundamental tool for debugging, logging, and interacting with users through the console.

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
