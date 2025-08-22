# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Single Inheritance With Constructors
#  Author       : Team Tinitiate
# ==============================================================================



# Create a Parent Class, which will be inherited by a Child Class
class ParentClass:
    ParentVar1 = "parentVariable Value"
    
    def __init__(self, parentVar2):     # Parent Constructor
        # Initialize instance variable in the constructor
        self.parentVar2 = parentVar2
    
    def parentFunction(self):
        print("This is a message from ParentClass.parentFunction")

# This is a child class that inherits Parent Class
class ChildClass(ParentClass):          # Child Constructor
    ChildVar1 = "childVariable Value"
    
    def __init__(self, parentVar2, childVar2):
        # Call the constructor of the ParentClass using super()
        super().__init__(parentVar2)
        # Initialize instance variable specific to child class constructor
        self.childVar2 = childVar2
    
    def childFunction(self):
        print("This is a message from ChildClass.childFunction")

# Create an object of the ChildClass with parameters for the constructors
cObj = ChildClass("ParentVar2 Value", "ChildVar2 Value")

# Accessing instance variables and methods
print(cObj.parentVar2) 
print(cObj.childVar2)  
cObj.childFunction()   
cObj.parentFunction()  
# OUTPUT: ParentVar2 Value
#         ChildVar2 Value
#         This is a message from ChildClass.childFunction
#         This is a message from ParentClass.parentFunction
