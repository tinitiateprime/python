# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Functions with a LIST input parameter
#  Author       : Team Tinitiate
# ==============================================================================



def extract_list_into_strings_and_numbers(in_list):
    """This is a function separates list into a stringlist and numberlist"""
    
    # Store Numbers from "in_list" parameter in number_list
    number_list = []
    
    # Store Strings from "in_list" parameter in string_list
    string_list = []

    # Loop through the input parameter list
    for c in in_list:
        if c.isdigit():
            number_list.append(c)
        else:
            string_list.append(c)

    # Print Number List
    print(number_list)

    # Print String List
    print(string_list)

# Calling the function 
print(extract_list_into_strings_and_numbers(['1','A', '2', '3','B', 'c']))
# OUTPUT:
#        ['1', '2', '3']
#        ['A', 'B', 'c']
#        None
# In Python, when a function doesn’t have a return statement, 
# it implicitly returns `None`
