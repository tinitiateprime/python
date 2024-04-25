#
# __repr__ Method In Python
# Author: __author_credits__



class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Dog('{self.name}', {self.age})"

my_dog = Dog("Buddy", 5)
print(repr(my_dog))  

# Output: Dog('Buddy', 5)