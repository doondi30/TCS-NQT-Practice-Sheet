# problem Statement: Adding two fractional numbers.
# Examples:

# Example 1:
# Input: 3/4 + 1/7 
# Output: 25/28
# Explanation: Since 3/4 + 1/7 = 25/28

# Example 2:
# Input: 5/2 +1/2
# Output: 3/1
# Explanation: Since 5/2 + 1/2 = 3/1

a = "5/2 + 1/2"

h = a.split("+")
n = {}
d = {}

for i in range(2):
    x = h[i].strip().split("/") 
    n[i] = int(x[0])
    d[i] = int(x[1])

res1 = (n[0] * d[1]) + (n[1] * d[0])
res2 = d[0] * d[1]

if res1 % res2 == 0:
    res = f"{res1 // res2}/1"
else:
    res = f"{res1}/{res2}"

print(res)

