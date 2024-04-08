#
# Functions Pass By Value in Python
# Author: __author_credits__



def modify_number(num):
    num = num + 1  # Modifying the number inside the function
    print(num)

my_num = 5

modify_number(my_num) 
# Output: 6

print(my_num)  
# Output: 5