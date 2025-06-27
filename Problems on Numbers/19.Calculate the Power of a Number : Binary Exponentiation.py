# Problem Statement: Given a number N, return all primes till N.

# Examples
#                 Example 1:
#                 Input:x = 2, n = 5
               
#                 Output:32
                
#                 Explanation: Calculate pow(2, 5) = 25 = 2*2*2*2*2 = 32
                                        
#                 Example 2:
#                 Input:x = 21, n = 2                
                
#                 Output: 441
                
#                 Explanation:  Calculate pow(21, 2) = 212 = 21*21 = 441 

x = 21
n = 2
result = 1
while n > 0:
    if n % 2 == 1:
        result *= x
    x *= x
    n //= 2
print(result)



