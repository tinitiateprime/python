![Python Tinitiate Image](../python_tinitiate.png)

# Python Interview QnA
&copy; TINITIATE.COM

##### [Back To Contents](./README.md)

# Python OOP

## Q1. What is Object-Oriented Programming (OOP)?
**Answer:**  
OOP is a programming paradigm that organizes code into objects (instances of classes) combining data and behavior.

## Q2. What is a class in Python?
**Answer:**  
A class is a blueprint for creating objects. It defines attributes (variables) and methods (functions).  
```python
class Person:
    def __init__(self,name): self.name=name
```

## Q3. What is an object in Python?
**Answer:**  
An object is an instance of a class with its own data.  
```python
p = Person("Alice")
```

## Q4. What is the purpose of the `__init__` method?
**Answer:**  
It is a constructor called when an object is created to initialize attributes.

## Q5. What is `self` in class methods?
**Answer:**  
`self` refers to the instance of the class and is used to access instance variables and methods.

## Q6. What are instance variables?
**Answer:**  
Variables tied to a specific object, defined using `self`.  
```python
class Car:
    def __init__(self,brand): self.brand=brand
```

## Q7. What are class variables?
**Answer:**  
Shared variables defined inside the class but outside methods.  
```python
class Car:
    wheels = 4
```

## Q8. What is encapsulation?
**Answer:**  
Bundling data and methods inside classes, restricting direct access to some components.

## Q9. How do you make private variables in Python?
**Answer:**  
Prefix with double underscore (`__var`).  
```python
class Demo:
    def __init__(self): self.__hidden=10
```

## Q10. What is inheritance in Python?
**Answer:**  
A mechanism where a class can derive properties and methods from another class.  
```python
class Animal: pass
class Dog(Animal): pass
```

## Q11. What is polymorphism in Python?
**Answer:**  
The ability of objects of different classes to respond to the same method call differently.  
```python
class Cat: 
    def sound(self): return "Meow"
class Dog: 
    def sound(self): return "Bark"
for a in [Cat(),Dog()]:
    print(a.sound())
```

## Q12. What is method overriding?
**Answer:**  
Redefining a parent class method in a child class.

## Q13. What is multiple inheritance?
**Answer:**  
A class inheriting from multiple base classes.  
```python
class A: pass
class B: pass
class C(A,B): pass
```

## Q14. What is the `super()` function?
**Answer:**  
It calls parent class methods, often used in constructors.  
```python
class Parent: 
    def __init__(self): print("Parent")
class Child(Parent):
    def __init__(self): super().__init__()
```

## Q15. What is method overloading in Python?
**Answer:**  
Python doesn’t support traditional overloading; default arguments or `*args` are used instead.

## Q16. What is method resolution order (MRO)?
**Answer:**  
The order in which Python looks for methods/attributes when multiple inheritance is used (`.mro()`).

## Q17. What are abstract classes?
**Answer:**  
Classes that cannot be instantiated directly, defined using `abc` module with `@abstractmethod`.

## Q18. What is the difference between class method, instance method, and static method?
**Answer:**  
- Instance → takes `self` (operates on object).  
- Class → takes `cls` (operates on class).  
- Static → no `self` or `cls`.  
```python
class Demo:
    @classmethod
    def c(cls): pass
    @staticmethod
    def s(): pass
```

## Q19. What is duck typing in Python OOP?
**Answer:**  
An object's suitability is determined by presence of methods/attributes, not its type.

## Q20. What are pros of OOP in Python?
**Answer:**  
- Code reusability  
- Modularity  
- Encapsulation  
- Easier maintenance

##### [Back To Contents](./README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
