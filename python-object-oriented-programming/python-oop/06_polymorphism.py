#
# Polymorphism In Python
# Author: __author_credits__



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

# Output: "Woof!"
#         "Meow!"