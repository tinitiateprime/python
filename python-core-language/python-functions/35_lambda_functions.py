#
# Lambda Functions / Anonymous functions in Python
# Author: __author_credits__



# Add Two Numbers
add = lambda x, y: x + y
print(add(3, 4))  
# Output: 7

# Check if a Number is Even
is_even = lambda x: x % 2 == 0
print(is_even(6))  
# Output: True
print(is_even(7))  
# Output: False

# Square a Number
square = lambda x: x ** 2
print(square(5))  
# Output: 25

# Sorting a List of Tuples by the Second Element
points = [(1, 2), (3, 1), (5, 4), (2, 2)]
sorted_points = sorted(points, key=lambda x: x[1])
print(sorted_points)  
# Output: [(3, 1), (1, 2), (2, 2), (5, 4)]