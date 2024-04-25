#
# Multi-Level Inheritance In Python
# Author: __author_credits__



# Create a grand parent class
class GrandParent():
    "This is the GrandParent class"
    def GrandParentFunction(self):
        print("This is a message from the GrandParent.GrandParentFunction")

# This parent class inherits the GrandParent class
class Parent(GrandParent):
    "This is the Parent class"
    def ParentFunction(self):
        print("This is a message from the Parent.ParentFunction")

# Class that inherits Parent class
class Child(Parent):
    "This is the ChildMI, this inherits Parent_1 and Parent_2"
    def ChildFunction(self):
        print("This is a message from the Child.ChildFunction")

# Create a Child Object
gcObj = Child()

# Calling methods from multi-level classes from child class
gcObj.GrandParentFunction()
gcObj.ParentFunction()
gcObj.ChildFunction()

# Output: This is a message from the GrandParent.GrandParentFunction
#         This is a message from the Parent.ParentFunction
#         This is a message from the Child.ChildFunction