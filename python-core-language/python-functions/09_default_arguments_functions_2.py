#
# Default Arguments Functions in Python
# Author: __author_credits__



def power(base, exponent=2):
    result = base ** exponent
    print(f"{base} raised to the power of {exponent} is {result}")

power(3)      # Uses default exponent (2)
power(2, 4)   # Overrides default exponent
# Output: 3 raised to the power of 2 is 9
#         2 raised to the power of 4 is 16