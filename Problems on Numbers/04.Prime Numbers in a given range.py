# problem Statement: Given a and b, find prime numbers in a given range [a,b], (a and b are included here).

# Examples:

# Examples:
# Input: 2 10
# Output: 2 3 5 7 
# Explanation: Prime Numbers b/w 2 and 10 are 2,3,5 and 7.

# Example 2:
# Input: 10 16
# Output: 11 13 
# Explanation: Prime Numbers b/w 10 and 16 are 11 and 13.


mini, maxi = 12, 50

if mini < 2:
    print(-1)
    mini = 3
elif mini == 2:
    print(2, end=' ')
    mini = 3
elif mini % 2 == 0:
    mini += 1

for i in range(mini, maxi, 2):  # only odd numbers
    flag = True
    for j in range(3, int(i**0.5) + 1, 2):  # checks odd divisors only
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i, end=' ')
