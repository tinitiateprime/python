#
# __init__ Method In Python
# Author: __author_credits__



class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Dog name is {}, age = {}".format(name, age))

# Creating an instance of Dog
my_dog = Dog("Buddy", 5)
# Constructor is automatically called implicitly when an object is created

# Output: Dog name is Buddy, age = 5