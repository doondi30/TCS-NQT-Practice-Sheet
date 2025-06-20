# problem Statement: Search an element in an array and return its position
# Example 1:
# Input: array[] = {1,2,3,4,5} k=3                                                                              
# Output: 2                                                                                                             
# Explanation: The answer is 2 because 3 is present at 2nd index.

# Example 2:
# Input: array[]={6,7,9,5,3,10} k=10
# Output: 5
# Explanation: The answer is 5 because 10 is present at 5th index.

arr = [6, 7, 9, 5, 3, 10]
arr.sort()
k = 10

l = 0
r = len(arr) - 1

while l <= r:
    m = l + (r - l) // 2
    if arr[m] == k:
        print(m)
        break
    elif arr[m] > k:
        r = m - 1
    else:
        l = m + 1
