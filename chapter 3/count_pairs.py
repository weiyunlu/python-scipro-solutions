"""
Exercise 3.35: Find pairs of characters
Author: Weiyun Lu
"""

def count_pairs(dna, pair):
    s = 0 #initialize the count
    for i in range(len(dna)-1):
        if dna[i] == pair[0] and dna[i+1] == pair[1]:
            s +=1
    return s
    
print count_pairs('ACTGCTATCCATT', 'AT')