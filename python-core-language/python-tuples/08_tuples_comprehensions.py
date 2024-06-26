#
# Tuple Comprehensions in Python
# Author: __author_credits__



number_tuple = (0, 1, 2, 3, 4)
print(number_tuple)
# Output: (0, 1, 2, 3, 4)

my_tuple = tuple(x ** 2 for x in number_tuple)
print(my_tuple)  
# Output: (0, 1, 4, 9, 16)