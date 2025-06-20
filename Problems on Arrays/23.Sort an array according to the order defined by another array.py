#Problem Statement: You are given two arrays A1 and A2. Sort A1 such that the relative order of items in A1 is the same as those in A2.
#Elements of A1 not present in A2 should be placed at the end in ascending order.

# Test Case 1:

# Input:
# A1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
# A2 = [2, 1, 8, 3]

# Output:
# [2, 2, 1, 1, 8, 8, 3, 5, 6, 7, 9]

# Explanation:

# First include 2s in order → [2, 2]

# Then 1s → [1, 1]

# Then 8s → [8, 8]

# Then 3 → [3]

# Remaining (not in A2): 5, 6, 7, 9 → sort → [5, 6, 7, 9]

# Test Case 2:

# Input:
# A1 = [4, 5, 6, 7]
# A2 = [7, 5]

# Output:
# [7, 5, 4, 6]

# Explanation:
# First elements in A2 appear in A1, then remaining in sorted order.

l1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
l2 = [2, 1, 8, 3]

res = []
for i in l2:
    if i in l1:
        res+=[i]*l1.count(i)

remaining = sorted(set(l1) - set(l2))
for i in remaining:
    res += [i] * l1.count(i)
print(res)


