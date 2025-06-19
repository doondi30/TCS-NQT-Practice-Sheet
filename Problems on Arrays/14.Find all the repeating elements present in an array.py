# Problem Statement: Find all the repeating elements present in an array.

# Examples:

# Example 1:
# Input: 
# Arr[] = [1,1,2,3,4,4,5,2]
# Output:
#  1,2,4
# Explanation:
#  1,2 and 4 are the elements which are occurring more than once.

# Example 2:
# Input:
#  Arr[] = [1,1,0]
# Output:
#  1
# Explanation:
#  Only 1 is occurring more than once in the given array.

arr=[1,1,2,3,4,4,5,2]
dic={}
for i in arr:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for i in dic:
    if dic[i]>1:
        print(i,end=' ')
