# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Importing and Instantiating OOP Code File
#  Author       : Team Tinitiate
# ==============================================================================



from oop_test import OOP as t1

# Create Obj1 of class OOP
Obj1 = t1()
Obj1.n1 = 100
Obj1.n2 = 200
Obj1.print_class_vars()
print(Obj1.add1())
print(Obj1.mul1())

# Create Obj2 of class OOP
Obj2 = t1()
Obj2.n1 = 1000
Obj2.n2 = 2000
Obj2.print_class_vars()
print(Obj2.add1())
print(Obj2.mul1())

# Print the object Size of both the objects
print(Obj1.__sizeof__() + Obj2.__sizeof__())
# OUTPUT: Class OOPs vars:
#         n1= 100
#         n2= 200
#         300
#         20000
#         Class OOPs vars:
#         n1= 1000
#         n2= 2000
#         3000
#         2000000
#         32
