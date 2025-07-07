# Problem Statement: Given a number, convert it into the form of words.

# Note:- Consider maximum no. of digits in the number as 4.

# Examples:

# Example 1:
# Input: 7824
# Output: seven thousand eight hundred twenty four
# Explanation: 7824 in words can be written as seven thousand eight hundred twenty four.

# Example 2:
# Input: 370
# Output: three hundred seventy
# Explanation: 370 in words can be written as three hundred seventy.

def words(n):
    w = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",11: "eleven",
     12:"twelve", 13: "thirteen", 14: "fourteen",15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty"
     ,30: "thirty", 40:"fourty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}

    if n in w:
        return w[n]

    elif n<100:
        return w[n//10*10]+ " " +w[n%10]

    elif n<1000:
        return w[n//100]+" hundred "+ (words(n%100) if n%100 else " ")

    else:
        return w[n//1000]+" thousand "+(words(n%1000) if n%1000 else " ")

n=7824
print(words(n))
