# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : __repr__ Method
#  Author       : Team Tinitiate
# ==============================================================================



class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Dog('{self.name}', {self.age})"

my_dog = Dog("Buddy", 5)
print(repr(my_dog))  
# OUTPUT: Dog('Buddy', 5)
