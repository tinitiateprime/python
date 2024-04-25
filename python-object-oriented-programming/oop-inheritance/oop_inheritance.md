![Python Tinitiate Image](../../python_tinitiate.png)
# Python Tutorial
&copy; TINITIATE.COM
##### [Back To Context](../../README.md)

# Object-Oriented Programming (OOP) - Inheritance
* Inheritance, is the process of accessing members and functions of a class from another class.
* Here the **Class** whose members and functions need to be accessed is called the **Parent Class** and the **Class** that accessing is called the **Child Class**.
* **Parent Class** is also known as **Base Class** or **Superclass** or **Ancestor Class**.
* **Child Class** is also known as **Derived Class** or **Subclass** or **Descendant Class**.
* To Inherit parent class members and functions, pass the parent class name as a parameter to the child class.
* Now a child class object can access the parent class members and functions.
```python
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
```

## Multiple Inheritance
* Inheritance can be implemented as Multiple Inheritance i.e, multiple parent classes and one child class.
```python
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

# Output: This is a message from the Parent_1.Parent1Function
#         This is a message from the Parent_2.Parent2Function
```

## Multi-Level Inheritance
* Inheritance can also be implemented as Multi-level Inheritance i.e, Child Class Inherits from a Parent Class, and the Parent Class inherits from a Grand parent Class.
```python
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
```

## Inheritance Overriding
* Overriding is all about NAMES of Functions and Variables.
* Overriding is the process of using the same NAME for Functions and variables, In the child class, which inherits same named Functions and variables from a parent class.
* Here the Child Functions and variables, with same names takes precedence over the Inherited Parent Class Functions and Variables.
```python
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
```

## Inheritance Super Function
* Super is useful for accessing inherited methods from parent class that have been overridden in the child class.
* Here we use the `super` keyword, Pass the Child Class Name and call the parent class's function.
```python
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
```

## Inheritance With Constructors
* Single inheritance with constructors:
```python
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

# Output: ParentVar2 Value
#         ChildVar2 Value
#         This is a message from ChildClass.childFunction
#         This is a message from ParentClass.parentFunction
```

* Multiple inheritance with constructors:
```python
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

# Output: Parent1Var Value
#         Parent2Var Value
#         This is a message from the Parent_1.Parent1Function
#         This is a message from the Parent_2.Parent2Function
#         This is a message from the ChildMI.ChildMIFunction
```

* Multi-level inheritance with constructors:
```python
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
```

##### [Back To Context](../../README.md)