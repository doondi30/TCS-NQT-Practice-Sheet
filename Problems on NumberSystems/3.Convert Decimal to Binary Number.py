# Problem Statement: Convert decimal to binary number.

# Examples:

# Example 1:
# Input: N = 15
# Output: 1111
# Explanation: 15 in binary is represented as "1111".

# Example 2:
# Input: 18
# Output: 10010
# Explanation: 18 in binary is represented as "10010".


n=10
ans=''
while n>0:
    ans=str(n%2)+ans
    n=n//2
print(ans)

