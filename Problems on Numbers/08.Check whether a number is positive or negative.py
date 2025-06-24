# problem statement: Given a number n check whether it's positive or negative.

# Examples:

# Example 1:
# Input: n=5
# Output: Positive

# Example2:
# Input: n=-6
# Output: Negative

n = int(input())
print("Positive" if n > 0 else ("Negative" if n < 0 else "Zero"))
