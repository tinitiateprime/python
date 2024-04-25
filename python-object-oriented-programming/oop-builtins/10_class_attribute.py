#
# __class__ Attribute In Python
# Author: __author_credits__



class Dog:
    def __init__(self, name):
        self.name = name

my_dog = Dog("Buddy")
print(my_dog.__class__)  

# Output: <class '__main__.Dog'>