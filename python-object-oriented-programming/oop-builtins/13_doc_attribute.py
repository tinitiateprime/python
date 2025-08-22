# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : __doc__ Attribute
#  Author       : Team Tinitiate
# ==============================================================================



class Dog:
    """This class represents a dog."""
    def __init__(self, name):
        self.name = name

print(Dog.__doc__)  
# OUTPUT: This class represents a dog.
