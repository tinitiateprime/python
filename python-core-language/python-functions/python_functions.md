![Python Tinitiate Image](../../python_tinitiate.png)
# Python Tutorial
&copy; TINITIATE.COM
##### [Back To Context](../../README.md)

# Python Functions
* Functions in Python are blocks of reusable code that perform a specific task. Thus, Function is a code block, that can be called once or multiple times.
* They allow you to break down your program into smaller, modular components, making your code more organized, readable, and easier to understand, debug, and maintain.
* Functions play a crucial role in modular programming and code reusability.

## Function Structure
* The structure of a Python function typically consists of several components, including the function definition, parameters, docstrings, function body, and return statement.
```python
def function_name(parameter1, parameter2, ...):
    """
    Docstring: Description of the function.
    
    Args:
        parameter1 (type): Description of parameter1.
        parameter2 (type): Description of parameter2.
        ...
    
    Returns:
        return_type: Description of the return value.
    """
    # Code is indented, notice the spacing
    # Function body: Code to be executed when the function is called
    # ...
    # You can use the parameters within the function

    # Return statement: Optional, used to return a value from the function
    # return value
```
* Here's what the general structure components of a Python function mean:
    * `def`: This keyword is used to define a function.
    * **function_name**: Replace this with the name you want to give to your function. Choose a descriptive name that indicates the function's purpose and follow Python naming conventions (lowercase with underscores for readability).
    * **parameters/arguments**: These are placeholders for values that the function expects to receive when it's called. Parameters are optional. They are enclosed in parentheses `()` and multiple parameters can be separated by commas`,`. After parameters colon`:` indicates the end of function definition, and next is the code within the function.
    * **Indentation**: Code inside the function must be indented, meaning all code inside a function must atleast have 2 spaces in front of them, Any code without that indentation means that code is outside the function code.
    * **docstring**: An optional string that provides documentation about the function's purpose, parameters, and expected behavior.
    * **Function body**: This is where you write the actual code that accomplishes the task. It consists of one or more statements that perform a specific task or computation. You can use the provided parameters within the function.
    * `return`: An optional statement used to send a value back from the function when it's executed.

## Defining a Function
* Using the above syntax, we can define the function with code block.
```python
# Defining a Function
# Example 1:
def greet(name):
    print("Hello,", name)

# Example 2:
def square(number):
    """Calculate the square of a number."""
    result = number ** 2
    return result
```

## Calling a Function
* To use a function, you need to call it by its name followed by parentheses`()`.
* If the function requires parameters, you pass the values inside the parentheses.
* The function executes its code and may optionally return a value.
```python
# Example 1:
# Defining a Function
def greet(name):
    print("Hello,", name)

# Calling a Function
greet("Alice")

# Output: Hello, Alice


# Example 2:
# Defining a Function
def square(number):
    """Calculate the square of a number."""
    result = number ** 2
    return result

# Calling a Function
num = 5
square_result = square(num)
print(f"The square of {num} is {square_result}")

# Output: The square of 5 is 25
```

## Scope of Variables in Functions
* Variables defined inside a function have local scope, meaning they are only accessible within that function.
    * **Local Variable** are variables inside a function, they are accessable from within a function and not outside the function.
* Variables defined outside functions have global scope, meaning they can be accessed from any part of the code.
    * **Global Variable** is accessable from anywhere in the program, Global Variables outside the function are accessable inside the function as well.
```python
# Example 1:
def my_func():
    x = 10 # Local Variable
    print("Inside function:", x)

x = 20 # Global Variable
my_func()
print("Outside function:", x)

# Output: Inside function: 10
#         Outside function: 20


# Example 2:
MyVar = 'This is a Global Value'
def myFunction():
    # Local Variable
    MyVar = 'This is a local variable'
    print('Value of MyVar inside function: ', MyVar)

# Make a call to myFunction
myFunction()
print('Value of MyVar outside function: ', MyVar)

# Output: Value of MyVar inside function:  This is a local variable
#         Value of MyVar outside function:  This is a Global Value


# Example 3:
global_variable = 10  # Global variable
def func():
    local_variable = 20  # Local variable
    print(global_variable)  # Accessing global variable inside function
    print(local_variable)

func()
print(global_variable)  # Accessing global variable outside function
# Output: 10
#         20
#         10

# print(local_variable)  # Uncomment and run, This line would raise an error
```

## Types of Arguments in Functions
* In Python, functions can accept different types of arguments or parameters.
### Positional Arguments
* These are the most basic type of arguments.
* Positional arguments are passed to a function based on their position or order in the function call.
```python
def greet(name, greeting):
    print(greeting, name)

greet("Alice", "Hello")  
# "Alice" is assigned to name, "Hello" is assigned to greeting
# Output: Hello Alice
```
### Keyword Arguments
* Keyword arguments are passed to a function using the parameter name followed by the value.
* They allow you to specify arguments in any order and makes the code more readable.
```python
def greet(name, greeting):
    print(greeting, name)

greet(greeting="Hello", name="Bob")  
# "Hello" is assigned to greeting, "Bob" is assigned to name
# Output: Hello Bob
```
### Default Arguments
* Default arguments have a default value specified in the function definition.
* If a value is not provided for a default argument during the function call, the default value is used.
```python
# Example 1:
def greet(name, greeting="Hello"):
    print(greeting, name)

greet("Charlie")  # Default argument: "Hello" is assigned to greeting
# Output: Hello Charlie


# Example 2:
def power(base, exponent=2):
    result = base ** exponent
    print(f"{base} raised to the power of {exponent} is {result}")

power(3)      # Uses default exponent (2)
power(2, 4)   # Overrides default exponent
# Output: 3 raised to the power of 2 is 9
#         2 raised to the power of 4 is 16


# Example 3:
def function_with_default_arguments( arg1, default_arg2 = 100 ):
    "This is a demonstration for default argument"
    print("Value of arg1: ", arg1)
    print("Value of default_arg2: ", default_arg2)
    return      # If Nothing specified returns None

# Calling function with both arguments 
print(function_with_default_arguments( arg1 = 10, default_arg2 = 99 ))
# OUTPUT:
#    Value of arg1:  10
#    Value of default_arg2:  99
#    None

# Calling function with ONLY ONE argument
print(function_with_default_arguments( arg1 = 11))
# OUTPUT:
#    Value of arg1:  11
#    Value of default_arg2:  100
#    None
```
### Variable-Length Arguments
* Variable-length arguments (often denoted with `*args`) allow a function to accept any number of positional arguments.
* These arguments are captured as a tuple inside the function.
* Also called as **Arbitrary Positional Arguments**.
```python
# Example 1:
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_numbers(1, 2, 3)) 
# Variable-length arguments: 1, 2, 3 are captured as a tuple (1, 2, 3)
# Output: 6


# Example 2:
def show_items(*items):
    print("Items:")
    for item in items:
        print(item)

print(show_items("apple", "banana", "cherry"))
# Output: Items:
#         apple
#         banana
#         cherry
#         None

# Example 3:
def one_fixed_and_arbitrary_length_argument(arg1, *arbitrary_arguments_tuple):
    "This is a demonstration of the one fixed and arbitrary arguments"
    print('Value of the first argument: ',arg1)
    v=0
    for c1 in arbitrary_arguments_tuple:
        v+=1
        print('Arbitrary Argument number: ',v,' value: ',c1)

# calling the function 
# in this case ONE fixed and FOUR variable length
print(one_fixed_and_arbitrary_length_argument(1, 2, 3, 5, 6))

# in this case ONE fixed and FOUR variable length
print(one_fixed_and_arbitrary_length_argument
(1, 'a1', 'a2', 'a3', 'a4', 'a5', 'a6'))

# Output: Value of the first argument:  1
#         Arbitrary Argument number:  1  value:  2
#         Arbitrary Argument number:  2  value:  3
#         Arbitrary Argument number:  3  value:  5
#         Arbitrary Argument number:  4  value:  6
#         None
#         Value of the first argument:  1
#         Arbitrary Argument number:  1  value:  a1
#         Arbitrary Argument number:  2  value:  a2
#         Arbitrary Argument number:  3  value:  a3
#         Arbitrary Argument number:  4  value:  a4
#         Arbitrary Argument number:  5  value:  a5
#         Arbitrary Argument number:  6  value:  a6
#         None
```
### Keyword Variable-Length Arguments
* Keyword variable-length arguments (often denoted with `**kwargs`) allow a function to accept any number of keyword arguments.
* These arguments are captured as a dictionary inside the function.
* Also called as **Arbitrary Keyword Arguments**.
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key + ":", value)

print_info(name="Alice", age=30, city="New York")  
# Keyword variable-length arguments: name="Alice", age=30, city="New York"
# Output: name: Alice
#         age: 30
#         city: New York
```

## Python Functions With Different Inputs In Parameters
### Python Functions with empty parameters:
* Calling a simple python function without any input values or return values
```python
def myFunc():
   "This is a function without any input values or return values"
   print("This message is from the function: myFunc")
# Calling the function 
myFunc()

# Calling the function again (Can be called as many times as needed)
myFunc()

#OUTPUT:
#    This message is from the function: myFunc
#    This message is from the function: myFunc
```
### Python Functions with input parameters
* Calling a function with 2 input parameters and returning the sum
```python
def Add2Nums(number1, number2):
    "This is a function with 2 input parameters and returning the sum"
    print('Sum of',number1,'and',number2,'is',number1+number2)

# Calling the function with input parameters
Add2Nums(1,2)  # These are the input parameters
Add2Nums(10,20)

# OUTPUT:
# Sum of 1 and 2 is 3
# Sum of 10 and 20 is 30
```
### Python Functions with loop and conditional statements
* Calling a function with loop and conditional statements as parameters
```python
# Example 1:
def function_with_constructs(in_string, in_number):
    "This function demonstrates use of loop and conditional statements"
    # Loop
    for c in range(5):
        print(in_string)

    # Conditional statement
    if in_number%2 == 0:
        print(in_number,' is even.')
    elif in_number%2 != 0:
        print(in_number,' is odd.')

# Calling the function
function_with_constructs("Python", 20)
# OUTPUT:
#    Python
#    Python
#    Python
#    Python
#    Python
#    20 is even.


# Example 2:
def print_even_numbers(numbers):
    """
    Print even numbers from the given list.
    """
    for num in numbers:
        if num % 2 == 0:
            print(num, "is even")
        else:
            print(num, "is odd")

# Call the function
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_even_numbers(numbers_list)
# Output: 1 is odd
#         2 is even
#         3 is odd
#         4 is even
#         5 is odd
#         6 is even
#         7 is odd
#         8 is even
#         9 is odd
#         10 is even
```
### Python Functions with Return Value
* A function can **RETURN** a value, Which is a value that is substituted in the place of the function call.
* The function when returns a value, Must be stored in a variable Or the function can be put in a print statement if the return value is printable.
```python
# Example 1:
def return_sum(num1, num2):
    return num1+num2

## Call the function
## Store the value to a variable
x = return_sum(1, 2)
print(x)

## Call the function, Use the call in a print
print(return_sum(1, 2))

# Output: 3
#         3


# Example 2:
def calculate_average(numbers):
    """
    Calculate the average of numbers in a list.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The average of the numbers.
    """
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Call the function
numbers_list = [1, 2, 3, 4, 5]
average = calculate_average(numbers_list)
print("Average:", average)
# Output: Average: 3.0
```
### Python Functions with a LIST input parameter
* Calling a function that accepts a LIST as input parameter.
```python
# Example 1:
def extract_list_into_strings_and_numbers(in_list):
    """This is a function separates list into a stringlist and numberlist"""
    
    # Store Numbers from "in_list" parameter in number_lsti
    number_list = []
    
    # Store Strings from "in_list" parameter in string_list
    string_list = []

    # Loop through the input parameter list
    for c in in_list:
        if c.isdigit():
            number_list.append(c)
        else:
            string_list.append(c)

    # Print Number List
    print(number_list)

    # Print String List
    print(string_list)

# Calling the function 
print(extract_list_into_strings_and_numbers(['1','A', '2', '3','B', 'c']))

# OUTPUT:
#        ['1', '2', '3']
#        ['A', 'B', 'c']


# Example 2:
def process_list(input_list):
    """
    Process a list of numbers.

    Args:
        input_list (list): A list of numbers.

    Returns:
        list: A list containing squared numbers.
    """
    squared_numbers = [x ** 2 for x in input_list]
    return squared_numbers

# Calling the function 
numbers = [1, 2, 3, 4, 5]
result = process_list(numbers)
print("Squared numbers:", result)
# Output: Squared numbers: [1, 4, 9, 16, 25]
```
### Python Functions with a TUPLE input parameter
* Calling a function that accepts a TUPLE as input parameter.
```python
# Example 1:
def extract_tuple_into_strings_and_numbers(in_tuple):
    """This is a function separates tuple into a stringlist
     and numberlist based on split type"""

    # Store Numbers from "in_list" parameter in number_list
    number_list = []
    
    # Store Strings from "in_list" parameter in string_list
    string_list = []

    work_list = list(in_tuple)

    for c in work_list:
        if c.isdigit():
            number_list.append(c)
        else:
            string_list.append(c)

    # Print Number List
    print(number_list)

    # Print String List
    print(string_list)

# Calling the function 
print(extract_tuple_into_strings_and_numbers(('1','A', '2', '3','B', 'c')))

# OUTPUT:
#       ['1', '2', '3']
#       ['A', 'B', 'c']


# Example 2:
def reverse_tuple(input_tuple):
    """
    Reverse the elements of a tuple.

    Args:
        input_tuple (tuple): A tuple of elements.

    Returns:
        tuple: A new tuple with elements reversed.
    """
    reversed_tuple = input_tuple[::-1]
    return reversed_tuple

# Calling the function
my_tuple = (1, 2, 3, 4, 5)
reversed_result = reverse_tuple(my_tuple)
print("Reversed tuple:", reversed_result)
# Output: Reversed tuple: (5, 4, 3, 2, 1)
```
### Python Functions with a DICTIONARY input parameter
* Calling a function that accepts a DICTIONARY as input parameter.
```python
# Example 1:
def extract_dictionary_keys_values(in_dictionary):
    """This is a function separates dictionary KEYS and
     VALUES into lists and prints them"""
    
    # Print Keys, Using the ".KEYS" and enclosed in the "list()" function
    print(list(in_dictionary.keys()))

    # Print Keys, Using the ".VALUES" and enclosed in the "list()" function
    print(list(in_dictionary.values()))

# Calling the function
extract_dictionary_keys_values({1:'A',2:'B', 3:'C'})

# OUTPUT:
#       [1, 2, 3]
#       ['A', 'B', 'C']


# Example 2:
def calculate_average_values(input_dict):
    """
    Calculate the average of values for each key in a dictionary.

    Args:
        input_dict (dict): A dictionary with keys mapped to lists of numbers.

    Returns:
        dict: A dictionary containing keys and their corresponding averages.
    """
    average_dict = {}
    for key, values in input_dict.items():
        average = sum(values) / len(values)
        average_dict[key] = average
    return average_dict

# Calling the function
data = {
    "A": [10, 20, 30],
    "B": [15, 25, 35],
    "C": [20, 30, 40]
}
averages = calculate_average_values(data)
print("Average values:", averages)
# Output: Average values: {'A': 20.0, 'B': 25.0, 'C': 30.0}
```

## Python Functions Arguments Pass By Reference and Pass By Value
* In Python, function arguments are passed by object reference, which means that when you pass an object (like a list or a dictionary) as an argument to a function, you are passing a reference to the object, not a copy of the object itself.
* This behavior can lead to confusion regarding whether Python uses pass by reference or pass by value. 
### Pass By Reference: 
* When you pass a mutable object (such as a list or a dictionary) to a function in Python, any changes made to the object within the function will affect the original object outside the function.
```python
# Example 1:
def modify_list(lst):
    lst.append(4)  # Modifying the list inside the function

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  
# Output: [1, 2, 3, 4]


# Example 2:
source_list = ['A', 'B', 'C']

def function_pass_by_reference(in_list):
    print('function_pass_by_reference says Input List: ', in_list)
    # Changing the input by appending a value to in_list
    in_list.append('D')
    print('function_pass_by_reference says changed List: ', in_list)

print('Before passing reference to function, source_list: ', source_list)

# Passing the "source_list" and NOT A COPY of the "source_list"
function_pass_by_reference(source_list)
print('After passing reference to function, source_list: ', source_list)

# Ouput:
# Before passing reference to function, source_list:  ['A', 'B', 'C']
# function_pass_by_reference says Input List:  ['A', 'B', 'C']
# function_pass_by_reference says changed List:  ['A', 'B', 'C', 'D']
# After passing reference to function, source_list:  ['A', 'B', 'C', 'D']

# Example 3:
def modify_list(my_list):
    my_list.append(4)
    my_list[0] = 100
    print(my_list) 

numbers = [1, 2, 3]

modify_list(numbers) 
# Output: [100, 2, 3, 4]

print(numbers)  
# Output: [100, 2, 3, 4]


# Example 4:
def add_key_value(my_dict):
    my_dict["c"] = 30
    print(my_dict)

data = {"a": 10, "b": 20}

add_key_value(data) 
# Output: {'a': 10, 'b': 20, 'c': 30}

print(data)  
# Output: {'a': 10, 'b': 20, 'c': 30}
```
### Pass By Value:
* When you pass an immutable object (such as a tuple or an integer) to a function in Python, any modifications made to the object within the function do not affect the original object outside the function.
* Instead, a new object is created inside the function.
```python
# Example 1:
def modify_number(num):
    num = num + 1  # Modifying the number inside the function
    print(num)

my_num = 5

modify_number(my_num) 
# Output: 6

print(my_num)  
# Output: 5


# Example 2:
# Create a source list
source_list_2 = ['A', 'B', 'C']

def function_pass_by_value(in_list):
    print('function_pass_by_value says Input List: ', in_list)
    # Reassigning a local value, [pass by value]
    in_list =[1, 2, 3, 4]
    print('function_pass_by_value says changed List: ', in_list)

print('Before passing by value to function, source_list: ', source_list_2)

function_pass_by_value(source_list_2)

print('After passing by value to function, source_list: ', source_list_2)

# Output:
# Before passing by value to function, source_list:  ['A', 'B', 'C']
# function_pass_by_value says Input List:  ['A', 'B', 'C']
# function_pass_by_value says changed List:  [1, 2, 3, 4]
# After passing by value to function, source_list:  ['A', 'B', 'C']


# Example 3:
def modify_tuple(t):
    t = (4, 5, 6)
    print(t)

my_tuple = (1, 2, 3)
modify_tuple(my_tuple)
print(my_tuple)  # Output: (1, 2, 3)


# Example 4:
def modify_string(s):
    s = s.upper()
    print(s)

my_string = "hello"

modify_string(my_string) 
# Output: HELLO

print(my_string)  
# Output: hello
```

## Lambda Functions / Anonymous functions
* Lambda functions (also called anonymous functions) are small, inline functions defined using the `lambda` keyword. 
* They are useful for short, one-line functions.
```python
# Add Two Numbers
add = lambda x, y: x + y
print(add(3, 4))  
# Output: 7

# Check if a Number is Even
is_even = lambda x: x % 2 == 0
print(is_even(6))  
# Output: True
print(is_even(7))  
# Output: False

# Square a Number
square = lambda x: x ** 2
print(square(5))  
# Output: 25

# Sorting a List of Tuples by the Second Element
points = [(1, 2), (3, 1), (5, 4), (2, 2)]
sorted_points = sorted(points, key=lambda x: x[1])
print(sorted_points)  
# Output: [(3, 1), (1, 2), (2, 2), (5, 4)]
```

## Use Cases of Functions
* **Encapsulating Reusable Code:** Functions allow you to encapsulate blocks of code and reuse them throughout your program.
* **Improving Code Readability:** Breaking down complex tasks into smaller functions makes your code easier to understand and maintain.
* **Modular Programming:** Functions enable modular programming by dividing your program into smaller, self-contained modules.

## Conclusion
* Functions are essential building blocks in Python programming, allowing you to write modular, reusable code and enhance the structure, readability, and maintainability of your programs.
* They allow you to encapsulate logic and create code that's easier to understand and maintain.

##### [Back To Context](../../README.md)