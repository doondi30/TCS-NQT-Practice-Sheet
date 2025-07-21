# Problem Statement: Given an array of N integers, write a program to implement the Bubble Sorting algorithm.

# Examples:

# Example 1:
# Input: N = 6, array[] = {13,46,24,52,20,9}
# Output: 9,13,20,24,46,52
# Explanation: After sorting we get 9,13,20,24,46,52


# Input: N = 5, array[] = {5,4,3,2,1}
# Output: 1,2,3,4,5
# Explanation: After sorting we get 1,2,3,4,5


a=[13,46,24,52,20,9]
l=len(a)
for i in range(l-1,0,-1):
    for j in range(i):
        if a[j+1]<a[j]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)

#optimized 

a = [13, 46, 24, 52, 20, 9]
l = len(a)
for i in range(l - 1, 0, -1):
    swapped = False
    for j in range(i):
        if a[j + 1] < a[j]:
            a[j], a[j + 1] = a[j + 1], a[j]
            swapped = True
    if not swapped:
        break
print(a)
