#
# Functions Pass By Value in Python
# Author: __author_credits__



def modify_string(s):
    s = s.upper()
    print(s)

my_string = "hello"

modify_string(my_string) 
# Output: HELLO

print(my_string)  
# Output: hello