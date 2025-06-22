# problem Statement: Given an integer N, return true if it is a palindrome else return false.

# A palindrome is a number that reads the same backward as forward. For example, 121, 1331, and 4554 are palindromes because they remain the same when their digits are reversed.

#                 Example 1:
#                 Input:N = 4554
               
#                 Output:Palindrome Number
                
#                 Explanation: The reverse of 4554 is 4554 and therefore it is palindrome number
                                        
#                 Example 2:
#                 Input:N = 7789                
                
#                 Output: Not Palindrome
                
#                 Explanation: The reverse of number 7789 is 9877 and therefore it is not palindrome


n=5445
l=len(str(n))-1
d=n
a=0
while n:
    m=n%10
    a=m*(10**l)+a
    n=n//10
    l-=1
print("Palindrome Number" if a==d else "Not Palindrome")
