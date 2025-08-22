# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : __del__ Method
#  Author       : Team Tinitiate
# ==============================================================================



class MyClass:
    def __init__(self, name):
        self.name = name
    
    def call(self):
        print(f"Calling function from {self.name}")

    def __del__(self):
        print(f"{self.name} is being destroyed")

# Creating instances of MyClass
obj1 = MyClass("Object 1")
obj2 = MyClass("Object 2")
obj1.call()
obj2.call()

# Deleting the references to the objects
del obj1
del obj2

# Uncomment the below, try to call the call function again, will give error
# obj1.call()
# obj2.call()
# OUTPUT: Calling function from Object 1
#         Calling function from Object 2
#         Object 1 is being destroyed
#         Object 2 is being destroyed
