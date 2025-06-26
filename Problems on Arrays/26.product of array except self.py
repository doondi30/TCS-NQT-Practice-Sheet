a = [1, 2, 3, 4, 5]
l = len(a)
b = [1] * l

for i in range(1, l):
    b[i] = b[i - 1] * a[i - 1]

s = 1
for i in range(l - 1, -1, -1):
    b[i] *= s
    s *= a[i]

print(b)
