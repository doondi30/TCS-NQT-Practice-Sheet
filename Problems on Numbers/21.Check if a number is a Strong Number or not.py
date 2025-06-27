# Problem Statement: Given an integer Print “YES” if it is a strong number else print “NO”.

# Note : 

# When the sum of factorial of individual digits of a number is equal to the original number the number is called a strong number. 
# Strong number is also known as Krishnamurthi number/Peterson Number.
# Examples:

# Examples 1:
# Input: N = 145
# Output: Yes
# Explanation: 1! + 4! + 5! = 145. Hence 145 is a strong number. 

# Example 2:
# Input:  26
# Output: No
# Explanation: 2! + 6! = 722. Hence 26 is not a strong number

n=145
d=n
a=[]
while n:
    m=n%10
    a.append(m)
    n=n//10
res=0
for i in a:
    res+=math.factorial(i)
print(res==d)
