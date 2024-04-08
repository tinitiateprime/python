#
# Loop Control Statements in Python
# Author: __author_credits__



# continue
for c in range(3):
    print('Run:', c,'step1')
    if c==1:
        continue 
    print('Run:', c,'step2')
    print('Run:', c,'step3')
# Output: Run: 0 step1
#         Run: 0 step2
#         Run: 0 step3
#         Run: 1 step1      # step2 and step3 are skipped for run 1
#         Run: 2 step1
#         Run: 2 step2
#         Run: 2 step3