# problem Statement: Given an integer. Write a program to reverse digits of a number.

# Examples:

# Example 1:
# Input: N = 472
# Output: 274
# Explanation: Reading the number from back to front, we see that the output should be 274

# Example 2:
# Input: N = 470
# Output: 74
# Explanation: Reading the number from back to front, we get 074. For an integer with no decimals, we know that leading zeros have no significance and therefore our answer should be 74

n=-12345789
d=-1 if n<1 else 1
n=n*d
a=0
while n>0:
    m=n%10
    a=m+a*10
    n=n//10
print(a*d)
