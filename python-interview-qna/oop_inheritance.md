![Python Tinitiate Image](../python_tinitiate.png)

# Python Interview QnA
&copy; TINITIATE.COM

##### [Back To Contents](./README.md)

# OOP Inheritance

## Q1. What is inheritance in Python OOP?
**Answer:**  
Inheritance allows a class (child) to acquire properties and methods from another class (parent).

## Q2. How do you define inheritance in Python?
**Answer:**  
```python
class Parent: pass
class Child(Parent): pass
```

## Q3. What is single inheritance?
**Answer:**  
A child class inherits from one parent class.

## Q4. What is multiple inheritance?
**Answer:**  
A child class inherits from more than one parent class.  
```python
class A: pass
class B: pass
class C(A,B): pass
```

## Q5. What is multilevel inheritance?
**Answer:**  
Inheritance across multiple levels.  
```python
class A: pass
class B(A): pass
class C(B): pass
```

## Q6. What is hierarchical inheritance?
**Answer:**  
Multiple child classes inherit from the same parent.

## Q7. What is hybrid inheritance?
**Answer:**  
Combination of different inheritance types.

## Q8. How does Python handle multiple inheritance conflicts?
**Answer:**  
Using **Method Resolution Order (MRO)** with C3 linearization.

## Q9. How do you check MRO of a class?
**Answer:**  
Use `.mro()` or `__mro__`.  
```python
print(C.mro())
```

## Q10. What is method overriding?
**Answer:**  
When a child class defines a method with the same name as the parent, overriding its behavior.

## Q11. How do you call parent methods from child?
**Answer:**  
Use `super()`.  
```python
class Parent:
    def greet(self): print("Hi from Parent")
class Child(Parent):
    def greet(self):
        super().greet()
        print("Hi from Child")
```

## Q12. What happens if a child does not override a parent method?
**Answer:**  
The parent’s method is inherited and used as-is.

## Q13. Can constructors be inherited?
**Answer:**  
Yes, unless overridden in the child class.

## Q14. How do you call a specific parent method in multiple inheritance?
**Answer:**  
Explicitly use parent class name.  
```python
A.method(self)
```

## Q15. What is the `super()` function used for in inheritance?
**Answer:**  
To call parent class methods without explicitly naming the parent, supporting cooperative multiple inheritance.

## Q16. Can Python support private inheritance like C++?
**Answer:**  
No. Python only supports public inheritance, but encapsulation can be simulated using private variables.

## Q17. What is diamond problem in inheritance?
**Answer:**  
Occurs when a class inherits from multiple classes that share a common ancestor. Python resolves it using MRO.

## Q18. What are abstract base classes (ABCs)?
**Answer:**  
Classes from `abc` module that define methods to be implemented by child classes.

## Q19. What are advantages of inheritance?
**Answer:**  
- Code reuse  
- Hierarchical classification  
- Extensibility

## Q20. What are disadvantages of inheritance?
**Answer:**  
- Increases coupling between classes  
- Can make debugging complex  
- Misuse leads to fragile code

##### [Back To Contents](./README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
