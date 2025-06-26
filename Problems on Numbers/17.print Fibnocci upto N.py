# problem Statement: Given an integer N. Print the Fibonacci series up to the Nth term.

# Examples:

# Example 1:
# Input: N = 5
# Output: 0 1 1 2 3 5
# Explanation: 0 1 1 2 3 5 is the fibonacci series up to 5th term.(0 based indexing)

# Example 2:
# Input: 6

# Output: 0 1 1 2 3 5 8
# Explanation: 0 1 1 2 3 5 8 is the fibonacci series upto 6th term.(o based indexing)

n=5
n1,n2=0,1
for i in range(n+1):
    print(n1,end=' ')
    e=n1+n2
    n1=n2
    n2=e
