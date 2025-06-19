# Adding Element in an Array

# Problem Statement: Given an array of N integers, write a program to add an array element at the beginning, end, and at a specific position.

# Example:
# Input: N = 5, array[] = {1,2,3,4,5}
# insertbeginning(6)
# insertending(7)
# insertatpos(8,4)
# Output: 6,1,2,8,3,4,5,7
# Explanation: 6 is added at the beginning and 7 is added at the end and 8 is added at position 4


l = [1, 2, 3, 4, 5]

def insertbeginning(e):
    l.insert(0, e)

def insertending(e):
    l.append(e)

def insertatpos(e, pos):
    if 1<=pos<=len(l)+1:
        l.insert(pos-1,e)
    else:
        print("Invalid position")

insertbeginning(6)
insertending(7)
insertatpos(8, 4)

print(*l)
