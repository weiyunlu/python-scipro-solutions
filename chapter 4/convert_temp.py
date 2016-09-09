"""
Exercise 4.19: Make a complete module
Author: Weiyun Lu
"""

import sys

C2F = lambda x : x*9.0/5 + 32
F2C = lambda x : (x - 32) * 5.0/9
C2K = lambda x : x + 273
K2C = lambda x : x - 273
K2F = lambda x : (x - 273)*9.0/5 + 32
F2K = lambda x : (x - 32) * 5.0/9 + 273

def test_conversion():
    eps = 1.0E-10
    success = abs(C2F(F2C(13))-13) < eps and abs(K2C(C2K(131))-131) < eps \
        and abs(K2F(F2K(143))-143) < eps
    msg = 'Conversion error!  Check functions.'
    assert success, msg

if sys.argv[1] == 'verify':
    test_conversion()
    
if __name__ == '__main__':
    print '''
    C2K(0)
    Out[6]: 273
    
    K2C(0)
    Out[7]: -273
    
    K2F(373)
    Out[8]: 212.0
    
    F2C(100)
    Out[9]: 37.77777777777778
    '''