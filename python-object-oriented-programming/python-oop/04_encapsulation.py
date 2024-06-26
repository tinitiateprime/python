#
# Encapsulation In Python
# Author: __author_credits__



class Circle:
    def __init__(self, radius):
        self.__radius = radius      # Private attribute

    def get_radius(self):
        return self.__radius

    def set_radius(self, new_radius):
        if new_radius > 0:
            self.__radius = new_radius
        else:
            print("Radius must be greater than 0.")

obj1 = Circle(3)
print(obj1.get_radius())
obj1.set_radius(5)
print(obj1.get_radius())
obj1.set_radius(0)

# Output: 3
#         5
#         Radius must be greater than 0.