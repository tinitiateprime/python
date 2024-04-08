#
# Converting a List of Tuples to a Tuple of Lists in Python
# Author: __author_credits__



tuple_list = [(1, "a"), (2, "b"), (3, "c")]
int_list, char_list = zip(*tuple_list)
# '*' symbol zips all
print(tuple_list)
# Output: [(1, 'a'), (2, 'b'), (3, 'c')]

tuple_of_lists = (list(int_list), list(char_list))
print(tuple_of_lists) 
# Output: ([1, 2, 3], ['a', 'b', 'c'])