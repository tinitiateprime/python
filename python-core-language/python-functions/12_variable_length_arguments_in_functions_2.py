# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Variable-Length Arguments in Functions
#  Author       : Team Tinitiate
# ==============================================================================



def show_items(*items):
    print("Items:")
    for item in items:
        print(item)

print(show_items("apple", "banana", "cherry"))
# OUTPUT: Items:
#         apple
#         banana
#         cherry
#         None
