#
# __base__ and __bases__ Attribute In Python
# Author: __author_credits__



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