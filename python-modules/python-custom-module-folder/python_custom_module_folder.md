![Python Tinitiate Image](../../python_tinitiate.png)
# Python Tutorial
&copy; TINITIATE.COM
##### [Back To Contents](../../README.md)

# Python Custom Module Folder
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

# Output: 30
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

# Output: 30
#         600
```

## Python Module Executable and Import
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

# Output: Enter the first number: 3
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

# Output: Default sum is: 0
#         Custom sum is: 8
```

## Python Custom Module Folder Executable and Import
* Adding a `__main__.py` file to a custom module folder will make it executable.
* A Python custom module folder program can be run by the command line `python -m NameOfTheModuleFolder`

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

# Output: Enter the first number for addition: 1
#         Enter the second number for addition: 2
#         The sum is: 3
#         Enter the first number for multiplication: 3
#         Enter the second number for multiplication: 4
#         The product is: 12
```

**Run a custom module folder:**
* To execute the package as a script and see the functionalities, navigate to the directory containing these files in command prompt and run:
```bash
# Run using syntax python -m ModuleName
python -m MathModule
```

## Accessing Python modules from a different or custom directory path
* To import the Module from a different folder, use syntax `import sys` and the absolute path of the folder.
```python
import sys
sys.path.append('/path/to/module-folder')
```

##### [Back To Contents](../../README.md)