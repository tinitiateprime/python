#
# Class Private Variables In Python
# Author: __author_credits__



class MyClass:
    def __init__(self):
        # Public variable
        self.public_variable = "I'm public!"

        # Private variable (name mangling)
        self.__private_variable = "I'm private!"

    def get_private_variable(self):
        return self.__private_variable

    def set_private_variable(self, new_value):
        self.__private_variable = new_value


# Creating an object of the class
obj = MyClass()

# Accessing public variable
print(obj.public_variable)  # Output: I'm public!

# Attempting to access private variable directly (will raise an AttributeError)
# Uncomment the below and try
# print(obj.__private_variable)

# Accessing private variable using methods
print(obj.get_private_variable())  # Output: I'm private!

# Modifying private variable using methods
obj.set_private_variable("New private value")
print(obj.get_private_variable())  # Output: New private value