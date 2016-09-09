"""
Author: Weiyun Lu
Exercise 7.24: Find a bug in a class for polynomials
"""

class Polynomial:
    def __init__(self, coefficients):
        self.coeff = coefficients
    
    def __call__(self, x):
        return sum([c*x**i for i, c in enumerate(self.coeff)])
        
    def __add__(self, other):
        maxlength = max(len(self.coeff), len(other.coeff)) 
            #original code of the above line only had len(self), len(other)
        self.coeff += [0]*(maxlength - len(self.coeff))
        other.coeff += [0]*(maxlength - len(other.coeff))
        result_coeff = self.coeff[:] 
            #make a copy, don't mess with the original!
        for i in range(maxlength):
            result_coeff[i] += other.coeff[i]
        return Polynomial(result_coeff)