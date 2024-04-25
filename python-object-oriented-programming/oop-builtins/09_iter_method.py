#
# __iter__ Method In Python
# Author: __author_credits__



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

# Output: JAVA
#         C++
#         SCALA