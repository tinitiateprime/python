#
# Variable-Length Arguments Functions in Python
# Author: __author_credits__



def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_numbers(1, 2, 3)) 
# Variable-length arguments: 1, 2, 3 are captured as a tuple (1, 2, 3)
# Output: 6