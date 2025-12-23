# Problem Statement:
# Given an array of N integers, write a program to implement the Selection Sorting algorithm.
# Selection Sort works by repeatedly selecting the minimum element from the unsorted part
# of the array and placing it at the beginning.

# Examples:
#
# Example 1:
# Input: N = 6, array[] = {13, 46, 24, 52, 20, 9}
# Output: 9, 13, 20, 24, 46, 52
# Explanation: After sorting we get 9, 13, 20, 24, 46, 52
#
# Example 2:
# Input: N = 5, array[] = {5, 4, 3, 2, 1}
# Output: 1, 2, 3, 4, 5
# Explanation: After sorting we get 1, 2, 3, 4, 5


# Selection Sort Implementation

a = [13, 46, 24, 52, 20, 9]
n = len(a)

for i in range(n - 1):
    min_index = i  # assume the first element is the minimum
    for j in range(i + 1, n):
        if a[j] < a[min_index]:
            min_index = j
    # swap the found minimum element with the first element
    a[i], a[min_index] = a[min_index], a[i]

print(a)


# Another test case
a = [5, 4, 3, 2, 1]
n = len(a)

for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if a[j] < a[min_index]:
            min_index = j
    a[i], a[min_index] = a[min_index], a[i]

print(a)
