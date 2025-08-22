# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : __str__ Method
#  Author       : Team Tinitiate
# ==============================================================================



class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old."

my_dog = Dog("Buddy", 5)
print(my_dog)  
# OUTPUT: Buddy is 5 years old.
