![Python Tinitiate Image](../../python_tinitiate.png)
# Python Tutorial
&copy; TINITIATE.COM
##### [Back To Context](../../README.md)

# Conversions Between Dictionaries, Lists And Tuples
* Converting between dictionaries, lists, and tuples is a common operation in Python and can be done using various methods.
* This is essential in many cases to convert complex types to simple types.

## Converting List to Tuple
* You can convert a list to a tuple using the `tuple()` constructor.
```python
my_list = ['John', 30, 'Male']
print(my_list)
# Output: ['John', 30, 'Male']

my_tuple = tuple(my_list)
print(my_tuple)  
# Output: ('John', 30, 'Male')
```

## Converting List to Dictionary
* You can convert a list to a dictionary where each consecutive pair of elements in the list forms a key-value pair.
```python
my_list = ['name', 'John', 'age', 30, 'gender', 'Male']
print(my_list)
# Output: ['name', 'John', 'age', 30, 'gender', 'Male']

my_dict = {my_list[i]: my_list[i + 1] for i in range(0, len(my_list), 2)}
print(my_dict)  
# Output: {'name': 'John', 'age': 30, 'gender': 'Male'}
```

## Converting List of Tuples to Dictionary
* You can convert a list of tuples to a dictionary where each tuple represents a key-value pair using the `dict()` constructor.
```python
list_of_tuples = [('name', 'John'), ('age', 30), ('gender', 'Male')]
print(list_of_tuples)
# Output: [('name', 'John'), ('age', 30), ('gender', 'Male')]

my_dict = dict(list_of_tuples)
print(my_dict)  
# Output: {'name': 'John', 'age': 30, 'gender': 'Male'}
```

## Converting a List of Tuples to a Tuple of Lists
* If you have a list of tuples and want to separate the elements of the tuples into separate lists within a tuple, you can use list comprehension and the zip() function.
```python
tuple_list = [(1, "a"), (2, "b"), (3, "c")]
int_list, char_list = zip(*tuple_list)
# '*' symbol zips all
print(tuple_list)
# Output: [(1, 'a'), (2, 'b'), (3, 'c')]

tuple_of_lists = (list(int_list), list(char_list))
print(tuple_of_lists) 
# Output: ([1, 2, 3], ['a', 'b', 'c'])
```

## Converting Tuple to List
* You can convert a tuple to a list using the `list()` constructor.
```python
my_tuple = ('John', 30, 'Male')
print(my_tuple)
# Output: ('John', 30, 'Male')

my_list = list(my_tuple)
print(my_list)  
# Output: ['John', 30, 'Male']
```

## Converting Tuple of Tuples to Dictionary
* You can convert tuple of tuples to dictionary using `dict()` constructor.
```python
tuple1 = (('a', 1),('b', 2))
print(tuple1)
# Output: (('a', 1), ('b', 2))

dict1 = dict(tuple1)
print(dict1) 
# Output: {'a': 1, 'b': 2}
```

## Converting a Tuple of Lists to a Dictionary
* To create a dictionary from a tuple containing lists of keys and values, you can use a combination of `zip()`(is used to combine multiple iterables) and the `dict()` constructor.
```python
tuple_of_lists = (["a", "b", "c"], [1, 2, 3])
print(tuple_of_lists)
# Output: (['a', 'b', 'c'], [1, 2, 3])

keys_list, values_list = tuple_of_lists
my_dict = dict(zip(keys_list, values_list))
print(my_dict) 
# Output: {'a': 1, 'b': 2, 'c': 3}
```

## Converting a Tuple of Lists to a List of Tuples
* To reverse the process and convert a tuple of lists back to a list of tuples, you can use the zip() function again.
```python
tuple_of_lists = ([1, 2, 3], ["a", "b", "c"])
print(tuple_of_lists)
# Output: ([1, 2, 3], ['a', 'b', 'c'])

list_of_tuples = list(zip(*tuple_of_lists))
print(list_of_tuples)
# Output: [(1, 'a'), (2, 'b'), (3, 'c')]
```

## Converting Dictionary to List of Tuples
* You can convert a dictionary to a list of tuples where each tuple contains a key-value pair from the dictionary using the `items()` method.
```python
my_dict = {'name': 'John', 'age': 30, 'gender': 'Male'}
print(my_dict)
# Output: {'name': 'John', 'age': 30, 'gender': 'Male'}

list_of_tuples = list(my_dict.items())
print(list_of_tuples)  
# Output: [('name', 'John'), ('age', 30), ('gender', 'Male')]
```

## Converting Dictionary to List of Keys or Values
* You can convert a dictionary to a list of its keys or values using the `keys()` and `values()` methods.
```python
my_dict = {'name': 'John', 'age': 30, 'gender': 'Male'}
print(my_dict)
# Output: {'name': 'John', 'age': 30, 'gender': 'Male'}

keys_list = list(my_dict.keys())
print(keys_list)  
# Output: ['name', 'age', 'gender']

values_list = list(my_dict.values())
print(values_list)  
# Output: ['John', 30, 'Male']
```

## Converting Dictionary to a Tuple of Lists
* You can convert a dictionary to a list and then those lists to a tuple.
```python
my_dict = {'name': 'John', 'age': 30, 'gender': 'Male'}
print(my_dict)
# Output: {'name': 'John', 'age': 30, 'gender': 'Male'}

keys_list = list(my_dict.keys())
print(keys_list)  
# Output: ['name', 'age', 'gender']

values_list = list(my_dict.values())
print(values_list)  
# Output: ['John', 30, 'Male']

tuple_of_lists = (keys_list, values_list)
print(tuple_of_lists) 
# Output: (['name', 'age', 'gender'], ['John', 30, 'Male'])
```

## Conclusion
* Conversions between dictionaries, tuples, and lists in Python involves using various methods and techniques.
* This flexibility allows you to manipulate your data structures as needed in your programs.

##### [Back To Context](../../README.md)