![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# Python Lists
* In Python, a list is a versatile data structure used to store ordered collection of items. Each item in a list is called an element, and these elements can be of different data types, including numbers, strings, or even other lists.
* Lists are mutable, meaning their elements can be changed after the list is created.

## Creating Lists
* Lists can be created by enclosing elements within square brackets `[]`, separated by commas.
```python
MyNumbersList = [1, 100, 9, 99]

MyStringList  = ["A", 'b', 'Hello', "This"]

fruits = ["apple", "banana", "orange"]

# Nested list: Lists can contain other lists as elements
nested_list = [[1, 2], [3, 4], [5, 6]]

# A Compound elements based list
# Compound = elements with various data types
CompoundList = [1, "two", 3.0, True]

# Printing a List
print(MyNumbersList) # Output: [1, 100, 9, 99]
print(MyStringList)  # Output: ["A", 'b', 'Hello', "This"]
print(fruits)        # Output: ['apple', 'banana', 'orange']
print(nested_list)   # Output: [[1, 2], [3, 4], [5, 6]]
print (CompoundList) # Output: [1, 'two', 3.0, True]
```

## Accessing Elements in Lists
* Elements in a list are indexed, thus each element has a 
position associated with it, the position is called as **Index**, starting from 0 for the first element.
* You can access individual elements using their index.
```python
MyNumbersList = [1, 100, 9, 99]
#                0  1    2  3
print(MyNumbersList[3]) # Output: 99

my_list = ["apple", "banana", "cherry", "date"]

print(my_list[0])   # Output: apple
print(my_list[1])   # Output: banana
# (negative indexing, indexes from last)
print(my_list[-1])  # Output: date 

MyStringList  = ["A", 'b', 'Hello', "This"]
print(MyStringList[0]) # Output: A

fruits = ["apple", "banana", "orange"]
print(fruits[1]) # Output: banana

CompoundList = [1, "two", 3.0, True]
print(CompoundList[-2]) # Output: 3.0 
print(CompoundList[3]) # Output: True
```

## Accessing Nested List Elements
* A nested list is a list that contains other lists as elements.
* You can access elements in a nested list using nested indexing.
* The outer list is indexed first, then the inner list is indexed.
```python
nested_list = [[1, 2], [3, 4], [5, 6]]
#                0        1      2
#              00  01   10 11   20 21 
# First list in nested_list
print(nested_list[0])       # Output: [1, 2]
# First list elements in nested_list
print(nested_list[0][0])    # Output: 1
print(nested_list[0][1])    # Output: 2

# Second list in nested_list
print(nested_list[1])       # Output: [3, 4]
# First list elements in nested_list
print(nested_list[1][0])    # Output: 3
print(nested_list[1][1])    # Output: 4

# Third list in nested_list
print(nested_list[2])       # Output: [5, 6]
# First list elements in nested_list
print(nested_list[2][0])    # Output: 5
print(nested_list[2][1])    # Output: 6
```

## List Slicing
* Similar to strings, you can extract a sublist(portion of list) from a list using slicing.
```python
my_list = ["apple", "banana", "cherry", "date"]

# Sublist from index 1 upto 3 (not including 3)
print(my_list[1:3])   # Output: ['banana', 'cherry']

# Sublist from starting index upto 2 (not including 2)
print(my_list[:2])    # Output: ['apple', 'banana']

# Sublist from index 2 to ending index (including ending index)
print(my_list[2:])    # Output: ['cherry', 'date']
```

## List Operations
* Python supports various operations on lists, such as concatenation, repetition, and membership tests.
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
print(list1 + list2)   # Output: [1, 2, 3, 4, 5, 6]

# Repetition
print(list1 * 3)       # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Membership test
print(2 in list1)      # Output: True

# Comparision
print(list1 == list2)  # Output: False
```

## List Methods
* Python provides many built-in methods to manipulate and work with lists.
    * `len()`: Returns length of the list
    * `min()`: Returns minimum value in the list
    * `max()`: Returns maximum value in the list
    * `sum()`: Returns the sum of all the values in the list
    * `append()`: Adds a single element to the end of the list
    * `extend()`: Adds multiple Elements
    * `insert()`: Inserts a single element at a specified position in the list
    * `remove()`: Removes the first occurrence of a specified value from the list
    * `pop()`: Removes and returns the element at the specified index
    * `sort()`: Sorts the elements of the list in ascending order
    * `reverse()`: Reverses the order of the elements in the list
    * `index()`: Returns the index of the first occurrence of a specified value in the list
    * `count()`: Returns the number of occurrences of a specified value in the list
    * `clear()`: This removes all the elements of the list
```python
my_list = [1, 2, 3, 4]
print("Original List:", my_list)
# Output: Original List: [1, 2, 3, 4]



# len()
print(len(my_list))
# Output: 4
print(len([1, 2, 3]))
# Output: 3



# min()
print(min(my_list))
# Output: 1



# max()
print(max(my_list))
# Output: 4



# sum()
print(sum(my_list))
# Output: 10



# append()
my_list.append(5)
print("After append(5):", my_list)
# Output: After append(5): [1, 2, 3, 4, 5]



# extend()
my_list.extend([6,7,8,9,])
print("After extend([6,7,8,9,]):", my_list)
# Output: After extend([6,7,8,9,]): [1, 2, 3, 4, 5, 6, 7, 8, 9]

# insert()
my_list.insert(3, 10)
print("After insert(3, 10):", my_list)
# Output: After insert(3, 10): [1, 2, 3, 10, 4, 5, 6, 7, 8, 9]



# remove()
my_list.remove(3)
print("After remove(3):", my_list)
# Output: After remove(3): [1, 2, 10, 4, 5, 6, 7, 8, 9]



# pop()
popped_item = my_list.pop() # Removes the first or the last element in the list
print("After pop():", my_list)
# Output: After pop(): [1, 2, 10, 4, 5, 6, 7, 8]
popped_item = my_list.pop(1)
print("Popped Item:", popped_item)
# Output: Popped Item: 2
print("After pop(1):", my_list)
# Output: After pop(1): [1, 10, 4, 5, 6, 7, 8]



# sort()
my_list.sort()
print("After sort():", my_list)
# Output: After sort(): [1, 4, 5, 6, 7, 8, 10]



# reverse()
my_list.reverse()
print("After reverse():", my_list)
# Output: After reverse(): [10, 8, 7, 6, 5, 4, 1]



# index()
index = my_list.index(4)
print("Index of 4:", index)
# Output: Index of 4: 5



# count()
count = my_list.count(3)
print("Count of 3:", count)
# Output: Count of 3: 0



# clear()
my_list.clear()
print("Cleared list: ", my_list)
# Output: Cleared list:  []
```

## Modifying Lists
* Lists are mutable, meaning you can modify their elements after creation.
* You can assign new values to specific elements using indexing.
```python
my_list = ["apple", "banana", "cherry", "date"]



my_list[1] = "blueberry"
print(my_list)  
# Output: ['apple', 'blueberry', 'cherry', 'date']



my_list.append("elderberry")
print(my_list)  
# Output: ['apple', 'blueberry', 'cherry', 'date', 'elderberry']



my_list.insert(2, "cranberry")
print(my_list)  
# Output: ['apple', 'blueberry', 'cranberry', 'cherry', 'date', 'elderberry']



my_list.remove("cherry")
print(my_list)  
# Output: ['apple', 'blueberry', 'cranberry', 'date', 'elderberry']



del my_list[0] # Removing an element using index
print(my_list)
# Output: ['blueberry', 'cranberry', 'date', 'elderberry']



popped_item = my_list.pop()
print(popped_item)  
# Output: elderberry
print(my_list)      
# Output: ['blueberry', 'cranberry', 'date']



# Modifying elements in a list for a given range
my_list[1:] = ['New1', 'New2']
print('Updated my_list: ' ,my_list)
# Output: Updated my_list:  ['blueberry', 'New1', 'New2']



# Reassigning list to empty list [] will clear the list
my_list = []
print("Cleared list:",my_list)
# Output: Cleared list: []
```

## List Comprehensions
* List comprehensions provide a concise way to create lists based on existing lists.
```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)
# OUTPUT: [1, 4, 9, 16, 25]
```

## Conclusion
* Lists are fundamental data structures in Python that allow you to store, access, and manipulate collections of items.
* Their versatility and rich set of methods make them essential for various programming tasks, from data storage to transformation and analysis.

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
