"""
Exercise 4.9: Promt the user for input to a formula
Author: Weiyun Lu
"""

g = 9.81
v0 = raw_input('Enter initial velocity:')
t = raw_input('Enter time:')
v0 = float(v0); t = float(t)
y = v0*t - 0.5*g*t**2
print 'The height at that time is %6f' %(y)