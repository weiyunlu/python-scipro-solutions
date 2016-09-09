"""
Author: Weiyun Lu
Exercise 7.12: Make a class for a summation of series
"""

class Sum:
    def __init__(self, term, M, N):
        self.term = term
        self.M = M
        self.N = N
        
    def __call__(self, x):
        term = self.term
        M = self.M
        N = self.N
        s = 0
        for k in range(M, N+1):
            s += term(k,x)
        return s
        
if __name__ == '__main__':
    term = lambda k, x : (-x)**k
    S = Sum(term, M=0, N=3)
    ans = 0.625
    x = 0.5
    success = S(x) == ans
    msg = 'Sum class is not functionining as intended.'
    assert success, msg
    
    from math import pi, sin, factorial
    sin_term = lambda k, x : (-1)**k * (float(x**(2*k+1)) / factorial(2*k+1))
    x = pi
    S10 = Sum(sin_term, M=0, N=10)
    error = abs(S10(x) - sin(x))
    print 'The 10th degree Taylor approximation of sin(x) is %.12f and the\
        true answer is %.12f, with an error of %.12f.' %(S10(x), sin(x), error)