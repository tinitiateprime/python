#
# Modifying Lists in Python
# Author: __author_credits__



my_list = ["apple", "banana", "cherry", "date"]

my_list[1] = "blueberry"
print(my_list)  
# Output: ['apple', 'blueberry', 'cherry', 'date']

my_list.append("elderberry")
print(my_list)  
# Output: ['apple', 'blueberry', 'cherry', 'date', 'elderberry']

my_list.insert(2, "cranberry")
print(my_list)  
# Output: ['apple', 'blueberry', 'cranberry', 'cherry', 'date', 'elderberry']

my_list.remove("cherry")
print(my_list)  
# Output: ['apple', 'blueberry', 'cranberry', 'date', 'elderberry']

del my_list[0] # Removing an element using index
print(my_list)
# Output: ['blueberry', 'cranberry', 'date', 'elderberry']

popped_item = my_list.pop()
print(popped_item)  
# Output: elderberry
print(my_list)      
# Output: ['blueberry', 'cranberry', 'date']

# Modifying elements in a list for a given range
my_list[1:] = ['New1', 'New2']
print('Updated my_list: ' ,my_list)
# Output: Updated my_list:  ['blueberry', 'New1', 'New2']

# Reassigning list to empty list [] will clear the list
my_list = []
print("Cleared list:",my_list)
# Output: Cleared list: []