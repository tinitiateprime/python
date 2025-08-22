# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Importing and Instantiating Functional Code File
#  Author       : Team Tinitiate
# ==============================================================================



import func_test as f1
# Importing func_test as instance f1
import func_test as f2
# Importing func_test as instance f2

# Assigining values to instance f1
f1.n1 = 100
f1.n2 = 200
f1.print_func_vars()
print(f1.add1())
print(f1.mul1())

# Assigining values to instance f2
f2.n1 = 1000
f2.n2 = 2000
f2.print_func_vars()
print(f2.add1())
print(f2.mul1())

# Print the instance size of both instances
print(f1.__sizeof__() + f2.__sizeof__())
# OUTPUT: Function vars:
#         n1= 100
#         n2= 200
#         300
#         20000
#         Function vars:
#         n1= 1000
#         n2= 2000
#         3000
#         2000000
#         112
