#prroblem Statement: Given a geometric Progression (G.P) sequence with some inputs as:-

# a, first term
# r, common ratio
# n, number of terms
#  Write a program to find the sum of the geometric Progression Series.

# Examples:

# Example 1:
# Input: a=1 , r=0.5 , n=3
# Output: 1.75
# Explanation: The sum of given GP Series is 1.75

# Example 2:
# Input: a=3 , r=5 , n=2
# Output: 18
# Explanation: The sum of the given GP Series is 18

a=1
r=0.5
n=3

res=a*((r**n)-1)/(r-1)
print(res)
