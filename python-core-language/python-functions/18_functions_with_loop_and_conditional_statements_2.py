#
# Functions with loop and conditional statements in Python
# Author: __author_credits__



def print_even_numbers(numbers):
    """
    Print even numbers from the given list.
    """
    for num in numbers:
        if num % 2 == 0:
            print(num, "is even")
        else:
            print(num, "is odd")

# Call the function
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_even_numbers(numbers_list)
# Output: 1 is odd
#         2 is even
#         3 is odd
#         4 is even
#         5 is odd
#         6 is even
#         7 is odd
#         8 is even
#         9 is odd
#         10 is even