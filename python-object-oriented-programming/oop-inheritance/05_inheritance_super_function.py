#
# Inheritance Super Function In Python
# Author: __author_credits__



# Parent Class
class Parent1():
    "A parent class to demonstrate the SUPER"
    
    # Parent1 Class Variable
    X = 100
    
    # Parent1 Consructor
    def __init__(self):
        print("This is a message from ",Parent1.__name__)
    
    # Parent1 Method
    def func1(self):
        print("This is a message from Parent1.func1")

# Child Class
class Child1(Parent1):
    "A child class to demonstrate the SUPER"
    
    # Child1 Class Variable
    X = 999
    
    # Child1 Consructor
    def __init__(self):
    
        # Call the parent Class's Constructor using the super()
        super().__init__()
        
        # Refer the variable X from Parent1 Class using super()
        print(super().X)

        # Refer the variable X from Child1 Class using 'self' keyword
        print(self.X)
    
    def func1(self):
        print("This is a message from Child1.func1")
        
    # This is a func2, calling the Parent1 classes method.
    def func2(self):
        super().func1()

# Create an object
supObject = Child1()

# Calling the methods
supObject.func1()
supObject.func2()

# Output: This is a message from  Parent1
#         100
#         999
#         This is a message from Child1.func1
#         This is a message from Parent1.func1