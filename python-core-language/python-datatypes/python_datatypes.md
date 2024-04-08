![Python Tinitiate Image](../../python_tinitiate.png)
# Python Tutorial
&copy; TINITIATE.COM
##### [Back To Context](../../README.md)

# Python Datatypes
* Python provides several built-in data types to work with different kinds of data.
* A data type is a classification that specifies the type of data a variable can hold and the operations that can be performed on it.

## Built-in Python DataTypes
Here's a list of datatypes along with examples:

### Numeric Types
- **int**: Integers are whole numbers, positive or negative, without any decimal point.
    * **Example:** `x = 5`

- **float**: Floats represent real numbers and are written with a decimal point dividing the integer and fractional parts.
    * **Example:** `y = 3.14`
- **complex**: Complex numbers are written in the form `a + bj`, where `a` and `b` are floats and `j` represents the imaginary unit.
    * **Example:** `z = 2 + 3j`

### Sequence Types
- **str**: Strings are sequences of characters, enclosed within single quotes (`'`) or double quotes (`"`).
    * **Example:** `name = 'Alice'`

- **list**: Lists are ordered collections of items, which can be of different data types, and are enclosed within square brackets (`[]`).
    * **Example:** `numbers = [1, 2, 3, 4, 5]`
- **tuple**: Tuples are ordered collections of items, similar to lists, but are immutable (their values cannot be changed), and are enclosed within parentheses (`()`).
    * **Example:** `coordinates = (10, 20)`

### Mapping Type/Dictionaries
- **dict**: Dictionaries are unordered collections of items that are stored as key-value pairs, enclosed within curly braces (`{}`).
    * **Example:** `person = {'name': 'Alice', 'age': 30}`

### Set Types
- **set**: Sets are unordered collections of unique items, enclosed within curly braces (`{}`).
    * **Example:** `unique_numbers = {1, 2, 3, 4, 5}`

- **frozenset**: Frozensets are similar to sets but are immutable (like tuples), and they can be used as dictionary keys.
    * **Example:** `frozen_set = frozenset({1, 2, 3})`

### Boolean Type
- **bool**: Booleans represent truth values and can only have two values: `True` or `False`.
    * **Example:** `is_active = True`

### None Type
- **None**: Represents the absence of a value or a null value.
    * **Example:** `result = None`

```python
# Numeric Types
x = 5                  # int
y = 3.14               # float
z = 2 + 3j             # complex

# Sequence Types
name = 'Alice'         # str
numbers = [1, 2, 3]    # list
coordinates = (10, 20) # tuple

# Mapping Type
person = {'name': 'Bob', 'age': 25}  # dict

# Set Types
unique_numbers = {1, 2, 3}           # set
frozen_set = frozenset({4, 5, 6})    # frozenset

# Boolean Type
is_active = True                      # bool

# None Type
result = None                         # None

# Displaying the values of all variables
print("x:", x)
print("y:", y)
print("z:", z)
print("name:", name)
print("numbers:", numbers)
print("coordinates:", coordinates)
print("person:", person)
print("unique_numbers:", unique_numbers)
print("frozen_set:", frozen_set)
print("is_active:", is_active)
print("result:", result)
```

##### [Back To Context](../../README.md)