# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Multiple Inheritance
#  Author       : Team Tinitiate
# ==============================================================================



# Creating parent classes
class Parent_1():
    "This is another parent-level class"

    def Parent1Function(self):
        print("This is a message from the Parent_1.Parent1Function")

class Parent_2():
    "This is another parent-level class"

    def Parent2Function(self):
        print("This is a message from the Parent_2.Parent2Function")

# Child Class that inherits from two parents
class Child(Parent_1, Parent_2):
    "This is the ChildMI, this inherits Parent_1 and Parent_2"

    def ChildMIFunction(self):
        print("This is a message from the ChildMI.ChildMIFunction")

# Create a Child Object
gcObj = Child()

# Calling methods from different parent classes from child class object
gcObj.Parent1Function()
gcObj.Parent2Function()
# OUTPUT: This is a message from the Parent_1.Parent1Function
#         This is a message from the Parent_2.Parent2Function
