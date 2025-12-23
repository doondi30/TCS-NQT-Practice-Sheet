# Problem Statement: Given an array of N integers, write a program to implement the Insertion Sorting algorithm.

# Example:
# Input: N = 6, array[] = {13,46,24,52,20,9}
# Output: 9,13,20,24,46,52

a = [13, 46, 24, 52, 20, 9]
l = len(a)

for i in range(1, l):
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = key

print(a)
