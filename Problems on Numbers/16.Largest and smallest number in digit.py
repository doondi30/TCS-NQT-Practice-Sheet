# problem Statement: Given a number N, print the smallest and largest digits present in the number.

# Examples:

# Example 1:
# Input: N = 2746
# Output: Largest digit: 7
#         Smallest digit: 2
# Explanation: By simply going through the digits of 
# the number, we figure out the largest and smallest 
# digit in the number.

# Example 2:
# Input: N = 23004
# Output: Largest digit : 4
#         Smallest digit : 0
# Explanation: By simply going through the digits of 
# the number, we figure out the largest and smallest 
# digit in the number.

n="98541234559666906806"
z=[]
for i in n:
    z.append(int(i))
l=[0]*(max(z)+1)
for i in z:
    l[i]+=1
t=[]
for i in range(len(l)):
    t+=[i]*l[i]
print(t[0],t[-1])
