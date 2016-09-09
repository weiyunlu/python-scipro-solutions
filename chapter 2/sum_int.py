"""
Exercise 2.5: Sum of first n integers
Author: Weiyun Lu
"""

n = 198 #set n
s = 0 #sum counter
i = 1 #index counter
while i <= n:
    s = s + i
    i = i + 1
print 'The computed sum from 1 to %d is %d.' % (n, s)
t = n*(n+1)/2
print 'Using the formula n(n+1)/2 yields %d.' % (t)