#
# Functions Pass By Reference in Python
# Author: __author_credits__



def modify_list(lst):
    lst.append(4)  # Modifying the list inside the function

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  
# Output: [1, 2, 3, 4]