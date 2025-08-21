# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : String Formatting
#  Author       : Team Tinitiate
# ==============================================================================



name = "Alice"
age = 30
# Using f-strings(formatted string literals)
print(f"My name is {name} and I am {age} years old.")  
# Output: My name is Alice and I am 30 years old.

# Using the .format()
print("My name is {} and I am {} years old.".format(name, age))  
# Output: My name is Alice and I am 30 years old.

# Using the %
print("My name is %s and I am %d years old." % (name, age))  
# Output: My name is Alice and I am 30 years old.
