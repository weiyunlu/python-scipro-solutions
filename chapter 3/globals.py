"""
Exercise 3.10: Simulate a program by hand (global vs local variables)
Author: Weiyun Lu
"""

def a(x):
    q = 2
    x = 3*x
    return q + x
    
def b(x):
    global q
    q += x
    return q + x
    
q = 0
x = 3
print a(x), b(x), a(x), b(x), a(x), b(x)