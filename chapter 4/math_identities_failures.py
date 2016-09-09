"""
Exercise 4.22: Check if mathematical identities hold (round-off errors)
Author: Weiyun Lu
"""

import random
from math import exp, log, sin, tan, sinh, cos

#Part a
def power3_identity(A=-100, B=100, n=1000):
    failures = 0
    for i in range(1000):
        a = random.uniform(A,B)
        b = random.uniform(A,B)
        if (a*b)**3 != a**3*b**3:
            failures +=1
    return float(failures)/n
    
print 'The ratio of failures of power3_identity is', power3_identity(A=-100, B=100, n=1000)

#Part b
def equal(expr1, expr2, A=-100, B=100, n=500):
    failures = 0
    i = 0
    while i < n:
        a = random.uniform(A,B)
        b = random.uniform(A,B)
        try:
            f = eval(expr1)
            g = eval(expr2)
        except:
            continue
        if f != g:
            failures += 1
        i += 1
    return float(failures)/n
    
cube_ratio = equal('(a*b)**3', 'a**3 * b**3')
exp_ratio = equal('exp(a+b)', 'exp(a)*exp(b)')
log_ratio = equal('log(a**b)', 'b*log(a)')

print 'The ratio of failures of cube, exp, and log equalities are, respectively,', cube_ratio,\
     ',', exp_ratio, ', and', log_ratio, '.'
     
#Part c
X = [('a-b', '-(b-a)'), ('a/b', '1/(b/a)'), ('(a*b)**4', 'a**4 * b**4'), ('(a+b)**2', \
    'a**2 + 2*a*b + b**2'), ('(a+b)*(a-b)', 'a**2 - b**2'), ('exp(a+b)', 'exp(a)*exp(b)'), \
    ('log(a**b)', 'b*log(a)'), ('log(a*b)', 'log(a) + log(b)'), ('a*b', 'exp(log(a)+log(b))'), \
    ('1/(1/a + 1/b)', '(a*b)/(a+b)'), ('a*(sin(b)**2 + cos(b)**2)', 'a'), ('sinh(a+b)', \
    '(exp(a)*exp(b)-exp((-a)*(-b)))/2'), ('tan(a+b)', 'sin(a+b)/cos(a+b)'), ('sin(a+b)', \
    'sin(a)*cos(b)+sin(b)*cos(a)')]
    
def table(data, A0, B0, n=1000):
    print 'Error ratio per 1000 trials with random numbers from (%d, %d)' %(A0, B0)
    print '-'*60
    print '%45s %12s' %('Expression', 'Ratio of errors')
    for i in range(len(data)):
        print '%45s %12.8f' %(X[i][0] + '=' + X[i][1], equal(X[i][0],X[i][1],A=A0, B=B0))

table(X, A0=-100, B0=100)
print '\n'
table(X, A0=1, B0=2)
print '\n'
table(X, A0=1, B0=100)