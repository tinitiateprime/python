#
# Searching Methods in strings in Python
# Author: __author_credits__



# index()
sentence = "This is a sample sentence."
index1 = sentence.index("is")
print(index1)  # Output: 2

# Specifying start and end index
index2 = sentence.index("is", 3, 10)
print(index2)  # Output: 5

# Specifying only start
index3 = sentence.index("s", 4)
print(index3)  # Output: 6

# Searching string that doesn't exist, Uncomment the following to view error
# index4 = sentence.index("Python")
# print(index4)  # Output: ValueError


# rindex()
sentence = "This is a sample sentence."
index1 = sentence.rindex("is")
print(index1)  # Output: 5

# Specifying start and end index
index2 = sentence.rindex("s", 2, 23)
print(index2)  # Output: 17

# Specifying only start
index3 = sentence.rindex("is", 1)
print(index3)  # Output: 5

# Searching string that doesn't exist, Uncomment the following to view error
# index4 = sentence.rindex("z")
# print(index4)  # Output: ValueError


# find()
sentence = "This is a sample sentence."
index1 = sentence.find("sample")
print(index1)  # Output: 10

# Substring not found
index2 = sentence.find("example")
print(index2)  # Output: -1


# rfind()
sentence = "This is a sample sentence."
index1 = sentence.rfind("is", 1, 5)
print(index1)  # Output: 2

# Substring not found
index2 = sentence.rfind("example")
print(index2)  # Output: -1