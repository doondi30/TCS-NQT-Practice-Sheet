# You are given an array of integers and an integer K. Rotate the array circularly to the right by K positions. Output the resulting array.

# Sample Test Cases:
# Test Case 1:

# Input:
# arr = [1, 2, 3, 4, 5]
# K = 2

# Output:
# [4, 5, 1, 2, 3]

# Explanation:
# Right rotation by 1: [5, 1, 2, 3, 4]
# Right rotation by 2: [4, 5, 1, 2, 3]

arr = [1,2,3,4,5,6,7]
l = len(arr)
k = 2
ans = []

for i in range(l - k, l):
    ans.append(arr[i])
for i in range(0, l - k):
    ans.append(arr[i])
print(ans)
