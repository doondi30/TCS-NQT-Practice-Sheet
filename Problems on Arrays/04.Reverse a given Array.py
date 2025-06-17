# Problem Statement: You are given an array. The task is to reverse the array and print it. 

# Examples:

# Example 1:
# Input: N = 5, arr[] = {5,4,3,2,1}
# Output: {1,2,3,4,5}
# Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

# Example 2:
# Input: N=6 arr[] = {10,20,30,40}
# Output: {40,30,20,10}
# Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

n=6
arr=[5,4,3,2,1,9]
l=0
r=n-1
while l<=r:
    arr[l],arr[r]=arr[r],arr[l]
    l+=1
    r-=1
print(arr)
