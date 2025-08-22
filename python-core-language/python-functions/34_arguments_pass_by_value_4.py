# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Arguments Pass By Value
#  Author       : Team Tinitiate
# ==============================================================================



def modify_string(s):
    s = s.upper()
    print(s)

my_string = "hello"

modify_string(my_string) 
# OUTPUT: HELLO

print(my_string)  
# OUTPUT: hello
