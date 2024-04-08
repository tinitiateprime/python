#
# Functions Pass By Value in Python
# Author: __author_credits__



def modify_tuple(t):
    t = (4, 5, 6)
    print(t)

my_tuple = (1, 2, 3)
modify_tuple(my_tuple)
print(my_tuple)  
# Output: (4, 5, 6)
#         (1, 2, 3)