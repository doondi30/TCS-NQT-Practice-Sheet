# Problem Statement: Convert a binary number to a decimal number.

# Examples:

# Example 1:
# Input: N = 1011
# Output: 11
# Explanation: 1011 when converted to decimal number is “11”.

# Example 2:
# Input: 100
# Output: 4
# Explanation: 100 when converted to decimal number is “4"

n=100
d=n
p=0
a=0
while n>0:
    m=n%10
    a=a+m*(2**p)
    n=n//10
    p+=1
print(a)
