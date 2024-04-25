#
# __doc__ Attribute In Python
# Author: __author_credits__



class Dog:
    """This class represents a dog."""
    def __init__(self, name):
        self.name = name

print(Dog.__doc__)  

# Output: This class represents a dog.