# prroblem Statement: Perfect Number. Write a program to find whether a number is a perfect number or not.

# A perfect number is defined as a number that is the sum of its proper divisors ( all its positive divisors excluding itself). 

# Examples:

# Example 1:
# Input: n=6
# Output: 6 is a perfect number

# Example 2:
# Input: n=15
# Output: 15 is not a perfect number

# Example 3:
# Input: n=28
# Output: 28 is a perfect number
# Reason:
# For 6 and 28 , the sum of their proper divisors (1+2+3) and (1+4+7+14) is equal to the respective numbers and for 15 it is not.

# Example 1:
# Input: n=6
# Output: 6 is a perfect number

# Example 2:
# Input: n=15
# Output: 15 is not a perfect number

# Example 3:
# Input: n=28
# Output: 28 is a perfect number
# Reason:
# For 6 and 28 , the sum of their proper divisors (1+2+3) and (1+4+7+14) is equal to the respective numbers and for 15 it is not.

#m1

n=int(input())
a=1
for i in range(2,(n//2)+1):
    if n%i==0:
        a+=i
print(f"{n} is a perfect number" if a==n else f"{n} is not a perfect number")


#m2

n = int(input())
a = 1  
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        a += i
        if i != n // i:
            a += n // i
print(f"{n} is a perfect number" if a == n else f"{n} is not a perfect number")
