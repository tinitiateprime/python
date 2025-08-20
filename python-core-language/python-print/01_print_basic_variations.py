# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Print basic variations
#  Author       : Team Tinitiate
# ==============================================================================



# Simple print statement
print("Welcome to tinitiate.com python tutorials")
# OUTPUT: Welcome to tinitiate.com python tutorials



# Print statement with append using the `,` , This appends a SPACE
# You can pass multiple objects separated by commas
print("Welcome to tinitiate.com" , 'python tutorials "Appended ," ')
# OUTPUT: Welcome to tinitiate.com python tutorials "Appended ,"



# Print statement with append using the `+` , This Does Not append SPACE
print('Welcome to tinitiate.com' + 'python tutorials "Appended +"')
# OUTPUT: Welcome to tinitiate.compython tutorials "Appended +"



# Print statement using custom separator, Using the `sep=` parameter 
# we can change the separator between multiple arguments
# By default sep parameter comma is SPACE
print("apple", "banana", "orange")
# OUTPUT: apple banana orange

print("apple", "banana", "orange", sep=", ")
# OUTPUT: apple, banana, orange

print("apple", "banana", "orange", sep="- ")
# OUTPUT: apple- banana- orange



# Print a single quote, using escape character `\` backslash 
print('Printing a single quote \'')
# OUTPUT: Printing a single quote '

# Same goes with double quote and backslash
print("Printing a double quote \"")
# OUTPUT: Printing a double quote "



# Printing new line character `\n`
print("line1" + '\n' + "line2")
# OUTPUT: line1
#         line2  



# Print statement using end parameter, Using end parameter we can specify
# what character(s) should be printed at the end of the `print()` statement,
# instead of the default newline character
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
