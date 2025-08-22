# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : __init__ Method
#  Author       : Team Tinitiate
# ==============================================================================



class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Dog name is {}, age = {}".format(name, age))

# Creating an instance of Dog
my_dog = Dog("Buddy", 5)
# Constructor is automatically called implicitly when an object is created
# OUTPUT: Dog name is Buddy, age = 5
