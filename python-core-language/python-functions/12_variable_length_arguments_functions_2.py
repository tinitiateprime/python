#
# Variable-Length Arguments Functions in Python
# Author: __author_credits__



def show_items(*items):
    print("Items:")
    for item in items:
        print(item)

print(show_items("apple", "banana", "cherry"))
# Output: Items:
#         apple
#         banana
#         cherry
#         None