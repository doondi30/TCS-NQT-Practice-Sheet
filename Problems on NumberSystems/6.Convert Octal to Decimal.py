# Problem Statement: Given an Octal Number, convert it into a Decimal Number.

# Examples:

# Example 1:
# Input: 345
# Output: 229
# Explanation: Decimal equivalent of given Octal expressionis 229

# Example 2:
# Input: 170
# Output: 121
# Explanation: Decimal equivalent of given Octal expression is121

n=512
base,a=1,0
while n>0:
    m=n%10
    a=a+(m*base)
    n=n//10
    base=base*8
print(a)

