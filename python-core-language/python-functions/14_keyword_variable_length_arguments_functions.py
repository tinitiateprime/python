#
# Keyword Variable-Length Arguments Functions in Python
# Author: __author_credits__



def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key + ":", value)

print_info(name="Alice", age=30, city="New York")  
# Keyword variable-length arguments: name="Alice", age=30, city="New York"
# Output: name: Alice
#         age: 30
#         city: New York