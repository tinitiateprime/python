![Python Tinitiate Image](../../python_tinitiate.png)
# Python Tutorial
&copy; TINITIATE.COM
##### [Back To Context](../../README.md)

# Python Strings
* Strings in Python are sequences of characters, and they are one of the fundamental data types used to represent and manipulate textual data.
* They can contain letters, numbers, symbols, and even whitespace characters.
* Python provides a wide range of operations and methods to manipulate strings.

## Creating Strings
* Strings can be created using single quotes, double quotes, or triple quotes for multi-line strings.
```python
# String using DOUBLE QUOTES
var_string_1 = "DOUBLE QUOTES STRING:Python tutorials by tinitiate.com"

# String using SINGLE QUOTES
var_string_2 = 'SINGLE QUOTES STRING: Python tutorials by tinitiate.com'

# Multi line string using THREE DOUBLE QUOTES
var_string_3 = """Welcome to python 
tutorials by tinitiate.com, This is a multi line string
as you can see using double quotes"""

# Multi line string using THREE SINGLE QUOTES
var_string_4 = '''Welcome to python 
tutorials by tinitiate.com, This is a multi line string
as you can see using single quotes'''

# print the sthe above strings
print(var_string_1)
print(var_string_2)
print(var_string_3)
print(var_string_4)
```

## String Indexing/Accessing Characters in Strings
* Individual characters within a string can be accessed using indexing.
* Python uses 0-based indexing, where the first character is at index 0, the second at index 1, and so on. To index from last use negative symbol `-` before index number.
```python
var_test_string = "Python is cool"

# Index starts from 0, 
# This prints the first character of the string 
print('First character of variable var_test_string: ', var_test_string[0])

# Index of the last character is -1
print('Last character of variable var_test_string: ',var_test_string[-1])

# Print forth character from the end
print('Fourth character from the end of variable var_test_string: '
       ,var_test_string[-4])

# OUT oF range indexes
# When specifing indexes that don't exist is a string, it fails
var_my_string  = "four"
# print(var_my_string[5]) # this will raise an error
```

## String Slicing
You can extract a substring(portion of string) from a string using slicing.
```python
var_test_string = "Python is cool"
# Slicing part of the string using [number:]
# Prints string from specified index position to end of string
print(var_test_string[6:])

# Prints string from specified index position to end of string
print(var_test_string[-4:])

# Prints a part of the string between the specified index position
print(var_test_string[4:10])

# OUT oF range indexes
var_my_string  = "four"
# Slicing will not raise error, rather will not print anything 
print(var_my_string[5:7]) # Doesn't print anything 
```

## String Concatenation
* Strings can be concatenated using the `+` operator.
```python
first_name = "John"
last_name = "Doe"

full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe
```

## String Methods
* Python provides many built-in string methods for manipulation and analyzing strings.
### Case Conversion Methods:
* `upper()`: Converts a string to uppercase.
* `lower()`: Converts a string to lowercase.
* `title()`: Converts a string to title case(Capitalize the first character of each word)
* `swapcase()`: Swaps uppercase to lowercase and lowercase to uppercase.
* `capitalize()`: Coverts only first letter of the string to uppercase.
```python
var_string_case_test = "learn PYTHON"

# Uppercase conversion
print(var_string_case_test.upper()) # OUTPUT:  LEARN PYTHON

# Lowercase conversion
print(var_string_case_test.lower()) # OUTPUT:  learn python

# Title case conversion
print(var_string_case_test.title()) # OUTPUT:  Learn Python

# Swap case conversion
print(var_string_case_test.swapcase())  # OUTPUT:  LEARN python

# Capitalize case conversion
print(var_string_case_test.capitalize())  # OUTPUT:  Learn python
```
### Checking Methods:
* `isupper()`: Checks if the string is uppercase and returns `True`, otherwise it returns `False`.
* `islower()`: Checks if the string is lowercase and returns `True`, otherwise it returns `False`.
* `isalpha()`: Checks if the string contains only alphabets and returns `True`, otherwise it returns `False`.
* `isnumeric()`: Checks if the string contains only numerics and returns `true`, otherwise it returns `False`.
* `isalnum()`: Checks if the string contains only alphabets and numerics and returns `True`, otherwise it returns `False`.
* `isspace()`: Checks if the string has only whitespaces and returns `True`, otherwise it returns `False`.
* `startswith(str, start, end)`: Checks and returns `True` if the string starts with the specified string characters,otherwise it returns `False`. Optionally, if specified start and end index it searches within that and returns the requiredboolean.
* `endswith(str, start, end)`: Checks and returns `True` if the string ends with the specified string characters, otherwiseit returns `False`. Optionally, if specified start and end index it searches within that and returns the required boolean.
```python
# Checking if the string is UpperCase
print ('PYTHON'.isupper())   # Prints true
v = 'PYTHON'
print (v.isupper())   # Prints true

# Checking if the string is lowerCase
print ('PYTHON'.islower())   # Prints false

# Checking if the string has only alphabets
print ('PYTHON01'.isdigit()) # Prints false

# Checking if the string has only numerics
print ('1000'.isnumeric()) # Prints true

# Checking if the string has only alphabets and numerics
print ('PYTHON01'.isalnum()) # Prints true

# Checking if the string has whitespace (space/tab) only
print ('  '.isspace()) # Prints true

# Checking startswith
text = "Hello, world!"
result = text.startswith("Hello")
print(result)  # Output: True

text = "Hello, world!"
result = text.startswith("world", 7)
print(result)  # Output: True

# Checking endswith
text = "Hello, world!"
result = text.endswith("world!")
print(result)  # Output: True

text = "Hello, world!"
result = text.endswith("lo,", 0, 6)
print(result)  # Output: True
```
### Stripping Methods:
`strip()`: Removes leading(starting) and trailing(ending) whitespaces. If specified anything in the paranthesis, it will removes the occurrence(s) of the specified characters.
`lstrip()`: Removes leading(starting) whitespaces.If specified anything in the paranthesis, it will remove the leading occurrenc(s) of the specified characters.
`rstrip()`: Removes trailing(ending) whitespaces.If specified anything in the paranthesis, it will remove the trailing occurrenc(s) of the specified characters.
```python
# strip()
# Removes the whitespaces starting and ending of the string
print ('   This is a test  '.strip())
# OUTPUT: This is a test

# Removes the occurrence of 't'
print ('This is a test'.strip('t'))
# OUTPUT: This is a tes

# Removes the occurrence of 'T'
print ('This is a test'.strip('T'))
# OUTPUT: his is a test

# Removes the occurrence of 'is'
print ('sssThis is a testsss'.strip('s'))
# OUTPUT: This  a test


# lstrip()
text = "    Hello, world!    "
# Remove leading whitespace
stripped_text = text.lstrip()
print(stripped_text)  # Output: "Hello, world!    "

# Remove leading specified characters
text = ">>>Hello, world!"
stripped_text = text.lstrip(">")
print(stripped_text)  # Output: "Hello, world!"

print ('This is a test'.lstrip('This'))
# OUTPUT: is a test  


# rstrip()
text = "    Hello, world!    "
# Remove trailing whitespace
stripped_text = text.rstrip()
print(stripped_text)  # Output: "    Hello, world!"

# Remove trailing specified characters
text = "Hello, world!..."
stripped_text = text.rstrip(".")
print(stripped_text)  # Output: "Hello, world!"

print ('This is a test'.rstrip(' test'))
# OUTPUT: This is a
```
### Justify And Padding Methods:
* `ljust(length, char)`: Justifies a string by aligning the string to the left and padding the string to the length mentionedwith the specified characters.
* `center(length, char)`: Justifies a string by aligning the string to the center and padding the string to the lengthmentioned with the specified characters.
* `rjust(length, char)`: Justifies a string by aligning the string to the right and padding the string to the length mentioned with the specified characters.
```python
# ljust(lenght, char)
print ('test'.ljust(10,'+'))
# OUTPUT: test++++++

text = "Hello"
l_padded_text = text.ljust(10, '*')
print(l_padded_text)  # Output: Hello*****
print(l_padded_text.ljust(15,' '))


# center(length, char)
print ('test'.center(10,'+'))
# OUTPUT: +++test+++

text = "Hello"
centered_text = text.center(11, '*')
print(centered_text)  # Output: ***Hello***
print(centered_text.center(15,' '))


# rjust(length, char)
print ('test'.rjust(10,'+'))
# OUTPUT: ++++++test

text = "Hello"
r_padded_text = text.rjust(10, '*')
print(r_padded_text)  # Output: "*****Hello"
print(r_padded_text.rjust(15,' '))
```
### Searching Methods:
* `index(str,start,end)`: If start index and end index not specified, Returns the index of the first occurrence of specifiedsubstring within the string. If start and end index specified, returns the index of the first occurence of specifiedsubstring within those indexes. If the substring is not found, it raises a `ValueError`.
* `rindex(str,start,end)`: If start index and end index not specified, Returns the index of the last occurrence of specifiedsubstring within the string. If start and end index specified, returns the index of the last occurence of specified substringwithin those indexes. If the substring is not found, it raises a `ValueError`.
* `find(str,start,end)`: If start index and end index not specified, returns the index of the first occurrence of specifiedsubstring within the string. If start and end index specified, returns the index of the first occurence of specifiedsubstring within those indexes. If the substring is not found, it returns `-1`.
* `rfind(str,start,end)`: If start index and end index not specified, returns the index of the last occurrence of specifiedsubstring within the string. If start and end index specified, returns the index of the last occurence of specified substringwithin those indexes. If the substring is not found, it returns `-1`.
* So, if you're uncertain whether the substring exists or not, and you don't want your program to stop execution due to anerror, you might prefer using `find()` or `rfind()`(as per requirement). If you're confident that the substring should existand its absence indicates an error in your program's logic, you might prefer using `index()` or `rindex()`(as perrequirement) to explicitly handle that case.
```python
# index()
sentence = "This is a sample sentence."
index1 = sentence.index("is")
print(index1)  # Output: 2

# Specifying start and end index
index2 = sentence.index("is", 3, 10)
print(index2)  # Output: 5

# Specifying only start
index3 = sentence.index("s", 4)
print(index3)  # Output: 6

# Searching string that doesn't exist, Uncomment the following to view error
# index4 = sentence.index("Python")
# print(index4)  # Output: ValueError


# rindex()
sentence = "This is a sample sentence."
index1 = sentence.rindex("is")
print(index1)  # Output: 5

# Specifying start and end index
index2 = sentence.rindex("s", 2, 23)
print(index2)  # Output: 17

# Specifying only start
index3 = sentence.rindex("is", 1)
print(index3)  # Output: 5

# Searching string that doesn't exist, Uncomment the following to view error
# index4 = sentence.rindex("z")
# print(index4)  # Output: ValueError


# find()
sentence = "This is a sample sentence."
index1 = sentence.find("sample")
print(index1)  # Output: 10

# Substring not found
index2 = sentence.find("example")
print(index2)  # Output: -1


# rfind()
sentence = "This is a sample sentence."
index1 = sentence.rfind("is", 1, 5)
print(index1)  # Output: 2

# Substring not found
index2 = sentence.rfind("example")
print(index2)  # Output: -1
```
### Miscellaneous Methods:
* `len()` : Returns length of the string
* `split()`: Splits a string into a list of substrings based on a delimiter.
* `splitlines()`: Splits a multi-line strings into a list of substrings based on a delimiter.
* `replace()` : Replaces with the specified
```python
# len()
my_string = "Hello, world!"
print(len(my_string))  # Output: 13

# split()
my_string = "Hello, World!"
print(my_string.split(','))        # Output: ['Hello', ' World!']

# splitlines()
testString = """Line 1
Line 2
Line 3
"""
print(testString.splitlines()) # OUTPUT: ['Line 1', 'Line 2', 'Line 3']

# replace()
my_string = "Hello, World!"
print(my_string.replace('Hello', 'Hi'))  # Output: Hi, World!
```

## String Formatting
* String formatting allows you to create dynamic strings by incorporating variables or values into the string.
* There are different ways to achieve this, including f-strings and the format() method.
```python
name = "Alice"
age = 30
# Using f-strings(formatted string literals)
print(f"My name is {name} and I am {age} years old.")  
# Output: My name is Alice and I am 30 years old.

# Using the .format()
print("My name is {} and I am {} years old.".format(name, age))  
# Output: My name is Alice and I am 30 years old.

# Using the %
print("My name is %s and I am %d years old." % (name, age))  
# Output: My name is Alice and I am 30 years old.
```

## String Operations
* Python supports various operations on strings, such as membership tests, concatenation, repetition, and comparison.
```python
my_string = "Python"

print("P" in my_string)    # Output: True
print(my_string + " 3.8")   # Output: Python 3.8
print(my_string * 3)        # Output: PythonPythonPython
print(my_string == "Python") # Output: True
```

## String Immutability
Strings in Python are immutable, meaning that once a string is created, its contents cannot be changed. If you want to modify a string, you'll need to create a new string with the desired changes.

##### [Back To Context](../../README.md)
