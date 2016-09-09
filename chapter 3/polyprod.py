"""
Exercise 3.5: Compute a polynomial via a product
Author: Weiyun Lu
"""

def poly(x,roots):
    i = 0 #initialize counter
    p = 1 #initialize product
    while i < len(roots):
        p *= (x - roots[i])
        i += 1
    return p

x = 5
roots = [1, 2, 3]
ans = poly(x,roots)
print 'We compute p(x) = %.6f.' %(ans)