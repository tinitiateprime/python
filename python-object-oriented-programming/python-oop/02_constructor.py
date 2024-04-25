#
# Constructor In Python
# Author: __author_credits__



class Person:
    def __init__(self, name, age):      # Constructor
        self.name = name
        self.age = age
        print("This message is from constructor")

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# Creating an instance of the Person class
king = Person("King", 30)
# Accessing attributes and calling methods
king.introduce()

# Constructor method is called automatically whenever new objects created
jake = Person("Jake", 23)
jackel = Person("Jackel", 25)

# Output: This message is from constructor
#         Hello, my name is King and I am 30 years old.
#         This message is from constructor
#         This message is from constructor