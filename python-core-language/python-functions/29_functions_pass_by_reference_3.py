#
# Functions Pass By Reference in Python
# Author: __author_credits__



def modify_list(my_list):
    my_list.append(4)
    my_list[0] = 100
    print(my_list) 

numbers = [1, 2, 3]

modify_list(numbers) 
# Output: [100, 2, 3, 4]

print(numbers)  
# Output: [100, 2, 3, 4]