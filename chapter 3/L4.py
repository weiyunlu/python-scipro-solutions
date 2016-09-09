"""
Exercise 3.32: Use None in keyword arguments
Author: Weiyun Lu
"""

def L2(x, n):
    s = 0
    for i in range(1, n+1):
        s += (1.0/i)*(x/(1.0+x))**i
    value_of_sum = s
    first_neglected_term = (1.0/(n+1))*(x/(1.0+x))**(n+1)
    from math import log
    exact_error = log(1+x) - value_of_sum
    return value_of_sum, first_neglected_term, exact_error
    
def L3(x, epsilon=1.0E-6):
    x = float(x)
    i = 1
    term = (1.0/i)*(x/(1+x))**i
    s = term
    while abs(term) > epsilon:
        i += 1
        term = (1.0/i)*(x/(1+x))**i
        s += term
    return s, i
    
def L4(x, n=None, epsilon=None, return_n=False):
    if n is not None:
        if epsilon is not None:
            print 'Error!  You cannot specify both n -and- epsilon!'
        else:
            return (L2(x,n)[0], n) if return_n is True else L2(x,n)[0]
    elif epsilon is not None:
        return L3(x,epsilon)[0]
    else:
        print 'Error!  You must specify at least one of n or epsilon!'

#Test run of things that shouldn't work
print L4(13,3,4)
print L4(13)

#Test run of things that should work
print L4(10, n=100)
print L4(10, epsilon=1.0E-6)
print L4(10, n=100, return_n=True)