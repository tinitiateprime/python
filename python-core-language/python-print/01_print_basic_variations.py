#
# Basic print variations in Python
# Author: __author_credits__



# Simple print statement
print("Welcome to tinitiate.com python turorials")
# OUTPUT: Welcome to tinitiate.com python turorials


# Print statement with append using the `,` , This appends a SPACE
# You can pass multiple objects separated by commas
print("Welcome to tinitiate.com" , 'python turorials "Appended ," ')
# OUTPUT: Welcome to tinitiate.com python turorials "Appended ,"


# Print statement with append using the `+` , This Does Not append SPACE
print('Welcome to tinitiate.com' + 'python turorials "Appended +"')
# OUTPUT: Welcome to tinitiate.compython turorials "Appended +"


# Print statement using custom separator, Using the sep= parameter 
# we can change the separator between multiple arguments
# By default sep parameter comma is SPACE
print("apple", "banana", "orange")
# OUTPUT: apple banana orange
print("apple", "banana", "orange", sep=", ")
# OUTPUT: apple, banana, orange
print("apple", "banana", "orange", sep="- ")
# OUTPUT: apple- banana- orange


# Print a single quote, using esacpe character `\` backslash 
print('Printing a single quote \'')
# OUTPUT: Printing a single quote '
# Same goes with double quote and backslash


# Printing new line character
print("line1" + '\n' + "line2")
# OUTPUT: line1
#         line2  


# Print statement using end parameter, Using end parameter we can specify
# what character(s) should be printed at the end of the print() statement,
# instead of the default newline character.
# Below is Without end parameter
print('First Line')
print('Second Line')
# OUTPUT: First Line
#         Second Line
print('First Line', end="")
print('Second Line')
# OUTPUT: First LineSecond Line
print("tinitiate", end=".")
print("com")
# OUTPUT: tinitiate.com


# Printing a string multiple times using the `*` operator
print ("hello " * 3)
# OUTPUT: hello hello hello 