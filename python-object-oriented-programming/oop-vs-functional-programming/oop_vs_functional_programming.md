![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# Object Oriented Programming Vs Functional Programming
* To understand the difference between functional programming code and Object Oriented programming code, Lets consider a single problem and write code in both functional and Object Oriented.
* We will demonstrate why Object Oriented Programming is more efficient than Functional Programming for a same problem-solution.

## Create a Functional Programming code
* Lets create a file with functional programming code.
```python
n1 = None
n2 = None
        
def print_func_vars():
    print("Function vars:")
    print("n1=",n1)
    print("n2=",n2)

def add1():
    return n1 + n2

def mul1():
    return n1 * n2
```
* Saving the above code file with name `func_test`.

## Import and Instantiate Functional Code File
* Here we import the Functionl Programming code file `func_test` and create the instances.
* Assigning the values to the instances, and get the function instance size.
```python
import func_test as f1
# Importing func_test as instance f1
import func_test as f2
# Importing func_test as instance f2

# Assigining values to instance f1
f1.n1 = 100
f1.n2 = 200
f1.print_func_vars()
print(f1.add1())
print(f1.mul1())

# Assigining values to instance f2
f2.n1 = 1000
f2.n2 = 2000
f2.print_func_vars()
print(f2.add1())
print(f2.mul1())

# Print the instance size of both instances
print(f1.__sizeof__() + f2.__sizeof__())
# OUTPUT: Function vars:
#         n1= 100
#         n2= 200
#         300
#         20000
#         Function vars:
#         n1= 1000
#         n2= 2000
#         3000
#         2000000
#         112
```

## Create an Object Oriented Programming code
* Here we create a Class (Object Oriented Programming code) with the same functionality of the functional programming code.
```python
class OOP:
    # Class Variables
    n1 = None
    n2 = None
            
    # Class Methods(Functions)
    def print_class_vars(self):
        print("Class OOPs vars:")
        print("n1=",self.n1)
        print("n2=",self.n2)

    def add1(self):
        return self.n1 + self.n2

    def mul1(self):
        return self.n1 * self.n2
```
* Saving the above code file with name `oop_test`.

## Import and Instantiate OOP Code File
* Here we import the Object Oriented Programming code file `class_test` and create the objects.
* Assigning the values to the instances, and get the class instance size.
```python
from oop_test import OOP as t1

# Create Obj1 of class OOP
Obj1 = t1()
Obj1.n1 = 100
Obj1.n2 = 200
Obj1.print_class_vars()
print(Obj1.add1())
print(Obj1.mul1())

# Create Obj2 of class OOP
Obj2 = t1()
Obj2.n1 = 1000
Obj2.n2 = 2000
Obj2.print_class_vars()
print(Obj2.add1())
print(Obj2.mul1())

# Print the object Size of both the objects
print(Obj1.__sizeof__() + Obj2.__sizeof__())
# OUTPUT: Class OOPs vars:
#         n1= 100
#         n2= 200
#         300
#         20000
#         Class OOPs vars:
#         n1= 1000
#         n2= 2000
#         3000
#         2000000
#         32
```

## Functional Code vs. Object-Oriented Code
* Python supports both functional programming and object-oriented programming paradigms, offering developers the flexibility to choose the approach that best fits their needs.
* Each paradigm has its own set of pros and cons, and the choice between functional and object-oriented code often depends on the specific requirements of the project and the developer's preferences. 

### Functional Programming
**Pros:**
  * **Simplicity and Readability:** Functional code tends to be concise and expressive, making it easier to read and understand. Emphasis on pure functions, which have no side effects, leads to code that is easier to reason about.
  * **Immutability:** Immutable data structures prevent unexpected changes to data, promoting safer and more predictable code. Avoiding mutable state simplifies debugging and makes the code more thread-safe.
  * **Parallelism and Concurrency:** Pure functions are inherently thread-safe, facilitating parallelism and concurrency. Functions that don't rely on shared state can be easily parallelized.
  * **Easy Testing:** Pure functions make unit testing straightforward since they have no dependencies on external state.

**Cons:**
  * **Learning Curve:** Functional programming concepts, such as higher-order functions and immutability, may have a steeper learning curve for developers accustomed to imperative programming.
  * **Performance Overhead:** Immutable data structures and functional constructs might introduce a performance overhead compared to their mutable counterparts.
  * **Limited Tooling for Certain Domains:** In some domains, such as GUI programming, functional programming might not have as mature tooling or standard practices.

### Object-Oriented Programming (OOP)
**Pros:**
  * **Modularity and Reusability:** OOP encourages the creation of modular and reusable code through encapsulation, inheritance, and polymorphism. Classes provide a natural way to structure and organize code.
  * **Abstraction:** Abstraction allows developers to focus on high-level functionality without worrying about implementation details. Well-designed class hierarchies provide a clear structure for the application.
  * **Readability and Maintainability:** OOP code can be more readable and maintainable, especially for large and complex systems. Encapsulation hides internal details, reducing complexity.
  * **Widely Used in Industry:** Many large-scale software projects and frameworks are built using OOP principles, making it a valuable skill for developers entering the industry.

**Cons:**
  * **Boilerplate Code:** OOP code can sometimes involve more boilerplate code, leading to verbosity. Inheritance hierarchies can become overly complex and introduce maintenance challenges.
  * **Mutable State:** Encapsulation doesn't guarantee immutability, and mutable state can lead to unexpected side effects. Managing state can be challenging, especially in concurrent environments.
  * **Performance Concerns:** Some OOP constructs might introduce performance overhead, and optimizing OOP code can be more complex.

## Conclusion
* The choice between functional and object-oriented programming in Python depends on the specific requirements of the project, the preferences of the development team, and the nature of the problem domain.
* In many cases, a hybrid approach that combines elements of both paradigms can provide a balanced solution, leveraging the strengths of each to create robust and maintainable code.
* Developers should carefully consider the trade-offs and choose the paradigm that aligns best with the goals of their project.

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
