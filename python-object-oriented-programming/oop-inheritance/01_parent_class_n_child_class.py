#
# Inheritance: Parent Class & Child Class In Python
# Author: __author_credits__



# Create a Parent Class, which will be inherited by a Child Class
class ParentClass():
    Parentvar1 = "parentVariable Value"
    def parentFunction(self):
        print("This is a message from ParentClass.parentFunction")

# This is a child class that inherits Parent Class
class ChildClass(ParentClass):
    ChildVar1 = "parentVariable Value"
    def childFunction(self):
        print("This is a message from ChildClass.childFunction")

# Create an object of the Child Class
cObj = ChildClass()

# Calling the child class and parent class methods from the child object
cObj.childFunction()
cObj.parentFunction()

# Output: This is a message from ChildClass.childFunction
#         This is a message from ParentClass.parentFunction