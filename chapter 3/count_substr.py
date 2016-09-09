"""
Exercise 3.36: Count substrings
Author: Weiyun Lu
"""

def count_substring(dna,subs):
    s = 0 #initialize the count
    l = len(subs) #length of the substring we are searching for
    for i in range(len(dna)-(l-1)): #is the first letter a match?  we need l-1 remaining entries
        if dna[i] == subs[0]: #if it is indeed a match then...
            if dna[i+1:i+l] == subs[1:l+1]: #then we check if the rest matches
                s +=1
    return s
    
print count_substring('ACGTTACGGACG', 'ACG')            