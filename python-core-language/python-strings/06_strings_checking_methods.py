#
# Checking Methods in strings in Python
# Author: __author_credits__



# Checking if the string is UpperCase
print ('PYTHON'.isupper())   # Prints true
v = 'PYTHON'
print (v.isupper())   # Prints true

# Checking if the string is lowerCase
print ('PYTHON'.islower())   # Prints false

# Checking if the string has only alphabets
print ('PYTHON01'.isdigit()) # Prints false

# Checking if the string has only numerics
print ('1000'.isnumeric()) # Prints true

# Checking if the string has only alphabets and numerics
print ('PYTHON01'.isalnum()) # Prints true

# Checking if the string has whitespace (space/tab) only
print ('  '.isspace()) # Prints true

# Checking startswith
text = "Hello, world!"
result = text.startswith("Hello")
print(result)  # Output: True

text = "Hello, world!"
result = text.startswith("world", 7)
print(result)  # Output: True

# Checking endswith
text = "Hello, world!"
result = text.endswith("world!")
print(result)  # Output: True

text = "Hello, world!"
result = text.endswith("lo,", 0, 6)
print(result)  # Output: True