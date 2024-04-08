#
# Nested if Statements In Python
# Author: __author_credits__



grade = 85

if grade >= 90:
    print("Grade is A")
elif grade >= 80:
    print("Grade is B")
elif grade >= 70:
    print("Grade is C")
else:
    if grade >= 60:
        print("Grade is D")
    else:
        print("Grade is F")
# Output: Grade is B