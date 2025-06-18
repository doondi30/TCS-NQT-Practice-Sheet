# Problem Statement: Given an array, we have to find the average of all the elements in the array.

# Examples:

# Example 1:
# Input: N = 5, array[] = {1,2,3,4,5}
# Output: 3
# Explanation: Average is the sum of all the elements divided by number of elements.Therefore (1+2+3+4+5)/5 = 3.

# Example 2:
# Input:  N=6, array[] = {1,2,1,1,5,1}
# Output: 1.8
# Explanation: Average is the sum of all the elements divided by number of elements.Therefore (1+2+1+1+5+1)/6 = 1.8

arr=[1,2,1,1,5,1]
l=len(arr)
ans=0
for i in range(l):
    ans+=arr[i]
avg=round(ans/l,1)
print(avg)
