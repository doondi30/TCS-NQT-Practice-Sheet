# problem Statement: Given an integer, find the sum of digits of that integer.

# Examples:

# Input: N = 472
# Output: 13
# Explanation: The digits in the number are 4,7 and 2. Summing them up gives us a value of 13

# Example 2:
# Input: N = 102
# Output: 3
# Explanation: The digits in the number are 0, 1, and 2. Summing them up gives us a value of 3


n=472
d=n
a=0
while n>0:
    m=n%10
    a=a+m
    n=n//10
print(a)

