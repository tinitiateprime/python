# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : __sizeof__ Method
#  Author       : Team Tinitiate
# ==============================================================================



class MyClass:
    def __init__(self, name):
        self.name = name

# Create an instance of MyClass
obj = MyClass("Hello")

# Get the size of the instance
print(obj.__sizeof__())
# OUTPUT: 16
# Note: Output will vary based on python version and system architecture
