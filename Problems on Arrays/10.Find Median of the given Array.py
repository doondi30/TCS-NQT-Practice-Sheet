# Problem Statement: Given an unsorted array, find the median of the given array.

# Examples:

# Example 1:
# Input: [2,4,1,3,5]
# Output: 3

# Example 2:
# Input: [2,5,1,7]
# Output: 3.5
# What is a Median?
# Median is defined as the value which is present in the middle for a series of values. Note, in order to find the median of an array of integers, we must make sure they are sorted.

#count sort o(n) applied to sort the unsorted array
n=[2,5,1,7]
l=[0]*(max(n)+1)
for i in n:
    l[i]+=1
ans=[]
for i in range(len(l)):
    ans+=[i]*l[i]
# print(ans)

length=len(n)
answer=0
if length%2!=0:
    answer=length//2
    print(ans[answer])
else:
    answer=ans[length//2]+ans[(length//2)-1]
    answer=round(answer/2,2)
    print(answer)

