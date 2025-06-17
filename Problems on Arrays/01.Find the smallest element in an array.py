# Find the smallest element in an array
#
# Problem Statement: Given an array, we have to find the smallest element in the array.
#
# Examples:
#
# Example 1:
# Input: arr[] = {2,5,1,3,0};
# Output: 0
# Explanation: 0 is the smallest element in the array.
#
# Example2:
# Input: arr[] = {8,10,5,7,9};
# Output: 5
# Explanation: 5 is the smallest element in the array.

a=[2,5,1,3,0]
l=len(a)
mini=float("inf")
for i in range(l):
    if a[i]<mini:
        mini=a[i]
print(mini)
