"""
Exercise 2.1: Make a Fahrenheit-Celcius conversion table
Author: Weiyun Lu
"""

print '--------------------'
F = 0
dF = 10
while F <= 100:
    C = 5.0/9 * (F-32)
    print '%5d %5.1f' % (F, C)
    F = F + dF
print '--------------------'