![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# Custom Module Folder
* Python Custom Module Folder or a Package are collection of python files placed in one DIRECTORY (Name with No Spaces), This DIRECTORY name becomes the module name.
* Essentially, a custom module folder or package serves as a container for organizing related Python code files.
* Each file within this directory typically may contains functions, classes, or variables that serve a specific purpose or contribute to a particular aspect of functionality within the module.
* By organizing code in this manner, developers can better manage and maintain their projects, promoting modularity, reusability, and overall code cleanliness.

## Creating Custom Module Folder
* **Define Python Files:** 
    * First, you'll create one or more Python files within a directory.
    * These files contain the functions, classes, and variables that you want to include in your module.
* **Create `__init__.py`:**
    *  Next, create an empty file named `__init__.py` within the same directory.
    * This file serves as an indicator to Python that the directory should be treated as a module.
    * It essentially marks the directory as a package, allowing you to import its contents in other Python files.
* **Naming:**
    * The name of the directory (the folder) becomes the name of the module.
    * Ensure that the directory name follows Python naming conventions and does not contain any spaces.
* **Importability:**
    * Once you've completed the above steps, the functions, classes, and variables defined in the Python files within this directory become importable in other Python scripts or modules.
* **Using `__all__`:** 
    * Optionally, you can use a special directive called `__all__` within the `__init__.py` file.
    * By setting `__all__` to a list of module names or strings, loads all the modules to the memory or you specify which modules should be imported when someone uses the `from module import *` syntax.
    * This can be helpful for controlling what gets exposed when importing your module.

## Demonstration/Example for Creating Custom Module Folder
* Create a folder with your module name, say "MathCalc". (Don't use spaces or spl characters in the folder name, also don't start with numbers)
* **Create python file:** `add2nums.py`
```python
def add2nums(num1, num2):
    print(num1+num2)
```
* **Create python file:** `mul2nums.py`
```python
def mul2nums(num1, num2):
    print(num1*num2)
```
* **Create python file:** `sub2nums.py`
```python
def sub2nums(num1, num2):
    print(num1-num2)
```
* Add your python files, `add2nums.py`, `mul2nums.py`, `sub2nums.py` to the **MathCalc** directory.
* Create an empty file with name `__init__.py`.
* This makes the folder a module, below is the folder structure.
```
MathCalc/
│
├── __init__.py
├── add2nums.py
├── mul2nums.py
└── sub2nums.py
```

**Testing the module MathCalc**
* Create a `MathCalcCaller.py` to test the module `MathCalc`
* The `MathCalcCaller.py` must be in the same folder as Module Folder, for say:
    * `c:\code\tinitiate\MathCalc`
    * `c:\code\tinitiate\MathCalcCaller.py`
```python
from MathCalc import add2nums, mul2nums, sub2nums

add2nums.add2nums(10,20)
mul2nums.mul2nums(20,30)
sub2nums.sub2nums(40,10)
# OUTPUT: 30
#         600
#         30
```

## Custom module folder with `__all__` in `__init__.py` file
* The `__all__` list, when placed in the `__init__.py` file within a module folder, specifies which members of the module should be made accessible to users when they import the module.
    * Creating folder with module name as `MathCalcInit_all`
    * Create module files
    * **Create python file:** `__init.py__`
    ```python
    __all__ = ['add2nums', 'mul2nums']
    ```
    * **Create python file:** `add2nums.py`
    ```python
    def add2nums(num1, num2):
        print(num1+num2)
    ```
    * **Create python file:** `mul2nums.py`
    ```python
    def mul2nums(num1, num2):
        print(num1*num2)
    ```
    * **Create python file:** `sub2nums.py`
    ```python
    def sub2nums(num1, num2):
        print(num1-num2)
    ```
* When you import the module using syntax like from `MathCalcInit_all import *`, if `__all__` is specified only the members listed in the `__all__` list will be available for use outside the module, if not specified everything will be available.
* **Module Caller file:**  `MathCalcInit_all_caller.py`
```python
from MathCalcInit_all import *

add2nums.add2nums(10,20)
mul2nums.mul2nums(20,30)
# Uncomment the below, will give an error
# sub2nums.sub2nums(40,10)
# OUTPUT: 30
#         600
```

## Module Executable and Import
* A python module can be called as an executable and also be called as import.
* The `if __name__ == "__main__":` construct in Python enables a script to serve dual purposes: it can be utilized as a module by other scripts, while also capable of running independently as a standalone script.
* `__main__` is a predefined variable in Python that stores information about the currently executing program. On the other hand, `__name__` is another built-in variable that holds the name of the current Python module or script.
* So, when `__name__` equals `"__main__"`, it indicates that the current script is being executed directly, rather than being imported as a module into another script.
* This condition is often utilized to include code blocks that should only execute when the script is run directly, allowing the script to perform certain tasks or functions specifically meant for standalone execution.

**Create the custom module - `addition_module.py`:**
* Inside this module, we'll define a function called `add_variables()` that adds two variables. When this module is imported elsewhere, it should allow the user to pass values to add.
```python
def add_variables(var1=0, var2=0):
    """Add two variables and return the result."""
    return var1 + var2

if __name__ == "__main__":
    # This block of code will only run if this script is executed directly
    # and not when it's imported as a module.
    
    # You can use this block to test the functionality if needed.
    value1 = int(input("Enter the first number: "))
    value2 = int(input("Enter the second number: "))
    
    result = add_variables(value1, value2)
    print(f"The sum is: {result}")
# OUTPUT: Enter the first number: 3
#         Enter the second number: 4
#         The sum is: 7
```

**Use the custom module in another script:**
* Now, you can use the `addition_module.py` as a module in another script with name `addition_module_caller_script.py`.
```python
import addition_module

# Using the function from the module with default values
result_default = addition_module.add_variables()
print(f"Default sum is: {result_default}")

# Using the function from the module with custom values
value3 = 5
value4 = 3
result_custom = addition_module.add_variables(value3, value4)
print(f"Custom sum is: {result_custom}")
# OUTPUT: Default sum is: 0
#         Custom sum is: 8
```

## Custom Module Folder Executable and Import
* Adding a `__main__.py` file to a custom module folder will make it executable.
* A Python custom module folder program can be run by the command line `python -m NameOfTheModuleFolder`
```
MathModule/
│
├── __init__.py
├── __main__.py
├── add_variables.py
└── multiply_variables.py
```
**Creating custom module folder files:**
* Create `__init__.py` file.
* Creating `add_variables.py` file which contains the function to add two numbers.
```python
def add_variables(var1=0, var2=0):
    """Add two variables and return the result."""
    return var1 + var2
```
* Creating `multiply_variables.py` file which contains the function to multiply two numbers.
```python
def multiply_variables(var1=1, var2=1):
    """Multiply two variables and return the result."""
    return var1 * var2
```
* Creating `__main__.py` file which will be the entry point that demonstrates the functionalities of both modules.
```python
from . import add_variables
from . import multiply_variables

def main():
    # Using the add_variables function from MathModule
    value1 = int(input("Enter the first number for addition: "))
    value2 = int(input("Enter the second number for addition: "))
    result_add = add_variables.add_variables(value1, value2)
    print(f"The sum is: {result_add}")

    # Using the multiply_variables function from MathModule
    value3 = int(input("Enter the first number for multiplication: "))
    value4 = int(input("Enter the second number for multiplication: "))
    result_multiply = multiply_variables.multiply_variables(value3, value4)
    print(f"The product is: {result_multiply}")

if __name__ == "__main__":
    # This block will only execute if this script (__main__.py) is run directly.
    main()
# OUTPUT: Enter the first number for addition: 1
#         Enter the second number for addition: 2
#         The sum is: 3
#         Enter the first number for multiplication: 3
#         Enter the second number for multiplication: 4
#         The product is: 12
```

**Run a custom module folder:**
* To execute the package as a script and see the functionalities, navigate to the directory containing these files(here we have created `MathModule` folder) in command prompt and run:
```bash
# Run using syntax python -m ModuleName
python -m MathModule
```

## `main()` Function
* The `main()` function is a special function in Python that serves as the entry point of a program. It is the function that is executed when the program is run.
* The `main()` function typically contains the top-level logic of the program, including the initialization of variables, the invocation of other functions, and the handling of any exceptions that might occur.
* In Python, the `main()` function is often implemented using a conditional statement that checks whether the current module is being run as the main program. 
* This is done using the `if __name__ == "__main__":` statement.
* If this condition is true, then the code within the block following the statement is executed.
```python
def main():
    print("Hello, world!")

if __name__ == "__main__":
    main()
```
* While it is common to name the entry point function in a Python program `main()`, it is not strictly required.
* We can name the entry point function whatever you like, as long as you indicate it as the entry point using the `if __name__ == "__main__":` statement.
```python
def start():
    # Initialization code goes here
    print("Starting program...")
    # Main program logic goes here

if __name__ == "__main__":
    start()
```
### Using `if __name__ == "__main__"` statement
* The `if __name__ == "__main__"` statement is a special statement in Python that is used to control the execution of code. 
* When the `if __name__ == "__main__"` statement is executed, the code inside the `if` block will only be executed if the script is being run as the main program.
* If the script is being imported as a module, the code inside the `if` block will not be executed.
* If the script is imported as a module, the `main()` function will not be called and no output will be displayed.
* The `if __name__ == "__main__"` statement is a powerful tool that can be used to control the execution of code in Python scripts.
```python
# math_functions.py
import math

def square_root(n):
    return math.sqrt(n)

def main():
    n = float(input("Enter a number: "))
    result = square_root(n)
    print("The square root of", n, "is", result)

if __name__ == "__main__":
    main()
```
```python
# my_program.py
from math_functions import square_root

n = 16
result = square_root(n)
print("The square root of", n, "is", result)
```
* In this case, the `if __name__ == "__main__":` statement in `math_functions.py` prevents the code in the `main()` function from executing when the module is imported into `my_program.py`. This ensures that the user input prompt and output statements in `main()` are not executed when the `square_root()` function is imported and used in another program.
* Instead, only the code within the `square_root()` function is executed when it is called from `my_program.py`, and the user input and output statements in `main()` are not executed. This allows you to reuse the `square_root()` function without executing the entry point function when it is not intended to be run.
```python
# math_functions1.py
import math

def square_root(n):
    return math.sqrt(n)

def power(x, n):
    return x ** n

def main():
    n = float(input("Enter a number: "))
    x = float(input("Enter a power: "))
    result1 = square_root(n)
    result2 = power(x, n)
    print("The square root of", n, "is", result1)
    print(x, "raised to the power of", n, "is", result2)

if __name__ == "__main__":
    main()
```
```python
# my_program1.py
from math_functions1 import square_root, power

n = 16
x = 2
result1 = square_root(n)
result2 = power(x, n)
print("The square root of", n, "is", result1)
print(x, "raised to the power of", n, "is", result2)
```
* In this example, the `square_root()` and `power()` functions from `math_functions.py` are imported into `my_program.py` using the `from math_functions import square_root, power` statement. The functions are then called to perform their respective operations on the input values, and the results are printed to the console.
* In this way, the `if __name__ == "__main__":` statement in `math_functions.py` ensures that the user input prompt and output statements in the `main()` function are not executed when the module is imported into `my_program.py`, and only the definitions of the `square_root()` and `power()` functions are imported and used.
### Not using `if __name__ == "__main__":` statement
```python
# math_functions2.py
import math

def square_root(n):
    return math.sqrt(n)

def power(x, n):
    return x ** n

def main():
    n = float(input("Enter a number: "))
    x = float(input("Enter a power: "))
    result1 = square_root(n)
    result2 = power(x, n)
    print("The square root of", n, "is", result1)
    print(x, "raised to the power of", n, "is", result2)

main()
```
```python
# my_program2.py
from math_functions2 import square_root, power

n = 16
x = 2
result1 = square_root(n)
result2 = power(x, n)
print("The square root of", n, "is", result1)
print(x, "raised to the power of", n, "is", result2)
```
* In this example, when you run `my_program.py`, the `main()` function in `math_functions.py` will be executed, and the user input prompt and output statements will be printed to the console, even though they are not relevant to `my_program.py`. 
* To avoid this issue, it's a good practice to always use the `if __name__ == "__main__":` statement in your main program, as shown in the previous examples, to ensure that the entry point code is only executed when the module is run as the main program, and not when it is imported as a module into another program.

## Accessing modules from a different or custom directory path
* To import the Module from a different folder, use syntax `import sys` and the absolute path of the folder.
```python
import sys
sys.path.append('/path/to/module-folder')
from module_name import module_function
```

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
