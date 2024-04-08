#
# Nested Loops in Python
# Author: __author_credits__



# Nested Loops, loop inside loop using range() function
for outer_loop in range(5):
    for inner_loop in range(5):
        print('outer_loop-inner_loop', outer_loop, '-', inner_loop) 
        # Prints all the elements in new line
# Output: outer_loop-inner_loop 0 - 0
#         outer_loop-inner_loop 0 - 1
#         outer_loop-inner_loop 0 - 2
#         outer_loop-inner_loop 0 - 3
#         outer_loop-inner_loop 0 - 4
#         outer_loop-inner_loop 1 - 0
#         outer_loop-inner_loop 1 - 1
#         outer_loop-inner_loop 1 - 2
#         outer_loop-inner_loop 1 - 3
#         outer_loop-inner_loop 1 - 4
#         outer_loop-inner_loop 2 - 0
#         outer_loop-inner_loop 2 - 1
#         outer_loop-inner_loop 2 - 2
#         outer_loop-inner_loop 2 - 3
#         outer_loop-inner_loop 2 - 4
#         outer_loop-inner_loop 3 - 0
#         outer_loop-inner_loop 3 - 1
#         outer_loop-inner_loop 3 - 2
#         outer_loop-inner_loop 3 - 3
#         outer_loop-inner_loop 3 - 4
#         outer_loop-inner_loop 4 - 0
#         outer_loop-inner_loop 4 - 1
#         outer_loop-inner_loop 4 - 2
#         outer_loop-inner_loop 4 - 3
#         outer_loop-inner_loop 4 - 4