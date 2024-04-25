#
# __sizeof__ Method In Python
# Author: __author_credits__



class MyClass:
    def __init__(self, name):
        self.name = name

# Create an instance of MyClass
obj = MyClass("Hello")

# Get the size of the instance
print(obj.__sizeof__())

# Output: 16
# Note: Output will vary based on python version and system architecture