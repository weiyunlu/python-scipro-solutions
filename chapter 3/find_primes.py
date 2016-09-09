"""
Exercise 3.34: Find prime numbers (Eratosthenes' sieve)
Author: Weiyun Lu
"""

from math import sqrt, ceil

def Sieve(n):
    numbers = [] #initialize a list of numbers
    for i in range(2,n+1): #add all numbers from 2 to n to the list
        numbers.append(i)
    m = int(ceil(sqrt(n))) #this is the highest number we need to test multiples for
    p = 0 #count which remaining index must be checked
    while numbers[p] <= m: #as long as the first remaining number is below m...
        k = numbers[p]
        for j in range(2*k, n+1, k): #we must cross out all multiples of k except k
            if j in numbers:
                del numbers[numbers.index(j)]
        p += 1 #now check the next number in the list
    return numbers

print Sieve(100)
    