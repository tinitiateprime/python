#
# Inheritance In Python
# Author: __author_credits__



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

# Output: Woof!
#         Meow!