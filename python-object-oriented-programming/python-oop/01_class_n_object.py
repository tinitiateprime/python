# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Class and Object
#  Author       : Team Tinitiate
# ==============================================================================



# Creating a class Tinitiate
class Tinitiate:
    'This is a brief note about the class, This is the TINITIATE Class'

    # CLASS VARIABLES / ATTRIBUTES
    # A class Variable
    ti_var   = 100
    # A class list
    ti_list  = ["a","b","c"]
    # A class tuple
    ti_tuple = ("x","y","z")
    # A class dictionary
    ti_dictionary = {"1":"A", "2":"b", "3":"c"}

    # CLASS FUNCTION
    def ti_function(self):
        "This is a class function"
        print("This is a message from the TINITIATE Class ti_function")


# Using the class Tinitiate
# Create an object of the class
tinObject = Tinitiate()
# This will instantiate the Class

# Use the class attributes
print(tinObject.ti_var)
print(tinObject.ti_list)
print(tinObject.ti_tuple)
print(tinObject.ti_dictionary)

# Call the the class function
tinObject.ti_function() 
# This will print the message from the function

# Create another object of the class
tObject = Tinitiate()

# Call the class function
tObject.ti_function()
# OUTPUT: 100
#         ['a', 'b', 'c']
#         ('x', 'y', 'z')
#         {'1': 'A', '2': 'b', '3': 'c'}
#         This is a message from the TINITIATE Class ti_function
#         This is a message from the TINITIATE Class ti_function
