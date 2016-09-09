"""
Exercise 9.12: Understand if a class can be used recursively
Author: Weiyun Lu
"""

from Diff import Central2

f = lambda x : x**4 + 2*x**3 + 3*x**2 + 6*x + 1
ddf = Central2(Central2(f))

print ddf(2) 
#exact value should be 78; we got 78.0000064537
#easy algebra shows that calling Central twice recursively returns (f(x+2h) - f(x+2h) / 4h)