# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Stripping Methods
#  Author       : Team Tinitiate
# ==============================================================================



# strip()
# Removes the whitespaces starting and ending of the string
print ('   This is a test  '.strip())
# OUTPUT: This is a test

# Removes the occurrence of 't'
print ('This is a test'.strip('t'))
# OUTPUT: This is a tes

# Removes the occurrence of 'T'
print ('This is a test'.strip('T'))
# OUTPUT: his is a test

# Removes the occurrence of 'is'
print ('sssThis is a testsss'.strip('s'))
# OUTPUT: This is a test



# lstrip()
text = "    Hello, world!    "
# Remove leading whitespace
stripped_text = text.lstrip()
print(stripped_text)  # Output: "Hello, world!    "

# Remove leading specified characters
text = ">>>Hello, world!"
stripped_text = text.lstrip(">")
print(stripped_text)  # Output: "Hello, world!"

print ('This is a test'.lstrip('This'))
# OUTPUT: is a test  



# rstrip()
text = "    Hello, world!    "
# Remove trailing whitespace
stripped_text = text.rstrip()
print(stripped_text)  # Output: "    Hello, world!"

# Remove trailing specified characters
text = "Hello, world!..."
stripped_text = text.rstrip(".")
print(stripped_text)  # Output: "Hello, world!"

print ('This is a test'.rstrip(' test'))
# OUTPUT: This is a
