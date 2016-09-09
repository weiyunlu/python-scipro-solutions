"""
Exercise 1.6: Compute the growth of money in a bank
Author: Weiyun Lu
"""

p = 5.0 #interest rate
A = 1000.00 #initial amount
n = 3.0 #three years
answer = A*(1+(p/100))**n
print 'With an initial investment of $%.2f at interest rate %.2f%%, \
       after %d years, we will have $%.2f.' %(A,p,n,answer)