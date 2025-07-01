# Given an integer array nums. Find the subarray with the largest product, and return the product of the elements present in that subarray.
# A subarray is a contiguous non-empty sequence of elements within an array.
# Examples:
# Input: nums = [4, 5, 3, 7, 1, 2]
# Output: 840
# Explanation: The largest product is given by the whole array itself

# Input: nums = [-5, 0, -2]
# Output: 0

# Explanation: The largest product is achieved with the following subarrays [0], [-5, 0], [0, -2], [-5, 0, -2].
# current solution is correct but has a time complexity of O(n²) due to the nested loops. We can make it far more efficient using Kadane’s algorithm-inspired 
# approach for products

#using kadane's algorithm
n = [4, 5, 3, 0, 1, 2]
c = 1
m = float("-inf")

for i in range(len(n)):
    c *= n[i]
    m = max(m, c)
    if n[i] == 0:
        c = 1 
print(m)

#using builtin math.prod and bruteforce approach
n = [1,2,-3,0,-4,-5]
import math
l=len(n)
maxi=float("-inf")

for i in range(l):
    for j in range(i+1,l):
        k=math.prod(n[i:j+1])
        maxi=max(k,maxi)
print(maxi)
