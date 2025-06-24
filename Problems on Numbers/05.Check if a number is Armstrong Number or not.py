# problem Statement: Given an integer N, return true it is an Armstrong number otherwise return false.

# An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

# Examples
#                 Example 1:
#                 Input:N = 153
               
#                 Output:True
                
#                 Explanation: 1^3+5^3+3^3 = 1 + 125 + 27 = 153
                                        
#                 Example 2:
#                 Input:N = 371                
                
#                 Output: True
                
#                 Explanation: 3^3+5^3+1^3 = 27 + 343 + 1 = 371

n=int(input())
l=len(str(n))
d=n
a=0
while n>0:
    m=n%10
    a=a+(m**l)
    n=n//10
print("True" if a==d else "False")
