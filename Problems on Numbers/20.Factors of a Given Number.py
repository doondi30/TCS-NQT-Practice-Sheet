# Problem Statement: Find all factors of a number or find all distinct divisors of a natural number.

# Examples:

# Example 1:
# Input: n = 6
# Output: 1,2,3,6
# Explanation: 6 is divisible by 1,2,3,6

# Example 2:
# Input: n = 9
# Output: 1,3,9
# Explanation: 9 is divisible by 1,3,9

n=6
l=set()
i=1
while i*i<=n:
    if n%i==0:
        l.add(i)
        l.add(n//i)
    i+=1
print(sorted(l))
