# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Print `string.format`
#  Author       : Team Tinitiate
# ==============================================================================



# The `{}` brackets and data enclosed within them are called format fields
# The data is replaced with the objects passed in the `str.format()` method
# By default order is left to right as in `{}` `{}` and `str.format(Obj1, Obj2)`
print('Welcome to {} training of {} language'.format('tinitiate.com', 'python'))
# OUTPUT: Welcome to tinitiate.com training of python language



# The order can be substituted by the numbers `{1}` `{2}` for first and second 
# object in `str.format(Obj1, Obj2)`
print('{0} and {1}'.format('tinitiate.com', 'python'))
# OUTPUT:  tinitiate.com and python
print('{1} and {0}'.format('tinitiate.com', 'python'))
# OUTPUT: python and tinitiate.com



# The order of the data can also be in the key-values of the
# `str.format(key1='value1',key2='value2')`
print('{siteName} teaches {LanguageName}.'.format
    (siteName='tinitiate.com', LanguageName='python'))
# OUTPUT: tinitiate.com teaches python.



# Positional and key-value arguments can be arbitrarily combined
print('The site {0} teaches {LanguageName}'.format
    ('tinitiate.com', LanguageName='Python'))
# OUTPUT: The site tinitiate.com teaches Python



# Print statement using `f` string, `f` string is similar to `string.format`
l_site = 'tinitiate.com'
l_language_name = 'Python'
l_str = f"The site {l_site} teaches {l_language_name}"
print(l_str)
# OUTPUT: The site tinitiate.com teaches Python
