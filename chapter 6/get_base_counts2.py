"""
Exercise 6.17: Make a function more robust
Author: Weiyun Lu
"""

from collections import defaultdict

#so that it doesn't crash on strings containing other letters not in DNA.

def get_base_counts2(dna):
    counts = defaultdict(lambda: 0) 
    counts.update({'A': 0, 'T': 0, 'G': 0, 'C': 0})
    for base in dna:
        counts[base] += 1
    return counts