# problem Statement: Given a number n, express the number as a sum of 2 prime numbers.
#
# Examples
# Example 1:
# Input : N = 74
# Output : True .
# Explanation: 74 can be expressed as 71 + 3 and both are prime numbers.
#
# Example 2:
# Input : N = 11
# Output : False.
# Explanation: 11 cannot be expressed as sum of two prime numbers

n=11
a=[2]
for i in range(3,n+1,2):
    flag=True
    for j in range(3,int(i**0.5)+1,2):
        if i%j==0:
            flag=False
    if flag:
        a.append(i)

l=len(a)
flame=False
for i in range(l-1):
    for j in range(l):
        if a[i]+a[j]==n:
            flame=True
            break
if flame:
    print("True")
else:
    print("False")

