![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# Python Tuples
* Tuples in Python are ordered collections of elements, similar to lists, but unlike lists, tuples are immutable, meaning their elements cannot be changed after the tuple is created.
* Tuples can have elements(values) of mixed data types but they are often used to store related pieces of information together and are commonly used in scenarios where immutability and integrity of data are desired.

## Creating Tuples
* Tuples can be created by enclosing comma separated sequence of elements within parentheses `()` or by using the `tuple()` constructor.
```python
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('A', 'b', 1, 2)

# Tuples can also be created without parentheses by using commas alone
tuple3 = 4, 5, 6

# Using tuple() constructor
tuple4 = tuple((1, 22, 333))

# Nested tuples
tuple5 = ((1, 2),(11, 22), (111, 222))

# Printing a tuple
print(tuple1)   # Output: (1, 2, 3, 4, 5)
print(tuple2)   # Output: ('A', 'b', 1, 2)
print(tuple3)   # Output: (4, 5, 6)
print(tuple4)   # Output: (1, 22, 333)
print(tuple5)   # Output: ((1, 2), (11, 22), (111, 222))
```

## Accessing Elements in Tuples
* Individual elements in a tuple can be accessed using indexing, similar to lists.
```python
my_tuple = (1, 2, 3, 4, 5)
#           0  1  2  3  4
print(my_tuple[0])   # Output: 1
print(my_tuple[1])   # Output: 2
print(my_tuple[-1])  # Output: 5 (negative indexing)
```

## Accessing Nested Tuple Elements
* Nested tuples can be accessed using indexing, similar to lists.
```python
my_nested_tuple = ((1, 2), (11, 22), (111, 222))
#                    0       1          2
#                  00  01   10  11    20    21

# First tuple
print(my_nested_tuple[0])       # Output: (1, 2)
# First tuple elements
print(my_nested_tuple[0][0])    # Output: 1
print(my_nested_tuple[0][1])    # Output: 2

# Last tuple
print(my_nested_tuple[2])       # Output: (111, 222)
# Last tuple elements
print(my_nested_tuple[2][0])    # Output: 111
print(my_nested_tuple[2][1])    # Output: 222

# Last tuple using negative indexing
print(my_nested_tuple[-1])      # Output: (111, 222)
# Last tuple elements using negative indexing
print(my_nested_tuple[-1][-2])  # Output: 111
print(my_nested_tuple[-1][-1])  # Output: 222
```

## Tuple Packing and Unpacking
* Tuple packing is the process of creating a tuple without using parentheses, and tuple unpacking is the process of extracting elements from a tuple into separate variables.
```python
# Tuple packing
my_tuple = 1, 2, 3
print(my_tuple)     # Output: (1, 2, 3)

# Tuple unpacking
a, b, c = my_tuple
print(a, b, c)      # Output: 1 2 3
```

## Tuple Methods
* Tuples have limited methods due to their immutability.
* They mainly include methods for counting occurrences and finding indices of elements.
```python
my_tuple = (1, 2, 3, 2)

# count()
print(my_tuple.count(2))  
# Output: 2 (number of occurrences of 2)

# index()
print(my_tuple.index(3))  
# Output: 2 (index of the first occurrence of 3)

# min() and max()
print("Min =",min(my_tuple), "Max =",max(my_tuple)) 
# Output: Min = 1 Max = 3

# len()
print(len(my_tuple)) 
# Output: 4

# sum()
print(sum(my_tuple)) 
# Output: 8
```

## Tuple Slicing
* You can determine the length of a tuple using the `len()` function and slice it to extract a subset of elements.
```python
my_tuple = (1, 2, 3, 4, 5, 6, 7)

print(my_tuple[1:4])
# Output: (2, 3, 4)

print(my_tuple[4:])
# Output: (5, 6, 7)

print(my_tuple[-4:])
# Output: (4, 5, 6, 7)
```

## Tuple Update and Delete
* Tuples are immutable, so to add or update elements in tuples, create a new tuple with parts of existing ones.
* Tuples can be deleted using `del` keyword.
```python
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('A', 'b', 1, 2)

# UPDATE TUPLES
# Easier option for updating parts of tuple are creating 
# new tuples with parts of existing ones
# Create a Tuple with elements 2,3,4 from tuple1
tuple3=tuple1[1:4]
print(tuple3)
# Output: (2, 3, 4)

# DELETING TUPLES 
del tuple3
# print(tuple3) # This will throw an error, as this TUPLE doesnt exist
```

## Tuple Comprehensions
* Tuple comprehensions provide a concise way to create tuples based on existing tuples.
```python
number_tuple = (0, 1, 2, 3, 4)
print(number_tuple)
# Output: (0, 1, 2, 3, 4)

my_tuple = tuple(x ** 2 for x in number_tuple)
print(my_tuple)  
# Output: (0, 1, 4, 9, 16)
```

## Tuple Membership Testing
* Membership testing can be used to check if an element exists in tuple or not.
```python
my_tuple = (1, 2, 3)

print(1 in my_tuple)
# Output: True

print(4 in my_tuple)
# Output: Fasle

print(4 not in my_tuple) 
# Output: True

print(1 not in my_tuple) 
# Output: False
```

## Tuple Immutability
* Tuples are immutable, meaning their elements cannot be changed after the tuple is created.
```python
my_tuple = (1, 2, 3)

# Try to add an element to tuple
# Remove below comment and run
# my_tuple[0] = 4         # This will raise a TypeError
```

## Tuples in Lists
* We can createa a list with tuples nested.
* You can use indexing to access elements in list of tuples.
```python
# Creating a list with tuples in it
list_tup = [(1,2),(11,22),(111,222)]

# Print the 3rd Tuple in the list
print(list_tup[2])

# Print the 2nd Element in 2nd Element of the nested tuple
print(list_tup[1][1])
```

## Tuples Use Cases
* **Tuples are commonly used for:**
    * **Immutable Data:** When you need a collection of data that should not be changed after creation.
    * **Returning Multiple Values:** Functions can return multiple values as a tuple, and these values can be easily unpacked.
    * **Storing Related Data and Ordering Data:** Storing related data that shouldn't be changed, and also When the order of elements matters, and you want to prevent accidental modifications.
    * **Dictionary Keys:** Tuples can be used as keys in dictionaries due to their immutability.
```python
# Returning multiple values from a function
def get_coordinates():
    return 10, 20       # Tuples

x, y = get_coordinates()
print(x, y)                 
# Output: 10 20

# Storing related data
person = ("John", 30, "Male")
print(person)              
# Output: ('John', 30, 'Male')

# Immutable keys in dictionaries
coordinates = {(1, 2): "point"}
print(coordinates[1, 2])    
# Output: point
```

## Conclusion
* Tuples provide a lightweight and immutable way to store related data, and they are widely used in Python programming.
* Remember, while tuples are immutable, the objects they contain might be mutable. This means that if a tuple contains mutable objects like lists, those objects can still be modified.

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
