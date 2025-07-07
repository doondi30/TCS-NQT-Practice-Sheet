# Problem Statement: Given a decimal number, convert it into Octal Number.

# Examples:

# Example 1:
# Input:  17
# Output: 21
# Explanation: Octal Equivalent of 17 is 21

# Example 2:
# Input:  45
# Output: 55
# Explanation: Octal Equivalent of 45 is 55


n=1234
a=''
while n>0:
    m=n%8
    a=str(m)+a
    n=n//8
print(a)
