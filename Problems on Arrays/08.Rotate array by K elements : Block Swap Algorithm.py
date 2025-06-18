# Problem Statement: Given an array of n size, rotate the array by k elements

# Examples:

# Example 1:
# Input: N = 5, array[] = {1,2,3,4,5} K=2
# Output: {3,4,5,1,2}
# Explanation: Rotate the array to right by 2 elements.

# Example 2:
# Input: N = 7, array[] = {1,2,3,4,5,6,7} K=3
# Output: {4,5,6,7,1,2,3}
# Explanation: Rotate the array to right by 3 elements.

arr = [3, 4, 1, 5, 3, -5]
k = 8 #given to rotate array
l=len(arr)
k = k if (k<l) else k%l
ans=[]
for i in range(k,l):
    ans.append(arr[i])
for i in range(k):
    ans.append(arr[i])
print(ans)
