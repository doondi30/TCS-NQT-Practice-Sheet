# problem Statement: Given an Octal Number, convert it into Binary Number.

# Examples:

# Example 1:
# Input: 345
# Output: 011100101
# Explanation: Binary equivalent of given Octal expressionis 011100101

# Example 2:
# Input: 170
# Output: 001111000
# Explanation: Binary equivalent of given Octal expression is 001111000

n = "2322"
a = ""
if n == "0":
    a = "0"
else:
    for i in n:
        if i == "0":
            a += "000"
        elif i == "1":
            a += "001"
        elif i == "2":
            a += "010"
        elif i == "3":
            a += "011"
        elif i == "4":
            a += "100"
        elif i == "5":
            a += "101"
        elif i == "6":
            a += "110"
        elif i == "7":
            a += "111"
print(a.lstrip("0"))

