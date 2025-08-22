# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Use of Logical Operators In Conditional Statements
#  Author       : Team Tinitiate
# ==============================================================================



# `and` operator
x = 10
y = 20

if x > 0 and y > 0:
    print("Both x and y are positive")
else:
    print("At least one of x and y is not positive")
# OUTPUT: Both x and y are positive



# `or` operator
name = "Alice"

if name == "Alice" or name == "Bob":
    print("Hello, Alice or Bob!")
else:
    print("You are not Alice or Bob.")
# OUTPUT: Hello, Alice or Bob!



# `not` operator
is_sunny = False

if not is_sunny:
    print("It's not sunny today.")
else:
    print("It's sunny today.")
# OUTPUT: It's not sunny today.
