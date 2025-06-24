# problem statement: Given a number ‘N’, find out the sum of the first N natural numbers.

# Examples:

# Example 1:
# Input: N=5
# Output: 15
# Explanation: 1+2+3+4+5=15

# Example 2:
# Input: N=6
# Output: 21
# Explanation: 1+2+3+4+5+6=15

n=int(input())
N=(n*(n+1))//2
print(N)
