#
# Dictionary Comprehensions in Python
# Author: __author_credits__



numbers = {1, 2, 3, 4, 5}
numbers_dict = {x: x ** 2 for x in numbers}  
print(numbers_dict)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}