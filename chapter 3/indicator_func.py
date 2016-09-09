"""
Exercise 3.25: Implement an indicator function
Author: Weiyun Lu
"""

I = lambda x, L, R : 1 if L <= x <= R else 0 #direct definition

def H(x): #the Heaviside function
    if x < 0:
        return 0
    elif x >= 0:
        return 1
        
I2 = lambda x, L, R : H(x - L) * H(R - x) #in terms of Heaviside

L = -5
R = 5

testvalues = [-7, -5, 0, 5, 7]

for x in testvalues:
    print 'I of', x, 'is', I(x, L, R), '.'
    print 'I2 of', x, 'is', I2(x, L, R), '.'