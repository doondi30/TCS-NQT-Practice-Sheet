# problem Statement: Check if the number is an abundant number or not.

# Examples:

# Example 1:
# Input: 18
# Output: Abundant Number
# Explanation: Divisors of 18 are 1,2,3,6,9. 1+2+3+6+9=21, Since 21 is greater than 18, 18 is an abundant number.

# Example 2:
# Input: 21
# Output: Not Abundant Number
# Explanation:Divisors of 21 are 1,3,7. 1+3+7=11, Since 11 is smaller than 21, 11 is not an abundant number.
# Definition: If the sum of divisors of a number is greater than the number then it is called abundant number.

n=18
d=n
l=[]
i=1
while i*i<=n:
    if n%i==0:
        l.append(i)
        l.append(n//i)
    i+=1
ans=0
for i in range(len(l)):
    ans+=l[i]
ans-=d
print("Abundant Number" if ans>d else "Not a Abundant Number")
