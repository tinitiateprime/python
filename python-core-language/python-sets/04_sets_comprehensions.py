#
# Set Comprehensions in Python
# Author: __author_credits__



numbers = {1, 2, 3, 4, 5}
squared_numbers = {x ** 2 for x in numbers}  
print(squared_numbers)
# OUTPUT: {1, 4, 9, 16, 25}