#
# Miscellaneous Methods in strings in Python
# Author: __author_credits__



# len()
my_string = "Hello, world!"
print(len(my_string))  # Output: 13

# split()
my_string = "Hello, World!"
print(my_string.split(','))        # Output: ['Hello', ' World!']

# splitlines()
testString = """Line 1
Line 2
Line 3
"""
print(testString.splitlines()) # OUTPUT: ['Line 1', 'Line 2', 'Line 3']

# replace()
my_string = "Hello, World!"
print(my_string.replace('Hello', 'Hi'))  # Output: Hi, World!