# problem Statement: Finding Equilibrium index in an array

# Given a 0-indexed integer array nums, find the leftmost equilibrium Index.

# An equilibrium Index is an index at which sum of elements on its left is equal to the sum of element on its right. That is, nums[0] + nums[1] + ... + nums[equilibriumIndex-1] == nums[equilibriumIndex+1] + nums[equilibriumIndex+2] + ... + nums[nums.length-1]. If equilibriumIndex == 0, the left side sum is considered to be 0. Similarly, if equilibriumIndex == nums.length - 1, the right side sum is considered to be 0.

# Return the leftmost equilibrium Index that satisfies the condition, or -1 if there is no such index.

# Example 1:
# Input: nums = [2,3,-1,8,4]
# Output: 3
# Explanation: The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
# The sum of the numbers after index 3 is: 4 = 4

# Example 2:
# Input: nums = [1,-1,4]
# Output: 2
# Explanation: The sum of the numbers before index 2 is: 1 + -1 = 0
# The sum of the numbers after index 2 is: 0

#method-1

arr = [1, -1, 4]
l = len(arr)
l1 = []
l2 = []

for i in range(l):
    total = 0
    for j in range(i):
        total += arr[j]
    l1.append(total)

for i in range(l):
    total = 0
    for j in range(i + 1, l):
        total += arr[j]
    l2.append(total)

for i in range(l):
    if l1[i] == l2[i]:
        print(i)
        break
      
#method-2

arr = [1, -1, 4]
l = len(arr)
for i in range(l):
    if sum(arr[:i]) == sum(arr[i+1:]):
        print(i)
        break
