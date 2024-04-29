![Python Tinitiate Image](../../python_tinitiate.png)
# Python Tutorial
&copy; TINITIATE.COM
##### [Back To Context](../../README.md)

# Python Modules
* Python modules are a fundamental concept in Python programming, enabling you to organize and reuse code efficiently.
* A module in Python is simply a file containing Python code. This code can define functions, classes, and variables, and can also include runnable code.
* Modules are used to organize and break down your code into smaller, reusable components.
* They allow you to enclose related functionalities and keep your codebase organized, making it easier to manage and maintain.
* Grouping related code into a module makes the code easier to understand and use.
* Modules can be **import'ed** to other python files or other python modules and accessed.

## Creating a Module
* To create a module, you simply need to save your code into a file with a `.py` extension.
* For example, you can create a code and save it with file named **my_module.py**
* Inside this file, you can define functions, classes, and variables just like you would in any other Python script(code).
* The file name/module name must start with a letter `a-z, A-Z` or an underscore `_` and Can only contain alphanumeric characters (letters and numbers) and underscores.
```python
# Global variables for different countries
country_1 = "USA"
country_2 = "China"
country_3 = "India"

# GLOBAL list of countries
list_world_nations = ["Argentina", "Italy", "Australia"]

# GLOBAL tuple of countries
tuple_world_nations = ("Spain", "France", "Canada")

# GLOBAL dictionary with country entries
dictionary_world_nations = {
    'Country_1': 'Brazil',
    'Country_2': 'Germany',
    'Country_3': 'Japan'
}

# GLOBAL function to add two numbers
def module_function_add(in_number1, in_number2):
    """
    This function adds the two input numbers and returns the result.
    """
    return in_number1 + in_number2
```

## Using a Module
* To access/use functions, classes, and variables defined in one module, you must import that module into your script or another module where it is required.
* The keyword `import <module-name>` is used to import a module.
* The keyword `from <module-name> import <function>` enables the developer to import specific objects of a module.
```python
import my_module
# Imports the "my_module" module

# To use objects of my_module, use the syntax module_name.object_name
# Print the "my_module" variables
print (my_module.country_1, my_module.country_2, my_module.country_3);

# Print the "my_module" LIST
print (my_module.list_world_nations);

# print the "my_module" TUPLE
print (my_module.tuple_world_nations);

# print the "my_module" DICTIONARY
print (my_module.dictionary_world_nations);

# Calling a function from the "my_module"
print (my_module.module_function_add(1, 3));

# Output: USA China India
#         ['Argentina', 'Italy', 'Australia']
#         ('Spain', 'France', 'Canada')
#         {'Country_1': 'Brazil', 'Country_2': 'Germany', 'Country_3': 'Japan'}
#         4
```

## Importing Module Content
* You can also import specific attributes from a module directly, without importing completely.
```python
from my_module import country_1, dictionary_world_nations, module_function_add
# This imports only country_1 variable,
# dictionary_world_nations dictionary variable and module_function_add function

# We can use the imported objects directly without using
# the syntax module_name.object_name
# Print the "my_module" variables
print (country_1);

# Uncomment and try to use not imported object, will give an error
# print (country_2);

# print the "my_module" DICTIONARY
print (dictionary_world_nations);

# Calling a function from the "my_module"
print (module_function_add(1, 3));

# Output: USA
#         {'Country_1': 'Brazil', 'Country_2': 'Germany', 'Country_3': 'Japan'}
#         4
```

## Aliasing Modules
* For modules with longer names or for convenience, you can use aliases for better understanding and usability.
```python
import my_module as m1
# Imports the "my_module" module as "m1"

# Print the "my_module" variables
print (m1.country_1, m1.country_2, m1.country_3);

# Print the "my_module" LIST
print (m1.list_world_nations);

# print the "my_module" TUPLE
print (m1.tuple_world_nations);

# print the "my_module" DICTIONARY
print (m1.dictionary_world_nations);

# Calling a function from the "my_module"
print (m1.module_function_add(1, 3));

# Output: USA China India
#         ['Argentina', 'Italy', 'Australia']
#         ('Spain', 'France', 'Canada')
#         {'Country_1': 'Brazil', 'Country_2': 'Germany', 'Country_3': 'Japan'}
#         4
```

## Standard Library Modules
* Python comes with a vast standard library of modules that you can use in your programs.
* For example, the `math` module includes mathematical functions:
```python
import math

print(math.sqrt(16))
print(math.pi)

# Output: 4.0
#         3.141592653589793
```

## Packages
* When your application's code grows larger, you might need to organize multiple modules into a package. A package is a directory with Python modules and a special `__init__.py` file.

**Example structure:**
```
my_package/
│
├── __init__.py
└── sub_module.py
```
* Where `sub_module.py` might look like this:
```python
def sub_greet(name):
    print(f"Hello from the sub-module, {name}!")
```
* You can use it like this
```python
from my_package.sub_module import sub_greet

sub_greet("Dave")
# Output: Hello from the sub-module, Dave!
```

## Benefits of Using Modules
* **Code Organization:** Modules help organize your code into logical components, improving readability and maintainability.
* **Code Reusability:** Functions and classes defined in modules can be reused across different parts of your program or even in different projects.
* **Collaboration:** Modules allow multiple developers to work on different parts of a project simultaneously without interfering with each other's code.
* **Encapsulation:** You can encapsulate related code and hide implementation details, exposing only what's necessary to the user.

##### [Back To Context](../../README.md)