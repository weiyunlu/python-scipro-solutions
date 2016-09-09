"""
Author: Weiyun Lu
Exercise 7.28: Use a dict to hold polynomial coefficients
"""

class Polynomial:
    def __init__(self, coeff):
        self.coeff = coeff
    
    def __add__(self, other):
        c = self.coeff
        d = other.coeff
        result = {} #initialize empty result dictionary
        for key in c: #add coefficients to self from other, store in result
            if key in d:
                result[key] = c[key] + d[key]
            else:
                result[key] = c[key]
        for key in d: #add coeffecients only in other to result
            if key not in c:
                result[key] = d[key]
        #we don't need to include zero values - that's the whole point of using
        #a dictionary to store polynomials!
        result_unzero = {} 
        for key in result:
            if result[key] != 0:
                result_unzero[key] = result[key]
        return Polynomial(result_unzero)
        
    def __mul__(self, other):
        c = self.coeff
        d = other.coeff
        M = max(c)
        N = max(d)
        R = M+N+1
        result = {key: 0 for key in range(R)}
        for i in range(0,M+1):
            for j in range(0,N+1):
                if i in c and j in d:
                    result[i+j] += c[i]*d[j]
        result_unzero = {}
        for key in result:
            if result[key] != 0:
                result_unzero[key] = result[key]
        return Polynomial(result_unzero)
        
if __name__ == '__main__':        
    f = Polynomial({1:1, 100:-3})
    g = Polynomial({1:-1, 20:1, 100:4})
    p = f+g
    q = f*g
    p_ans = {20:1, 100:1}
    q_ans = {2:-1, 21:1, 101:7, 120:-3, 200:-12}
    success = (p.coeff == p_ans) and (q.coeff == q_ans)
    msg = 'Something funky is going on.  Fix it.'
    assert success, msg
    print 'f = ', f.coeff
    print 'g = ', g.coeff
    print 'f+g = ', p.coeff
    print 'f*g = ', q.coeff