#
# Converting a Tuple of Lists to a Dictionary in Python
# Author: __author_credits__



tuple_of_lists = (["a", "b", "c"], [1, 2, 3])
print(tuple_of_lists)
# Output: (['a', 'b', 'c'], [1, 2, 3])

keys_list, values_list = tuple_of_lists
my_dict = dict(zip(keys_list, values_list))
print(my_dict) 
# Output: {'a': 1, 'b': 2, 'c': 3}