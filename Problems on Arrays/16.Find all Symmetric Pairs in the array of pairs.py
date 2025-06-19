# Problem Statement: Given an array of pairs, find all the symmetric pairs in the array.

# Examples:

# Example 1:
# Input: (1,2),(2,1),(3,4),(4,5),(5,4)
# Output: (2,1) (5,4)
# Explanation: Since (1,2) and (2,1) are symmetric pairs and (4,5) and (5,4) are symmetric pairs.

# Example 2:
# Input: (1,5),(2,3),(4,2),(5,1),(2,4)
# Output: (2,4) (5,1)
# Explanation: Since (1,5) and (2,4) are symmetric pairs and (5,1) and (4,2) are symmetric pairs.

l=[[1,2],[2,1],[3,4],[4,5],[5,4]]
li=len(l)
for i in range(li):
    for j in range(i,li):
        if ( (l[i][0]==l[j][1]) and (l[i][1]==l[j][0]) ):
            print(f"({l[i][1]} {l[i][0]})",end=' ')
            break
