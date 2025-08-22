# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Default Arguments in Functions
#  Author       : Team Tinitiate
# ==============================================================================



def greet(name, greeting="Hello"):
    print(greeting, name)

greet("Charlie")  # Default argument: "Hello" is assigned to greeting
# OUTPUT: Hello Charlie
