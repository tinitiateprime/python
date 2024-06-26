#
# String Indexing/Accessing Characters in Strings in Python
# Author: __author_credits__



var_test_string = "Python is cool"

# Index starts from 0, 
# This prints the first character of the string 
print('First character of variable var_test_string: ', var_test_string[0])

# Index of the last character is -1
print('Last character of variable var_test_string: ',var_test_string[-1])

# Print forth character from the end
print('Fourth character from the end of variable var_test_string: '
       ,var_test_string[-4])

# OUT oF range indexes
# When specifing indexes that don't exist is a string, it fails
var_my_string  = "four"
# print(var_my_string[5]) # this will raise an error