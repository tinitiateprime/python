![Python Tinitiate Image](../../python_tinitiate.png)
# Python Tutorial
&copy; TINITIATE.COM
##### [Back To Context](../../README.md)

# Python Sets
* Sets in Python are unordered collections of unique elements(no duplicate entries).
* Sets are useful for tasks that involve membership testing, eliminating duplicate entries, and performing mathematical set operations.

## Creating Sets
* Sets can be created by enclosing comma-separated sequence of elements within curly braces `{}` or by using the `set()` constructor.
```python
fruits = {"apple", "banana", "orange"}
numbers = {1, 2, 3, 4, 5}

# Compound set
mixed_set = {42, "hello", 3.14, True}

# Using set() constructor
s1 = set(["USA", "CHINA", "INDIA"])

# Empty set
empty_set = set()

# Printing a set
print(fruits)       # Output: {'banana', 'apple', 'orange'}
print(numbers)      # Output: {1, 2, 3, 4, 5}
print(mixed_set)    # Output: {True, 42, 3.14, 'hello'}
print(s1)           # Output: {'USA', 'INDIA', 'CHINA'}
print(empty_set)    # Output: set()
```

## Modifying Sets
* Sets are mutable, meaning you can modify their contents after creation.
* You can add elements to a set using the `add()` method and remove elements using the `remove()` or `discard()` methods, also `clear()` to remove all the elements in sets.
```python
my_set = {1, 2, 3}

# add()
my_set.add(4)
print(my_set)        # Output: {1, 2, 3, 4}

# remove()
my_set.remove(2)     # Gives Key error if element does not exist
print(my_set)        # Output: {1, 3, 4}

# discard()
my_set.discard(5)    # No error if element does not exist
print(my_set)        # Output: {1, 3, 4}

# clear()
S11 = {1,2,3}
print('Before Clear:',S11) # Output: Before Clear: {1, 2, 3}
S11.clear()
print('After Clear:',S11)  # Output: After Clear: set()
```

## Set Operations
* Python supports various operations on sets, such as union, intersection, difference, symmetric difference and more.
    * `union()`: Returns a set containing all the distinct elements from both sets.
    * `intersection()`: Returns a set containing the common elements between two sets.
    * `difference()`: Returns a set containing the elements present in the first set but not in the second set.
    * `symmetric_difference()`: Returns a set containing the elements that are in either of the sets, but not in their intersection.
    * `issubset()`: Checks if the input is a SubSet of the give set and returns `TRUE` or `FALSE`.
    * `issuperset()`: Checks if the input is a SuperSet of the give set and returns `TRUE` or `FALSE`.
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
union_set = set1.union(set2)
print(union_set)  
# Output: {1, 2, 3, 4, 5}

# Intersection
intersection_set = set1.intersection(set2)
print(intersection_set)  
# Output: {3}

# Difference
difference_set = set1.difference(set2)
print(difference_set)  
# Output: {1, 2}

# Symmetric Difference
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  
# Output: {1, 2, 4, 5}

# Subset
D1 = {1,2,3,4,5}
S1 = {2,3,4}
print(S1.issubset(D1)) 
# Output: True

# Superset
D1 = {1,2,3,4,5}
S1 = {2,3,4}
print(D1.issuperset(S1)) 
# Output: True
```

## Set Comprehensions
* Similar to list comprehensions, you can use set comprehensions to create sets based on existing sets.
```python
numbers = {1, 2, 3, 4, 5}
squared_numbers = {x ** 2 for x in numbers}  
print(squared_numbers)
# OUTPUT: {1, 4, 9, 16, 25}
```

## Set Membership Testing
* Sets are particularly useful for testing membership efficiently.
```python
my_set = {1, 2, 3}

print(1 in my_set)   
# Output: True

print(4 not in my_set)  
# Output: True
```

## Frozen Sets or Immutable Sets
* Frozen sets are immutable sets. Once a frozen set is created, you cannot modify it.
```python
frozen_set = frozenset([1, 2, 3])
print(frozen_set)  
# Output: frozenset({1, 2, 3})

# Uncomment and run the below code, it will raise an error
# frozen_set.add(4)
```

## Conclusion
* Sets are versatile data structures in Python that allow you to store unique elements and perform various set operations.
* They are useful for tasks involving distinct values, membership testing, and performing set-based calculations.
* Understanding sets can greatly enhance your ability to work with unique collections of data in Python.

##### [Back To Context](../../README.md)