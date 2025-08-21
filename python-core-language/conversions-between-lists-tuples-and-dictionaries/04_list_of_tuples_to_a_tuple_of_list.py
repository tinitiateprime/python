# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : List of Tuples to a Tuple of Lists
#  Author       : Team Tinitiate
# ==============================================================================



tuple_list = [(1, "a"), (2, "b"), (3, "c")]
int_list, char_list = zip(*tuple_list)
# '*' symbol zips all
print(tuple_list)
# OUTPUT: [(1, 'a'), (2, 'b'), (3, 'c')]

tuple_of_lists = (list(int_list), list(char_list))
print(tuple_of_lists) 
# OUTPUT: ([1, 2, 3], ['a', 'b', 'c'])
