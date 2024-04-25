#
# __len__ Method In Python
# Author: __author_credits__



class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

my_list = MyList([1, 2, 3, 4, 5])
print(len(my_list))

# Output: 5