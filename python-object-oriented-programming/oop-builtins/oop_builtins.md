![Python Tinitiate Image](../../python_tinitiate.png)
# Python Tutorial
&copy; TINITIATE.COM
##### [Back To Contents](../../README.md)

# Object-Oriented Programming (OOP) - BuiltIns
* There are several built-in funtions or attributes (often called "dunder" methods or attributes) that facilitate the OOP process.
* These built-in functions or attributes start and end with double underscores, like `__init__`, `__str__`,` __repr__`, and more.

## `__init__` Method
* This is a constructor of the class. The `__init__` method is used for initializing an object's attributes. It is automatically called implicitly when an object is created.
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Dog name is {}, age = {}".format(name, age))

# Creating an instance of Dog
my_dog = Dog("Buddy", 5)
# Constructor is automatically called implicitly when an object is created

# Output: Dog name is Buddy, age = 5
```

## `__del__` Method
* This is a destructor of the class. The `__del__` method is used to define the deletion behavior of objects.
* It is called when an object is about to be destroyed, typically when it goes out of scope or when its reference count drops to zero.
```python
class MyClass:
    def __init__(self, name):
        self.name = name
    
    def call(self):
        print(f"Calling function from {self.name}")

    def __del__(self):
        print(f"{self.name} is being destroyed")

# Creating instances of MyClass
obj1 = MyClass("Object 1")
obj2 = MyClass("Object 2")
obj1.call()
obj2.call()

# Deleting the references to the objects
del obj1
del obj2

# Uncomment the below, try to call the call function again, will give error
# obj1.call()
# obj2.call()

# Output: Calling function from Object 1
#         Calling function from Object 2
#         Object 1 is being destroyed
#         Object 2 is being destroyed
```

## `__str__` Method
* The `__str__` method returns a string representation of the object.
* It's used for the "informal" or readable string representation.
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old."

my_dog = Dog("Buddy", 5)
print(my_dog)  

# Output: Buddy is 5 years old.
```

## `__repr__` Method
* The `__repr__` method returns an "official" string representation of the object.
* It's typically used for debugging and logging.
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Dog('{self.name}', {self.age})"

my_dog = Dog("Buddy", 5)
print(repr(my_dog))  

# Output: Dog('Buddy', 5)
```

## `__sizeof__` Method
* The `__sizeof__` method is used to return the size of an object in bytes.
* It can be called on any object to get an estimate of the memory it occupies.
* **Note**: Output will vary based on Python version and system architecture.
```python
class MyClass:
    def __init__(self, name):
        self.name = name

# Create an instance of MyClass
obj = MyClass("Hello")

# Get the size of the instance
print(obj.__sizeof__())

# Output: 16
# Note: Output will vary based on python version and system architecture
```

## `__len__` Method
* This method returns the length of the object.
* It is typically implemented for container objects like lists, tuples, dictionaries, etc.
```python
class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

my_list = MyList([1, 2, 3, 4, 5])
print(len(my_list))

# Output: 5
```

## `__add__` Method
* This method defines the behavior of the `+` operator when applied to objects of a class.
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3.x, p3.y)

# Output: 4 6
```

## `__getitem__` and `__setitem__` Methods
* These methods allow objects to behave like sequences or mappings, enabling indexing and slicing operations.
```python
class MyList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

my_list = MyList([1, 2, 3, 4, 5])
print(my_list[2])    # Output: 3
my_list[2] = 10
print(my_list[2])    # Output: 10
```

## `__iter__` Method
* This method is a special method used to define an iterator for an object.
* This returns a "loop of data".
```python
class IterTest:
    def __init__(self, classList):
        self.classList = classList

    def __iter__(self):
        return (i for i in self.classList)

# Create an object of the Class with a input TUPLE
t_Obj = IterTest(('JAVA','C++', 'SCALA'))

# The result is a loop of elements, now iterate over the result
for data in t_Obj:
    print(data)

# Output: JAVA
#         C++
#         SCALA
```

## `__class__` Attribute
* The `__class__` attribute references the object to which class it belongs.
```python
class Dog:
    def __init__(self, name):
        self.name = name

my_dog = Dog("Buddy")
print(my_dog.__class__)  # Output: <class '__main__.Dog'>
```

## `__base__` and `__bases__` Attribute
* The `__base__` and `__bases__` attributes are related to inheritance and provide information about the inheritance hierarchy of a class.
* The `__base__` attribute is a reference to the immediate parent class of a class. It allows you to access the direct superclass of a class.
* The `__bases__` attribute is a tuple containing references to all the direct parent classes of a class. It provides information about all the base classes from which the class directly inherits.
```python
class Animal:
    pass

class Bark:
    pass

class Cat(Animal):          # Single Inheritance
    pass

class Dog(Animal, Bark):    # Multiple Inheritance
    pass

class Bulldog(Dog):         # Multi-level Inheritance
    pass


print(Cat.__base__)
print(Cat.__bases__)
print(Dog.__base__)
print(Dog.__bases__)
print(Bulldog.__base__)
print(Bulldog.__bases__)


# Output: <class '__main__.Animal'>
#         (<class '__main__.Animal'>,)
#         <class '__main__.Animal'>
#         (<class '__main__.Animal'>, <class '__main__.Bark'>)
#         <class '__main__.Dog'>
#         (<class '__main__.Dog'>,)
```

## `__dict__` Attribute
* The `__dict__` attribute is a dictionary containing an object's attributes.
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_dog = Dog("Buddy", 5)
print(my_dog.__dict__)

# Output: {'name': 'Buddy', 'age': 5}
```

## `__doc__` Attribute
* The `__doc__` attribute retrieves the documentation string of a class or a function.
```python
class Dog:
    """This class represents a dog."""
    def __init__(self, name):
        self.name = name

print(Dog.__doc__)  # Output: This class represents a dog.
```

##### [Back To Contents](../../README.md)