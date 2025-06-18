# Problem Statement: Given an unsorted array, remove duplicates from the array.

# Examples:

# Example 1:
# Input: arr[]={2,3,1,9,3,1,3,9}
# Output:  {2,3,1,9}

# Explanation: Removed all the duplicate elements

# Example 2:
# Input: arr[]={4,3,9,2,4,1,10,89,34}
# Output: {3,4,9,2,1,10,34,89}
# Explanation: Removed all the duplicate elements
# Solution
# Disclaimer: Don't jump directly to the solution, try it out yourself first.

# Solution 1: Brute Force Approach

# Intuition:

# -> We can use an array to store non-duplicate and will return this array

# -> This array will be a boolean array. Corresponding to each index, true means element is Unique else it's duplicate.

# Approach: 

# -> We will place true from i to  n-1 in the mark array

# -> We will use a nested loop. In the outer loop, we will iterate the given array. Let the current number be ‘x’. Now in the inner loop, we will iterate from the given ‘x’ to the end of the array.

# -> If we find ‘x’, we will mark x as false

# -> Same can be done throughout for each element of the array

#Using Hashmap 

arr=[4,3,9,2,4,1,10,89,34]
dic={}
for i in arr:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for i in dic:
    print(i,end=' ')
