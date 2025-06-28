# problem Statement: Check if the number is a Harshad(or Niven) number or not.

# Examples:

# Example 1:
# Input: 378
# Output: Yes it is a Harshad number.
# Explanation: 3+7+8=18. 378 is divisible by 18. Therefore 378 is a harshad number.

# Example 2:
# Input: 379
# Output: No
#  it is not a Harshad number.
# Explanation: 3+7+9=19. 379 is not divisible by 19. Therefore 379 is a harshad number

n=378
d=n
a=0

while n:
    m=n%10
    a+=m
    n=n//10
print(" Yes it is a Harshad number." if d%a==0 else"No")
