# Problem Statement: Given an array of integers, having some duplicate elements, sort the array by frequency.

# Examples:

# Example 1:
# Input: N = 8, array[] = {1,2,3,2,4,3,1,2}
# Output: 2 2 2 1 1 3 3 4 
# Explanation: Since  2 is present 3 times in an array , so print it 3 times ,then print ‘1’ 2 times and then ‘3’ 2 times and 4 has least frequency, it will be printed at last.

# Example 2:
# Input: N = 6, array[] = {-199,6,7,-199,3,5}
# Output: -199 -199 3 5 6 7
# Explanation: Since -199 is present 2 times so it will be printed at first , then 3 , 5 ,6 ,7 are present once in array , so print them in their sorted order.

l = [-199,6,7,-199,3,5]
dic = {}
for i in l:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

l.sort()
l.sort(key=lambda i: -dic[i])
print(l)
