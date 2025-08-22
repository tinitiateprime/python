![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# Python Object-Oriented Programming (OOP)
* Object-Oriented Programming (OOP) in Python is a programming paradigm that allows you to structure your code in a way that models real-world entities as objects.
* OOP revolves around the concept of "objects" which are instances of "classes".
* In Python, everything is an object, and you can create your own objects by defining classes.
* Python, a versatile and powerful programming language, supports OOP principles, making it easy to create modular and reusable code.

## Class
* Python supports, Object Oriented Programming, Its a concept where data and functionality are combined into a unit called as CLASS.
* A `class` is a blueprint for creating objects. It defines the properties (attributes/variables) and behaviors (methods/functions) that all objects of that class will have.
* **Data** could be Class Variables(or CLASS ATTRIBUTES), lists, tuples, dictionaries.
* **Methods or Functions** are operations that perform operations on data values, such as to get squareroot or get square of a given data set.
* For more complex business scenarios, Data could be Credit and salary information and the function could be approve/disapprove loan.
### Attributes
* Attributes are data stored within a class or instance and represent the state or characteristics of the object.
### Methods
* Methods are functions defined within a class. They perform operations on the object's data and can modify the object's state.
```python
# Creating a class Tinitiate
class Tinitiate:
    'This is a brief note about the class, This is the TINITIATE Class'

    # CLASS VARIABLES / ATTRIBUTES
    # A class Variable
    ti_var   = 100
    # A class list
    ti_list  = ["a","b","c"]
    # A class tuple
    ti_tuple = ("x","y","z")
    # A class dictionary
    ti_dictionary = {"1":"A", "2":"b", "3":"c"}

    # CLASS FUNCTION
    def ti_function(self):
        "This is a class function"
        print("This is a message from the TINITIATE Class ti_function")
```

## Object
* An object is an instance of a class. It's a concrete realization of the class blueprint. They have attributes (data) and methods (functions) associated with them. While Class is a Spefcification, Object is the implementation.
* You can create multiple objects of the same class, each with its own set of attributes.
* To use or run a **class** we need to create an **Object**.
* An object is a runtime instance of a class.
* Thus, **Class** is a blueprint for creating objects, **Objects** are instances of a class, and each object can have attributes (characteristics) and methods (functions).
* Objects in Python can represent real-world entities, such as a person, a car, or an abstract concept like a file or a network connection.
```python
# Using the class Tinitiate
# Create an object of the class
tinObject = Tinitiate()
# This will instantiate the Class

# Use the Class variables/lists..
print(tinObject.ti_var)
print(tinObject.ti_list)
print(tinObject.ti_tuple)
print(tinObject.ti_dictionary)

# Call the the class function
tinObject.ti_function() 
# This will print the message from the function

# Create another object of the class
tObject = Tinitiate()

# Call the class function
tObject.ti_function()
# OUTPUT: 100
#         ['a', 'b', 'c']
#         ('x', 'y', 'z')
#         {'1': 'A', '2': 'b', '3': 'c'}
#         This is a message from the TINITIATE Class ti_function
#         This is a message from the TINITIATE Class ti_function
```

## Constructor
* A constructor is a special method used for initializing newly created objects.
* It is denoted by the `__init__()` method within a class definition.
* Constructors are automatically called when a new instance of a class is created.
```python
class Person:
    def __init__(self, name, age):      # Constructor
        self.name = name
        self.age = age
        print("This message is from constructor")

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# Creating an instance of the Person class
king = Person("King", 30)
# Accessing attributes and calling methods
king.introduce()

# Constructor method is called automatically whenever new objects created
jake = Person("Jake", 23)
jackel = Person("Jackel", 25)
# OUTPUT: This message is from constructor
#         Hello, my name is King and I am 30 years old.
#         This message is from constructor
#         This message is from constructor
```
* `self` is a conventional name given to the first parameter of methods in a class.
    * It refers to the instance of the class itself.
    * When you call a method on an object, Python automatically passes the instance as the first argument to the method.
    * By convention, this first parameter is named `self`, though you can technically name it whatever you want (but it's highly recommended to stick with self for clarity and consistency).

## Class Private Variables
* In Python, you can create private variables in a class by prefixing the variable name with two underscores `__`. 
* This practice is known as name mangling, and it makes it harder for external code to access the variable directly.
* However, it's important to note that Python does not provide true "private" variables; instead, it offers a way to make it more challenging for external code to access them.
* Here's an example demonstrating private variables in a class:
```python
class MyClass:
    def __init__(self):
        # Public variable
        self.public_variable = "I'm public!"

        # Private variable (name mangling)
        self.__private_variable = "I'm private!"

    def get_private_variable(self):
        return self.__private_variable

    def set_private_variable(self, new_value):
        self.__private_variable = new_value


# Creating an object of the class
obj = MyClass()

# Accessing public variable
print(obj.public_variable)  
# OUTPUT: I'm public!

# Attempting to access private variable directly (will raise an AttributeError)
# Uncomment the below and try
# print(obj.__private_variable)

# Accessing private variable using methods
print(obj.get_private_variable())  
# OUTPUT: I'm private!

# Modifying private variable using methods
obj.set_private_variable("New private value")
print(obj.get_private_variable())  
# OUTPUT: New private value
```
* In this example, public_variable is a regular public variable.
* **__private** variable is a private variable.
* Attempting to access **__private** variable directly from outside the class will result in an AttributeError.
* Instead, you can use getter and setter methods (**get_private_variable** and **set_private_variable**) to access and modify the private variable, providing a controlled way to interact with it.
* It's important to note that while name mangling adds a level of privacy, it is still possible to access private variables with some effort. The double underscores are mainly a convention, and it's essential to respect encapsulation and use the intended access methods whenever possible.
* **Note:** There are no private functions/methods in Python.

## Encapsulation
* Encapsulation is the concept of bundling data and methods that operate on the data within a single unit, i.e., a class.
* It helps in data hiding and abstraction, preventing direct access to the object's internal state from outside the class.
* In this example, **__radius** is a private attribute, and access to it is controlled through getter and setter methods.
```python
class Circle:
    def __init__(self, radius):
        self.__radius = radius      # Private attribute

    def get_radius(self):
        return self.__radius

    def set_radius(self, new_radius):
        if new_radius > 0:
            self.__radius = new_radius
        else:
            print("Radius must be greater than 0.")

obj1 = Circle(3)
print(obj1.get_radius())
obj1.set_radius(5)
print(obj1.get_radius())
obj1.set_radius(0)
# OUTPUT: 3
#         5
#         Radius must be greater than 0.
```

## Inheritance
* Inheritance is a mechanism that allows a new class (subclass) to inherit properties and methods from an existing class (base class).
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # Abstract method

class Dog(Animal):      # Inherit from class Animal
    def speak(self):
        return "Woof!"

class Cat(Animal):      # Inherit from class Animal
    def speak(self):
        return "Meow!"

object1 = Dog("Husky")
print(object1.speak())

object2 = Cat("Tom")
print(object2.speak())
# OUTPUT: Woof!
#         Meow!
```
* Here, Dog and Cat are subclasses of the Animal class, inheriting the name attribute and the abstract(have nothing in it) speak method.

## Polymorphism
* Polymorphism allows objects of different classes to be treated as objects of a common base class.
* It enables the same method name to be used for different classes, promoting code reusability.
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # Abstract method

class Dog(Animal):          # Inherit from class Animal
    def speak(self):
        return "Woof!"

class Cat(Animal):          # Inherit from class Animal
    def speak(self):
        return "Meow!"

def animal_sound(animal):       # Method 
    return animal.speak()
# The animal_sound function can be used with instances of
# both Dog and Cat, demonstrating polymorphism

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(animal_sound(dog))  
print(animal_sound(cat))  
# OUTPUT: "Woof!"
#         "Meow!"
```
* Here, animal_sound function takes any object with a speak method, demonstrating polymorphism.

# Conclusion
* Python's support for object-oriented programming provides a powerful and flexible way to structure code.
* By using classes, encapsulation, inheritance, and polymorphism, developers can create modular, reusable, and maintainable software.
* Understanding these concepts is essential for building robust and scalable applications in Python.

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
