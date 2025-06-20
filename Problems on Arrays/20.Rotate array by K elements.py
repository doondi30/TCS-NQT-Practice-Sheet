# Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right.

# Examples:

# Example 1:
# Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
# Output: 6 7 1 2 3 4 5
# Explanation: array is rotated to right by 2 position .

# Example 2:
# Input: N = 6, array[] = {3,7,8,9,10,11} , k=3 , left 
# Output: 9 10 11 3 7 8
# Explanation: Array is rotated to right by 3 position.

arr = [1,2,3,4,5,6,7]
l = len(arr)
k = 2
d = input('right/left: ')
ans = []

if d == 'right':
    for i in range(l - k, l):
        ans.append(arr[i])
    for i in range(0, l - k):
        ans.append(arr[i])
else:
    for i in range(k, l):
        ans.append(arr[i])
    for i in range(0, k):
        ans.append(arr[i])

print(ans)
