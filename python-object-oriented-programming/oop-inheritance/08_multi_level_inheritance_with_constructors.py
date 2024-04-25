#
# Multi-level Inheritance With Constructors In Python
# Author: __author_credits__



# SuperParent class with constructor
class SuperParent:
    "This is super parent-level class"
    
    def __init__(self, superparentVar):
        # Initialize instance variable in the constructor
        self.superparentVar = superparentVar
    
    def SuperParentFunction(self):
        print("This is a message from the SuperParent.SuperParentFunction")

# Parent class with constructor
class Parent(SuperParent):
    "This is parent-level class"
    
    def __init__(self, parentVar):
        # Initialize instance variable in the constructor
        self.parentVar = parentVar
    
    def ParentFunction(self):
        print("This is a message from the Parent.ParentFunction")

# Child class that inherits from Parent which is derived from SuperParent
class ChildMI(Parent):
    "This is the ChildMI, this inherits SuperParent and Parent"
    
    def __init__(self, superparentVar, parentVar):
        # Initialize SuperParent using its constructor
        SuperParent.__init__(self, superparentVar)
        # Initialize Parent using its constructor
        Parent.__init__(self, parentVar)
    
    def ChildMIFunction(self):
        print("This is a message from the ChildMI.ChildMIFunction")

# Create ChildMI Object with required parameters for the constructors
gcObj = ChildMI("SuperParentVar Value", "ParentVar Value")

# Accessing instance variables and methods
print(gcObj.superparentVar)
print(gcObj.parentVar)
gcObj.SuperParentFunction()
gcObj.ParentFunction()
gcObj.ChildMIFunction()

# Output: SuperParentVar Value
#         ParentVar Value
#         This is a message from the SuperParent.SuperParentFunction
#         This is a message from the Parent.ParentFunction
#         This is a message from the ChildMI.ChildMIFunction