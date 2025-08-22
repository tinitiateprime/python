# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Lambda Functions/Anonymous functions
#  Author       : Team Tinitiate
# ==============================================================================



# Add Two Numbers
add = lambda x, y: x + y
print(add(3, 4))  
# OUTPUT: 7



# Check if a Number is Even
is_even = lambda x: x % 2 == 0
print(is_even(6))  
# OUTPUT: True
print(is_even(7))  
# OUTPUT: False



# Square a Number
square = lambda x: x ** 2
print(square(5))  
# OUTPUT: 25



# Sorting a List of Tuples by the Second Element
points = [(1, 2), (3, 1), (5, 4), (2, 2)]
sorted_points = sorted(points, key=lambda x: x[1])
print(sorted_points)  
# OUTPUT: [(3, 1), (1, 2), (2, 2), (5, 4)]
