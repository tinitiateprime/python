#
# List Methods in Python
# Author: __author_credits__



my_list = [1, 2, 3, 4]
print("Original List:", my_list)
# Output: Original List: [1, 2, 3, 4]

# len()
print(len(my_list))
# Output: 4
print(len([1, 2, 3]))
# Output: 3

# min()
print(min(my_list))
# Output: 1

# max()
print(max(my_list))
# Output: 4

# sum()
print(sum(my_list))
# Output: 10

# append()
my_list.append(5)
print("After append(5):", my_list)
# Output: After append(5): [1, 2, 3, 4, 5]

# extend()
my_list.extend([6,7,8,9,])
print("After extend([6,7,8,9,]):", my_list)
# Output: After extend([6,7,8,9,]): [1, 2, 3, 4, 5, 6, 7, 8, 9]

# insert()
my_list.insert(3, 10)
print("After insert(3, 10):", my_list)
# Output: After insert(3, 10): [1, 2, 3, 10, 4, 5, 6, 7, 8, 9]

# remove()
my_list.remove(3)
print("After remove(3):", my_list)
# Output: After remove(3): [1, 2, 10, 4, 5, 6, 7, 8, 9]

# pop()
popped_item = my_list.pop() # Removes the first or the last element in the list
print("After pop():", my_list)
# Output: After pop(): [1, 2, 10, 4, 5, 6, 7, 8]
popped_item = my_list.pop(1)
print("Popped Item:", popped_item)
# Output: Popped Item: 2
print("After pop(1):", my_list)
# Output: After pop(1): [1, 10, 4, 5, 6, 7, 8]

# sort()
my_list.sort()
print("After sort():", my_list)
# Output: After sort(): [1, 4, 5, 6, 7, 8, 10]

# reverse()
my_list.reverse()
print("After reverse():", my_list)
# Output: After reverse(): [10, 8, 7, 6, 5, 4, 1]

# index()
index = my_list.index(4)
print("Index of 4:", index)
# Output: Index of 4: 5

# count()
count = my_list.count(3)
print("Count of 3:", count)
# Output: Count of 3: 0

# clear()
my_list.clear()
print("Cleared list: ", my_list)
# Output: Cleared list:  []