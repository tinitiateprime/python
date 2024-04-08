#
# Variable-Length Arguments Functions in Python
# Author: __author_credits__



def one_fixed_and_arbitrary_length_argument(arg1, *arbitrary_arguments_tuple):
    "This is a demonstration of the one fixed and arbitrary arguments"
    print('Value of the first argument: ',arg1)
    v=0
    for c1 in arbitrary_arguments_tuple:
        v+=1
        print('Arbitrary Argument number: ',v,' value: ',c1)

# calling the function 
# in this case ONE fixed and FOUR variable length
print(one_fixed_and_arbitrary_length_argument(1, 2, 3, 5, 6))

# in this case ONE fixed and FOUR variable length
print(one_fixed_and_arbitrary_length_argument
(1, 'a1', 'a2', 'a3', 'a4', 'a5', 'a6'))

# Output: Value of the first argument:  1
#         Arbitrary Argument number:  1  value:  2
#         Arbitrary Argument number:  2  value:  3
#         Arbitrary Argument number:  3  value:  5
#         Arbitrary Argument number:  4  value:  6
#         None
#         Value of the first argument:  1
#         Arbitrary Argument number:  1  value:  a1
#         Arbitrary Argument number:  2  value:  a2
#         Arbitrary Argument number:  3  value:  a3
#         Arbitrary Argument number:  4  value:  a4
#         Arbitrary Argument number:  5  value:  a5
#         Arbitrary Argument number:  6  value:  a6
#         None