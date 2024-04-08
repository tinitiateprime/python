#
# Converting a Tuple of Lists to a List of Tuples in Python
# Author: __author_credits__



tuple_of_lists = ([1, 2, 3], ["a", "b", "c"])
print(tuple_of_lists)
# Output: ([1, 2, 3], ['a', 'b', 'c'])

list_of_tuples = list(zip(*tuple_of_lists))
print(list_of_tuples)
# Output: [(1, 'a'), (2, 'b'), (3, 'c')]