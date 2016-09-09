"""
Exercise 2.2: Generate an approximate Fahrenheit-Celcius conversion table
Author: Weiyun Lu
"""

print '--------------------'
F = 0
dF = 10
print '%5s %8s %8s'% ('F', 'C', 'C2')
while F <= 100:
    C = 5.0/9 * (F-32)
    C2 = (F-30)/2.0
    print '%5d %8.2f %8.2f' % (F, C, C2)
    F = F + dF
print '--------------------'