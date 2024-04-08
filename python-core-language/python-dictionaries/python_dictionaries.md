![Python Tinitiate Image](../../python_tinitiate.png)
# Python Tutorial
&copy; TINITIATE.COM
##### [Back To Context](../../README.md)

# Python Dictionaries
* Dictionaries in Python are unordered collections of key-value pairs.
* It's a versatile data structure used to store and retrieve data efficiently.
* They are mutable, meaning their elements can be changed after the dictionary is created.
* Unlike sequences (like lists and tuples), which are indexed by a range of numbers, Dictionaries are used to store data in the form of key-value pairs, where each key is unique and maps to a corresponding value. 

## Creating Dictionaries
* Dictionaries can be created by enclosing key-value pairs within curly braces `{}` or by using the `dict()` constructor, where each key is followed by a colon `:` and its corresponding value.
```python
eats = {'APPLE':'FRUIT', 'POTATO':'ROOT', 'OKRA':'VEGETABLE'}
print(eats) 
# Output: {'APPLE': 'FRUIT', 'POTATO': 'ROOT', 'OKRA': 'VEGETABLE'}

my_dict = {'name': 'John', 'age': 30, 'gender': 'Male'}
print(my_dict)
# Output: {'name': 'John', 'age': 30, 'gender': 'Male'}

# Empty Dictionary
dict0 = {}
print(dict0)
# Output: {}
```

## Accessing Elements
* Individual elements in a dictionary can be accessed using keys.
```python
my_dict = {'name': 'John', 'age': 30, 'gender': 'Male'}

print(my_dict['name'])    
# Output: John

print(my_dict['age'])     
# Output: 30

print(my_dict.get('gender'))  
# Output: Male
```

## Modifying Dictionaries
* You can modify elements in a dictionary by assigning new values to existing keys or adding new key-value pairs.
* You can remove a key-value pair from a dictionary, you can use the `del` statement.
* Use `key()` to get all the keys in dictionary.
* Use `clear()` to remove everything in dictionary.
```python
my_dict = {'name': 'John', 'age': 30}
print(my_dict)
# Output: {'name': 'John', 'age': 30}

# Modifying existing value
my_dict['age'] = 35
print(my_dict)
# Output: {'name': 'John', 'age': 35}

# Adding new key-value pair
my_dict['gender'] = 'Male'
print(my_dict)  
# Output: {'name': 'John', 'age': 35, 'gender': 'Male'}

# Remove the key gender and its value
del my_dict['gender'] 
print(my_dict)
# Output: {'name': 'John', 'age': 35}

# Remove everything in dictionary
my_dict.clear() 
print(my_dict)
# Output: {}
```

## Dictionary Methods
* Python provides many built-in methods for dictionary manipulation, such as keys(), values(), items(), pop(), popitem().
my_dict = {'name': 'John', 'age': 30, 'gender': 'Male'}
    * `keys()`: Returns a view object containing the keys of the dictionary
    * `values()`: Returns a view object containing the values of the dictionary
    * `items()`: Returns a view object containing the key-value pairs of the dictionary
    * `pop()`: Removes the item with the specified key and returns its value
    * `popitem()`: Removes and returns the last inserted key-value pair
```python
my_dict = {'name': 'John', 'age': 30, 'gender': 'Male'}

# keys()
print(my_dict.keys())  
# Output: dict_keys(['name', 'age', 'gender'])

# values()
print(my_dict.values())  
# Output: dict_values(['John', 30, 'Male'])

# items()
print(my_dict.items())   
# Output: dict_items([('name', 'John'), ('age', 30), ('gender', 'Male')])

# pop()
value = my_dict.pop('age')
print(value)  
# Output: 30
print(my_dict)  
# Output: {'name': 'John', 'gender': 'Male'}

# popitem()
key, value = my_dict.popitem()
print(key, value)  
# Output: gender Male
print(my_dict)     
# Output: {'name': 'John'}
```

## Dictionary Comprehensions
* Dictionary comprehensions provide a concise way to create dictionaries based on existing dictionaries.
```python
numbers = {1, 2, 3, 4, 5}
numbers_dict = {x: x ** 2 for x in numbers}  
#OUTPUT: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(numbers_dict)
```

## Nested Dictionaries
* Dictionaries can contain other dictionaries as values, enabling the creation of nested data structures.
* You can use indexing to access elements in list of dictionaries.
```python
# Nested dict variation 1
my_dict = {'person': {'name': 'John', 'age': 30}}

print(my_dict)
# Output: {'person': {'name': 'John', 'age': 30}}

print(my_dict['person'])
# Output: {'name': 'John', 'age': 30}

print(my_dict['person']['name'])  
# Output: John

print(my_dict['person']['age'])   
# Output: 30


# Nested dict variation 2
list_dict = [{'EmpID':1, 'EmpName':'Venkat'},
             {'EmpID':2, 'EmpName':'Sujatha'},
             {'EmpID':3, 'EmpName':'Taran'}]

# Print Name of EmpID: 3 using indexing
# EmpID: 3 is 3rd element, whose index is "2"
print(list_dict[2]['EmpName'])
# Output: Taran
```

## Conclusion
* Dictionaries provide a flexible and efficient way to store and manipulate data using key-value pairs.
* Note that dictionaries are unordered, which means the order of key-value pairs might not be preserved. Starting from Python 3.7, the insertion order is preserved by default.

##### [Back To Context](../../README.md)