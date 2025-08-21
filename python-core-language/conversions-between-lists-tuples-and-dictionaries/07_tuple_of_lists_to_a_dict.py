# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Tuple of Lists to a Dictionary
#  Author       : Team Tinitiate
# ==============================================================================



tuple_of_lists = (["a", "b", "c"], [1, 2, 3])
print(tuple_of_lists)
# OUTPUT: (['a', 'b', 'c'], [1, 2, 3])

keys_list, values_list = tuple_of_lists
my_dict = dict(zip(keys_list, values_list))
print(my_dict) 
# OUTPUT: {'a': 1, 'b': 2, 'c': 3}
