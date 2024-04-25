#
# __str__ Method In Python
# Author: __author_credits__



class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old."

my_dog = Dog("Buddy", 5)
print(my_dog)  

# Output: Buddy is 5 years old.