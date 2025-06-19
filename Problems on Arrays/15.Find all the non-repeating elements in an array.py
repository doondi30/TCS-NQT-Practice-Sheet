# Find all the non-repeating elements in an array
# Problem Statement: Find all the non-repeating elements for a given array. Outputs can be in any order.

# Examples:
# Example 1:
# Input:
#  Nums = [1,2,-1,1,3,1]
# Output:
#  2,-1,3
# Explanation:
#  1 is the only element in the given array which occurs thrice in the array. -1,2,3 occurs only once and hence, these are non-repeating elements of the given array.

# Example 2:
# Input:
#  Nums = [1,2,3]
# Output:
#  1,2,3
# Explanation:
#  All elements present in the array occur once. Hence, every element is non-repeating.
# Solution:

arr=[1,2,-1,1,3,1]
dic={}
for i in arr:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for i in dic:
    if dic[i]==1:
        print(i,end=' ')
