# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Multiple Inheritance With Constructors
#  Author       : Team Tinitiate
# ==============================================================================



# Parent_1 class with constructor
class Parent_1:
    "This is parent-level class"
    
    def __init__(self, parent1Var):
        # Initialize instance variable in the constructor
        self.parent1Var = parent1Var
    
    def Parent1Function(self):
        print("This is a message from the Parent_1.Parent1Function")

# Parent_2 class with constructor
class Parent_2:
    "This is another parent-level class"
    
    def __init__(self, parent2Var):
        # Initialize instance variable in the constructor
        self.parent2Var = parent2Var  
    
    def Parent2Function(self):
        print("This is a message from the Parent_2.Parent2Function")

# Child class with constructor that inherits from Parent_1 and Parent_2
class ChildMI(Parent_1, Parent_2):
    "This is the ChildMI, this inherits Parent_1 and Parent_2"
    
    def __init__(self, parent1Var, parent2Var):
        # Initialize Parent_1 using its constructor
        Parent_1.__init__(self, parent1Var)
        # Initialize Parent_2 using its constructor
        Parent_2.__init__(self, parent2Var)
    
    def ChildMIFunction(self):
        print("This is a message from the ChildMI.ChildMIFunction")

# Create ChildMI Object with required parameters for the constructors
gcObj = ChildMI("Parent1Var Value", "Parent2Var Value")

# Accessing instance variables and methods
print(gcObj.parent1Var)
print(gcObj.parent2Var)
gcObj.Parent1Function()
gcObj.Parent2Function()
gcObj.ChildMIFunction()
# OUTPUT: Parent1Var Value
#         Parent2Var Value
#         This is a message from the Parent_1.Parent1Function
#         This is a message from the Parent_2.Parent2Function
#         This is a message from the ChildMI.ChildMIFunction
