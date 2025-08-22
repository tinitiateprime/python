# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Inheritance
#  Author       : Team Tinitiate
# ==============================================================================



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
