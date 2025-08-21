# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Modifying Sets
#  Author       : Team Tinitiate
# ==============================================================================



my_set = {1, 2, 3}

# add()
my_set.add(4)
print(my_set)        # Output: {1, 2, 3, 4}

# remove()
my_set.remove(2)     # Gives Key error if element does not exist
print(my_set)        # Output: {1, 3, 4}

# discard()
my_set.discard(5)    # No error if element does not exist
print(my_set)        # Output: {1, 3, 4}

# clear()
S11 = {1,2,3}
print('Before Clear:',S11) # Output: Before Clear: {1, 2, 3}
S11.clear()
print('After Clear:',S11)  # Output: After Clear: set()
