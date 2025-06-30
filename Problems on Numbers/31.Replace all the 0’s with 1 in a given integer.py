# problem Statement: You are given an integer. Your task is to replace all the zeros in the integer with ones.

# Examples:

# Example 1:
# Input: N = 102003
# Output: 112113
# Explanation: The 2nd,4th and 5th position from left contain 0.The resultant integer has replaced the 0’s in those  positions with 1.

# Example 2:
# Input:  204
# Output: 214
# Explanation: The 2nd position from left contain 0. The resultant integer has replaced the 0 in that position with 1.

n = 102003
b = 1
a = 0

while n:
    m = n % 10
    m = 1 if m == 0 else m
    a + = (m * b)
    b = b * 10
    n = n // 10
print(a)
