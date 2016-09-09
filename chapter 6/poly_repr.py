"""
Exercise 6.10: Compare data structures for polynomials
Author: Weiyun Lu
"""

def poly1(data,x): #evaluating a polynomial stored as a dictionary
    sum = 0.0
    for power in data:
        sum += data[power]*x**power
    return sum
    
def poly2(data,x): #evaluating a polynomial stored as a list
    sum = 0.0
    for power in range(len(data)):
        sum += data[power]*x**power
    return sum
    
p1 = {0: -0.5, 100: 2}

p2 = [0]*101
p2[0] = -0.5
p2[100] = 2

print p1
print p2

print poly1(p1,1.05)
print poly2(p2,1.05)

#timeit poly1(p1,1.05):  
#The slowest run took 6.58 times longer than the fastest. 
#This could mean that an intermediate result is being cached.
#100000 loops, best of 3: 1.96 µs per loop

#timeit poly2(p2,1.05):
#10000 loops, best of 3: 64 µs per loop

#The dictionary is much, much more efficient!