# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : __class__ Attribute
#  Author       : Team Tinitiate
# ==============================================================================



class Dog:
    def __init__(self, name):
        self.name = name

my_dog = Dog("Buddy")
print(my_dog.__class__)  
# OUTPUT: <class '__main__.Dog'>
