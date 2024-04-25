#
# __dict__ Attribute In Python
# Author: __author_credits__



class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_dog = Dog("Buddy", 5)
print(my_dog.__dict__)

# Output: {'name': 'Buddy', 'age': 5}