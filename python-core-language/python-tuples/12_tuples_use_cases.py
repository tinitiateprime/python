#
# Use Cases of Tuples in Python
# Author: __author_credits__



# Returning multiple values from a function
def get_coordinates():
    return 10, 20       # Tuples

x, y = get_coordinates()
print(x, y)                 
# Output: 10 20

# Storing related data
person = ("John", 30, "Male")
print(person)              
# Output: ('John', 30, 'Male')

# Immutable keys in dictionaries
coordinates = {(1, 2): "point"}
print(coordinates[1, 2])    
# Output: point