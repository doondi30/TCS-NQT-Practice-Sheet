# prblem Statement: Check if the given year is a leap year or not.

# Examples:

# Example 1:
# Input: 1996
# Output: Yes
# Explanation: Since 1996 is a leap year answer is “Yes”.

# Example 2:
# Input: 2000
# Output: Yes

# Explanation: Since 2000 is a leap year answer is “Yes”.

n=int(input())
if n%4==0 and (n%100!=0 or n%400==0):
    print("Yes")
else:
    print("No")
