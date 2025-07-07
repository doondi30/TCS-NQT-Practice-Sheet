# Problem Statement: Convert a binary number to an octal number

# Examples:

# Example 1:.
# Input: N = 1100110
# Output: 146
# Explanation: 1100110 when converted to octal number is “146”.

# Example 2:
# Input: 11111
# Output: 37
# Explanation: 11111 when converted to octal number is “37”.

n = 1010
# Step 1: Convert binary (as decimal input) to decimal number
d = n
p = 0
a = 0
while n > 0:
    m = n % 10
    a = a + m * (2 ** p)
    n = n // 10
    p += 1

# Step 2: Convert decimal to octal
n = a
a = ''
while n > 0:
    m = n % 8
    a = str(m) + a
    n = n // 8

print(a)

