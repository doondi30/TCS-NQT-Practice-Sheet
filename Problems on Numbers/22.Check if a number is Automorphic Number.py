# Problem Statement: Given a number, check if it is automorphic or not. A number is called an Automorphic number if and only if its square ends in the same digits as the number itself.

# Examples:

# Example 1:
# Input Format: N = 76
# Result: Automorphic Number
# Explanation: Calculating 76 * 76 gives 5776, it ends with the given number.

# Input Format: 25
# Result: Automorphic Number
# Explanation: Calculating 25 * 25 gives 625, it ends with the given number.

n=25
h=str(n*n)
print(h.endswith(str(n)))
