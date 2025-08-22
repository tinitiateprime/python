# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : __dict__ Attribute
#  Author       : Team Tinitiate
# ==============================================================================



class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_dog = Dog("Buddy", 5)
print(my_dog.__dict__)
# OUTPUT: {'name': 'Buddy', 'age': 5}
