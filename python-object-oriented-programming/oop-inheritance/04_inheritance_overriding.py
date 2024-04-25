#
# Inheritance Overriding In Python
# Author: __author_credits__



# Create a Parent Class
class xParent():  
    "This is a Parent Class"
    var1 = "Parent-Test"
    def func1(self):
        print("This is parent class")

# Creat Child class that inherits the xParent
# and overrides the function and variable with names same
# as the ones from the parent class
class xChild(xParent):
    "This is the Child class"
    var1 = "Child-Test"
    def func1(self):
        print("This is child class")

# Create a parent class object
objA = xParent()
objA.func1()    

# Create a child class object
objA = xChild()
objA.func1()    

# Output: This is parent class
#         This is child class