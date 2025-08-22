![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# Iterative Loops
* Iterative loops in Python allow you to execute a block of code repeatedly until a certain condition is met or until all elements in an iterable have been processed. 
* They enable you to automate repetitive tasks, iterate through data structures, and perform actions based on specific conditions.
* Python provides several types of iterative loops, including `for` loops, `while` loops, and nested loops.

## `for` Loop
* The `for` loop in Python is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each item in the sequence.
```python
# Simple `for` Loop
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
# OUTPUT: apple
#         banana
#         cherry



# LOOP Over the number of characters in a sting
for character in 'MyString':
    print(character) 
    # Prints all the characters in new line
# OUTPUT: M
#         y
#         S
#         t
#         r
#         i
#         n
#         g



# LOOP over elements in a LIST
myList = [1, 2, 3, 4, 5]
for element in myList:
    print(element)  
    # Prints all the elements in new line
# OUTPUT: 1
#         2
#         3
#         4
#         5

# Loop through a subset of list of elements
print("Sublist :")
for element in myList[2:4]:
    print(element)  
    # Prints all the elements in new line
# OUTPUT: Sublist :
#         3
#         4
```

## `while` Loop
* The `while` loop in Python is used to execute a block of code repeatedly as long as a specified condition is true.
* Be cautious when using `while` loops to avoid infinite loops—loops that never terminate if the condition is never met.
```python
# Example 1:
i = 0
while i < 5:
    print(i)
    i += 1
# OUTPUT: 0
#         1
#         2
#         3
#         4



# Example 2:
curr_value = 0   
while (curr_value <= 5):
    print('Curr_value: ', curr_value)
    curr_value += 1
# OUTPUT: Curr_value:  0
#         Curr_value:  1
#         Curr_value:  2
#         Curr_value:  3
#         Curr_value:  4
#         Curr_value:  5



# INFINITE LOOP issue
# Great care should be taken when writing loops as it could 
# iterate perpetually or run in an infinite loop
# while some situations require to run forever like services
# CODE
#  while(1==1):
#      print("in infinite loop")
# To stop, Close the application if nothing responds
```

## Nested Loops
* You can nest one loop inside another loop to create nested loops, allowing you to perform more complex iterations.
```python
# Example 1:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for ad in adj:
    for fruit in fruits:
        print(ad, fruit)
# OUTPUT: red apple
#         red banana
#         red cherry
#         big apple
#         big banana
#         big cherry
#         tasty apple
#         tasty banana
#         tasty cherry



# Example 2:
# Nested Loops, loop inside loop using range() function
for outer_loop in range(5):
    for inner_loop in range(5):
        print('outer_loop-inner_loop', outer_loop, '-', inner_loop) 
        # Prints all the elements in new line
# OUTPUT: outer_loop-inner_loop 0 - 0
#         outer_loop-inner_loop 0 - 1
#         outer_loop-inner_loop 0 - 2
#         outer_loop-inner_loop 0 - 3
#         outer_loop-inner_loop 0 - 4
#         outer_loop-inner_loop 1 - 0
#         outer_loop-inner_loop 1 - 1
#         outer_loop-inner_loop 1 - 2
#         outer_loop-inner_loop 1 - 3
#         outer_loop-inner_loop 1 - 4
#         outer_loop-inner_loop 2 - 0
#         outer_loop-inner_loop 2 - 1
#         outer_loop-inner_loop 2 - 2
#         outer_loop-inner_loop 2 - 3
#         outer_loop-inner_loop 2 - 4
#         outer_loop-inner_loop 3 - 0
#         outer_loop-inner_loop 3 - 1
#         outer_loop-inner_loop 3 - 2
#         outer_loop-inner_loop 3 - 3
#         outer_loop-inner_loop 3 - 4
#         outer_loop-inner_loop 4 - 0
#         outer_loop-inner_loop 4 - 1
#         outer_loop-inner_loop 4 - 2
#         outer_loop-inner_loop 4 - 3
#         outer_loop-inner_loop 4 - 4
```

## Looping Through Range
* Python's `range()` function generates a sequence of numbers that can be used for looping a specific number of times.
```python
# Example 1:
for i in range(5):
    print(i)    # Index starts from ZERO!
# OUTPUT: 0
#         1
#         2
#         3
#         4



# Example 2:
# LOOP 5 times with printing index
for c in range(5):
    print('Loop Count: ',c)
# OUTPUT: Loop Count:  0
#         Loop Count:  1
#         Loop Count:  2
#         Loop Count:  3
#         Loop Count:  4
```

## Loop Control Statements
* Python provides loop control statements such as `break`, `continue`, and `pass` to control the flow of loops.
    * `break`: The break statement terminates the loop prematurely when a certain condition is met.
    * `continue`: The continue statement skips the current iteration and moves to the next iteration of the loop.
    * `pass`: The pass statement does nothing and is used as a placeholder when a statement is syntactically required but no action is needed.
```python
# break
# for loop
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)
# OUTPUT: apple

# while loop
cur_value = 0                  
while (cur_value < 5):
    cur_value += 1 
    if cur_value==3:
        break
    print('Cur_value: ', cur_value)
# OUTPUT: Cur_value:  1
#         Cur_value:  2



# continue
# Example 1:
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)
# OUTPUT: apple
#         cherry

# Example 2:
for c in range(3):
    print('Run:', c,'step1')
    if c==1:
        continue 
    print('Run:', c,'step2')
    print('Run:', c,'step3')
# OUTPUT: Run: 0 step1
#         Run: 0 step2
#         Run: 0 step3
#         Run: 1 step1      # step2 and step3 are skipped for run 1
#         Run: 2 step1
#         Run: 2 step2
#         Run: 2 step3



# pass
# Example 1:
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == "banana":
        pass
    else:
        print(fruit)
# OUTPUT: apple
#         cherry

# Example 2:
for c in range(3):
    if c==1:
        print('Do a very important step')
    elif c==2:
        pass
    else:
        print('normal processing')
# OUTPUT: normal processing
#         Do a very important step
```

## Looping Through Dictionary
* You can loop through the keys, values, or key-value pairs of a dictionary using the `keys()`, `values()`, and `items()` methods, respectively.
```python
my_dict = {"name": "John", "age": 30, "gender": "Male"}

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)
```

## Looping Through Index
* To iterate through both the elements and their indices in a sequence, you can use the `enumerate()` function.
```python
fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
# OUTPUT: Index 0: apple
#         Index 1: banana
#         Index 2: orange
```

## Use Cases of Iterative Loops
* **Iterating over Data Structures:** Iterative loops are commonly used to iterate over elements of lists, tuples, sets, dictionaries, strings, etc.
* **Repeating Actions:** Iterative loops are used to execute a block of code repeatedly, such as reading lines from a file, processing data in batches, or performing simulations.
* **Nested Iterations:** Nested loops are useful for iterating through multiple dimensions of data, such as rows and columns of a matrix, nested lists, or hierarchical data structures.

## Conclusion
* Iterative loops are essential programming constructs in Python, allowing you to iterate over data structures, repeat actions, and control the flow of execution based on certain conditions.
* They provide a powerful mechanism for handling repetitive tasks and processing large amounts of data efficiently.

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
