"""
Exercise 3.19: Implement the factorial function
Author: Weiyun Lu
"""
n = input('Enter a natural number to compute the factorial of:')

def fact(n):
    success = n >= 0 and type(n) is int
    msg = 'Type error!  Follow instructions!'
    assert success, msg
    if n == 0:
        return 1
    else:
        k = 1 #initialize product
        i = 1 #initialize counter
        while i <= n:
            k *= i
            i += 1
        return k

ans = fact(n)
print 'The answer is %d.' %(ans)