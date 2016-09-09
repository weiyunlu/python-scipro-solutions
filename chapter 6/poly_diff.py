"""
Exercise 6.11: Compute the derivate of a polynomial
Author: Weiyun Lu
"""

def poly_diff(p):
    dp = {} #initialize empty list for differentiated polynomial
    for power in p:
        dp[power-1] = power * p[power]
    return dp
    
if __name__ == '__main__': #test run
    p = {4: 3, 2: 3, 1: 2} # 3x^4 + 3x^2 + 2x^1
    print poly_diff(p) #should be 12x^3 + 6x^1 + 2
    #output is {0: 2, 1: 6, 3: 12}, as desired