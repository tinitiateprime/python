# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Tuple of Lists to a List of Tuples
#  Author       : Team Tinitiate
# ==============================================================================



tuple_of_lists = ([1, 2, 3], ["a", "b", "c"])
print(tuple_of_lists)
# OUTPUT: ([1, 2, 3], ['a', 'b', 'c'])

list_of_tuples = list(zip(*tuple_of_lists))
print(list_of_tuples)
# OUTPUT: [(1, 'a'), (2, 'b'), (3, 'c')]
