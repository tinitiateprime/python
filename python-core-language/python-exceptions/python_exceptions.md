![Python Tinitiate Image](../../python_tinitiate.png)
# Python Tutorial
&copy; TINITIATE.COM
##### [Back To Contents](../../README.md)

# Python Exceptions
* In Python, exceptions are unexpected or erroneous events(errors) that occur during the execution of a program, leading to abnormal termination of the normal flow of the program's instructions if not handled properly.
* They usually arise due to errors or exceptional conditions that the programmer might not have anticipated.
* Python provides a mechanism for detecting, handling, and raising exceptions, allowing developers to gracefully manage errors and exceptions in their code to prevent your program from crashing unexpectedly.

## Exception Hierarchy
* In Python, exceptions are organized in a hierarchy, where each exception class is a subclass of another exception class.
* With a base BaseException class at the top, different types of exceptions are derived from this base class, forming a tree-like structure.
* This hierarchy allows for more granular exception handling, where specific exceptions can be caught and handled differently from more general ones.
* This hierarchy allows developers to catch specific exceptions based on the nature of the error and handle them accordingly, improving the robustness and clarity of Python programs.
### BaseException:
* This is the base class for all built-in exceptions. It is not meant to be directly inherited by user-defined exceptions.
### Exception:
* This is the base class for all built-in, non-system-exiting exceptions. User-defined exceptions should typically inherit from this class.
    - **StandardError**: This class is the base class for all built-in exceptions except `StopIteration`, `SystemExit`, `KeyboardInterrupt`, and `GeneratorExit`.
        - **ArithmeticError**: This class is the base class for numeric errors.
        
            - **ZeroDivisionError**: Raised when division or modulo by zero occurs.
            - **OverflowError**: Raised when arithmetic operation exceeds the limits of the data type.
            - **FloatingPointError**: Raised when a floating-point operation fails.

        - **LookupError**: This class is the base class for errors raised when a key or index is not found.
            
            - **IndexError**: Raised when a sequence subscript is out of range.
            - **KeyError**: Raised when a dictionary key is not found.
        
        - **AssertionError**: Raised when an `assert` statement fails.
        - **TypeError**: Raised when an operation or function is applied to an object of inappropriate type.
        - **ValueError**: Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.
        - **NameError**: Raised when a local or global name is not found.
        - **IOError**: Raised when an I/O operation (such as reading or writing to a file) fails.
        - **OSError**: Raised when a system-related operation (such as file I/O) fails.
        - **EOFError**: Raised when the `input()` function hits an end-of-file condition.
        - **RuntimeError**: Raised when an error is detected that doesn't fall in any of the other categories.
### StopIteration:
* Raised by built-in function `next()` to indicate that there are no further items to be returned by an iterator.
### SystemExit:
* Raised by the `sys.exit()` function to terminate the program.
### KeyboardInterrupt:
* Raised when the user interrupts the execution of the program, usually by pressing `Ctrl+C`.
### GeneratorExit:
* Raised when a generator's `close()` method is called.

## Handling Exceptions
* You can use a `try` and `except` blocks to handle exceptions in Python.
* The try block contains the code that might raise an exception, and the except block catches and handles the exception if it occurs.
```python
# Example 1:
try:
    # Code that might raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # Code to handle the exception
    print("Error: Division by zero")
# Output: Error: Division by zero


# Example 2:
try:
    result = "10" / 2
except TypeError:
    print("Error: Unsupported operand type(s) for /: 'str' and 'int'")
# Output: Error: Unsupported operand type(s) for /: 'str' and 'int'


# Example 3:
try:
    my_list = [1, 2, 3]
    print(my_list[4])
except IndexError:
    print("Error: Index out of range")
# Output: Error: Index out of range


# Example 4:
try:
    my_dict = {"a": 1, "b": 2}
    value = my_dict["c"]
except KeyError:
    print("Error: Key not found")
# Output: Error: Key not found


# Example 5:
try:
    v = 1/0
except Exception as e:
    print(type(e).__name__, e)
# type() function returns the type of the specified object as a type object.
# type(e).__name__ prints the name of the exception class
# e prints the actual exception instance
# Output: ZeroDivisionError division by zero
```

## Handling Multiple Exceptions
* You can handle multiple exceptions by providing multiple `except` blocks or using a single except block that handles a tuple of exception types.
```python
# Example 1:
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ValueError:
    # Handle ValueError
    print("An error occurred 1:")
except ZeroDivisionError:
    # Handle ZeroDivisionError
    print("An error occurred 2:")
except Exception as e:
    # Catch all other exceptions
    print("An error occurred3 :", e)
# Output: An error occurred 2:


# Example 2:
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")

# Input: 0
# Output: Invalid input or division by zero.


# Example 3:
try:
    my_dict = {"a": 1, "b": 2}
    value = my_dict["c"]  # This will raise a KeyError
    my_list = [1, 2, 3]
    print(my_list[4])  # This will raise an IndexError
except (KeyError, IndexError):
    print("Error: Key not found or index out of range")
# Output: Error: Key not found or index out of range


# Example 4:
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    print("Error: Please enter valid integers")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
except Exception as e:
    print("An error occurred:", e)

# Input 1: a
# Input 2: 1 
# Output: Error: Please enter valid integers

# Input 1: 1
# Input 2: 0
# Output: Error: Division by zero is not allowed
```

## Using `else` and `finally`
* The `else` block is executed when no exceptions are raised in the try block. It's often used to place code that should run only if the try block completes successfully.
* The `finally` block contains code that is executed no matter what, whether an exception occurred or not. It's used for cleanup operations, like closing files or releasing resources.
```python
# Example 1:
try:
    v = 1/1  # Trying to Divide By zero
except ZeroDivisionError:
    print("Tinitiate: Cannot Divide by ZERO")
else:
    print("Tinitiate: Execution completed successfully")
# Output: Tinitiate: Execution completed successfully


# Example 2:
try:
    v = 1/1  # Trying to Divide By zero
except ZeroDivisionError:
    print("Tinitiate: Cannot Divide by ZERO")
finally:
    print("Tinitiate: THIS MESSAGE MUST BE PRINTED")
# Output: Tinitiate: THIS MESSAGE MUST BE PRINTED


# Example 3:
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Division by zero")
else:
    print("Result:", result)
finally:
    print("Execution complete")
    
# Output: Result: 5.0
#         Execution complete


# Example 4:
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    print(f"Result: {result}")
finally:
    print("Execution complete.")

# Input : 2
# Output: Result: 5.0
#         Execution complete.

# Input : 0
# Output: Division by zero is not allowed.
#         Execution complete.


# Example 5:
try:
    x = int(input("Enter a number: "))
    result = 10 / x
    items = [1, 2, 3]
    value = items[x]
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Division by zero")
except IndexError:
    print("Error: Index out of range")
else:
    print("Result:", result)
    print("Value at index", x, ":", value)
finally:
    print("Execution complete")

# Input : 2
# Output: Result: 5.0
#         Value at index 2 : 3
#         Execution complete
```

## Raising Exceptions
* You can `raise` exceptions manually using the raise statement to indicate exceptional conditions in your code.
```python
x = -5
if x < 0:
    raise ValueError("x cannot be negative")
# Output: ValueError: x cannot be negative
```

## Custom Exceptions
* You can also create custom exception classes by subclassing built-in exception classes or the Exception class.
* This is useful when you want to raise exceptions specific to your program's logic.
```python
# Example 1:
class CustomError(Exception):
    pass        # Placeholder for class implementation

raise CustomError("An error occurred")
# Output: CustomError: An error occurred


# Example 2:
class tinitiate_exception(Exception):pass

# Block to test the user defined exception
try:
    raise tinitiate_exception
except tinitiate_exception:
    print("This is a user defined exception !")
# Output: This is a user defined exception !


# Example 3:
try:
    a=1/0
except:
    pass  # This will do nothing
# Pass can be used as placeholder for class and functions,
# and also to do nothing(ignore errors) in try or except block.


# Example 4:
try:
    # Code that may raise an exception
    pass
except SomeException:
    # Ignore the exception
    pass


# Example 5:
class CustomError(Exception):
    pass

def process_data(data):
    if not data:
        raise CustomError("No data provided!")

try:
    process_data(None)
except CustomError as ce:
    print(ce)
# Output: No data provided!


# Example 6:
class InsufficientFundsError(Exception):
    pass

class Account:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError
            ("Insufficient funds to withdraw " + str(amount))
        self.balance -= amount
        print("Withdrawal successful. Remaining balance:", self.balance)

try:
    acc = Account(1000)
    acc.withdraw(1500)
except InsufficientFundsError as e:
    print("Error:", e)
# Output: Error: 


# Example 7:
class CustomError(Exception):
    pass

try:
    raise CustomError("An error occurred")
except CustomError as e:
    print("Custom error:", e)
# Output: Custom error: An error occurred


# Example 8:
# Custom exception with additional attributes
class CustomError(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code

try:
    raise CustomError("An error occurred", 500)
except CustomError as e:
    print("Custom error:", e)
    print("Error code:", e.code)
# Output: Custom error: An error occurred
#         Error code: 500


# Example 9:
class ti_exception_1(Exception):pass
class ti_exception_2(Exception):pass

# Block to test the user defined exception
try:
    raise ti_exception_1
except ti_exception_1:
    # Exception handler for user defined exception: ti_exception_1
    print("This is a user defined exception 1 Handler !")
except ti_exception_2:
    # Exception handler for user defined exception: ti_exception_2 
    print("This is a user defined exception 2 Handler !")
# Output: This is a user defined exception 1 Handler !
```

## Conclusion
* Handling exceptions in Python is a crucial aspect of writing robust and reliable code.
* By anticipating potential errors and implementing appropriate exception handling mechanisms, developers can gracefully manage unexpected situations and prevent their programs from crashing.

##### [Back To Contents](../../README.md)