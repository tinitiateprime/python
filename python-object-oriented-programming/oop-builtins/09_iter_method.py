# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : __iter__ Method
#  Author       : Team Tinitiate
# ==============================================================================



class IterTest:
    def __init__(self, classList):
        self.classList = classList

    def __iter__(self):
        return (i for i in self.classList)

# Create an object of the Class with a input TUPLE
t_Obj = IterTest(('JAVA','C++', 'SCALA'))

# The result is a loop of elements, now iterate over the result
for data in t_Obj:
    print(data)
# OUTPUT: JAVA
#         C++
#         SCALA
