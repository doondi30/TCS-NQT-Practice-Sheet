# Check if array is subset of another array.

# Write a program to find whether an array is a subset of another array or not.

# Given arr1[] and arr2[], we need to find whether arr1[] is a subset of arr2[]. 
# An array is called a subset of another if all of its elements are present in the other array.

# Note: Array elements are assumed to be unique.

# Examples:
		  
# Example 1:
# Input: arr1[]= [1,3,4,5,2]
#        arr2[]= [2,4,3,1,7,5,15]
# Output: arr1[] is a subset of arr2[]

# Example 2:
# a1 = [1, 1]
# a2 = [1]  # Only one occurrence of 1
# Output: arr1[] is  a subset of arr2[]

# Example 3:
# Input: arr1[]= [1,3,4,5,2]
#        arr2[]= [11,12,13,15,16]
# Output: arr1[] is not a subset of arr2[]


a1=[1,3,4,5,2]
a2=[2,4,3,1,7,5,15]

d1={}
for i in a2:
    if i in d1:
        d1[i]+=1
    else:
        d1[i]=1

flag=1
for i in a1:
    if i in d1 and d1[i]>0:
        d1[i]-=1
    else:
        flag=0
        break

if flag==1:
    print("arr1[] is a subset of arr2[]")
else:
    print("arr1[] is not a subset of arr2[]")

