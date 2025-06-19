# Replace elements by its rank in the array

# Problem Statement: Given an array of N integers, the task is to replace each element of the array by its rank in the array.

# Examples:

# Example 1:
# Input: 20 15 26 2 98 6
# Output: 4 3 5 1 6 2
# Explanation: When sorted,the array is 2,6,15,20,26,98. So the rank of 2 is 1,rank of 6 is 2,rank of 15 is 3 and so…

# Example 2:
# Input: 1 5 8 15 8 25 9
# Output: 1 2 3 5 3 6 4
# Explanation: When sorted,the array is 1,5,8,8,9,15,25. So the rank of 1 is 1,rank of 5 is 2,rank of 8 is 3 and so…
# Solution 1:Naive approach

# Intuition: Use two for loops and calculate a rank for each element.

# Approach:

# Iterative over the array using a for loop.
# Now use another for loop to check the number of elements having value less than the current element.
# We can use a set to get the number of unique elements having value less than the current element.
# Number of such unique elements + 1 is the rank of that element.

#count sort used
a=[1,5,8,15,8,25,9]
l=[0]*(max(a)+1)
for i in a:
    l[i]+=1
ans=[]
for i in range(len(l)):
    ans+=[i]*l[i]

#hasing 

dic={}
j=1
for i in ans:
    if i not in dic:
        dic[i]=j
        j+=1
for i in a:
    print(i,dic[i])
