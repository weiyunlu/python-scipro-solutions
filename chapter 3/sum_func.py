"""
Exercise 3.2: Evaluate a sum and write a test function
Author: Weiyun Lu
"""

def sum_1K(M):
    s = 0 #initialize the sum.
    for k in range(1,M+1):
        s += 1.0/k
    return s
    
M = 3

def test_sum_1k():      #test if the value matches the computed value
    val = 1.833333333333333  #the correct value
    eps = 1.0E-16       #error tolerance
    val2 = sum_1K(3)    #test value
    if abs(val - val2) < eps:
        success = True
    else:
        success = False
    msg = 'The function is incorrect.'
    assert success, msg

test_sum_1k()
print 'The sum from 1 to M is %.6f' %sum_1K(M)