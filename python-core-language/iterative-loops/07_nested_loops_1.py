#
# Nested Loops in Python
# Author: __author_credits__



adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for ad in adj:
    for fruit in fruits:
        print(ad, fruit)
# Output: red apple
#         red banana
#         red cherry
#         big apple
#         big banana
#         big cherry
#         tasty apple
#         tasty banana
#         tasty cherry