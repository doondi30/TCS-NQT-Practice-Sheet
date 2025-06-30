# problem Statement: Find permutations in which n people can occupy r seats in a classroom.

# Examples:

# Example 1:
# Input: N = 5, r = 3
# Output: 60
# Explanation: To permute n people in r seats we have to find the value of n!/(n-r)!.The value of 5!/(5-3)! Is 60.

# Example 2:
# Input: N=6,r = 4.
# Output: 360

n=6
r=4

p=1
for i in range(n,(n-r),-1):
    p=p*i
print(p)
