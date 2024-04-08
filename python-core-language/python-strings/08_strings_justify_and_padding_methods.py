#
# Justify And Padding Methods in strings in Python
# Author: __author_credits__



# ljust(lenght, char)
print ('test'.ljust(10,'+'))
# OUTPUT: test++++++

text = "Hello"
l_padded_text = text.ljust(10, '*')
print(l_padded_text)  # Output: Hello*****
print(l_padded_text.ljust(15,' '))


# center(length, char)
print ('test'.center(10,'+'))
# OUTPUT: +++test+++

text = "Hello"
centered_text = text.center(11, '*')
print(centered_text)  # Output: ***Hello***
print(centered_text.center(15,' '))


# rjust(length, char)
print ('test'.rjust(10,'+'))
# OUTPUT: ++++++test

text = "Hello"
r_padded_text = text.rjust(10, '*')
print(r_padded_text)  # Output: "*****Hello"
print(r_padded_text.rjust(15,' '))