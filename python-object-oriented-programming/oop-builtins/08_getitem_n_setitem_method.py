#
# __getitem__ and __setitem__ Methods In Python
# Author: __author_credits__



class MyList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

my_list = MyList([1, 2, 3, 4, 5])
print(my_list[2])           # Output: 3
my_list[2] = 10
print(my_list[2])           # Output: 10