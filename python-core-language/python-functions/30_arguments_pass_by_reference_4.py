# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Arguments Pass By Reference
#  Author       : Team Tinitiate
# ==============================================================================



def add_key_value(my_dict):
    my_dict["c"] = 30
    print(my_dict)

data = {"a": 10, "b": 20}

add_key_value(data) 
# OUTPUT: {'a': 10, 'b': 20, 'c': 30}

print(data)  
# OUTPUT: {'a': 10, 'b': 20, 'c': 30}
