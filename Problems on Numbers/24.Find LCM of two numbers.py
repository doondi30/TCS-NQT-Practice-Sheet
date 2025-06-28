# problem Statement: Find lcm of two numbers.

# Examples:

# Example 1:
# Input: num1 = 4,num2 = 8
# Output: 8


# Example 2:
# Input: num1 = 3,num2 = 6
# Output: 6

n1=3
n2=6
for i in range(max(n1,n2),1+(n1*n2),max(n1,n2)):
    if i%n1==i%n2==0:
        lcm=i
        break
print(lcm)


