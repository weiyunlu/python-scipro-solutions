"""
Exercise 2.14: Index a nested list
Author: Weiyun Lu
"""

q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]
print q[0][0] #extract the letter 'a'
print q[1] #extract list (d,e,f)
print q[-1][-1] #extract the last element 'h'
print q[1][0] #extract letter 'd'

for i in q: #i are the lists of elements qithin q
    for j in range(len(i)): #j are the letters within the list
        print i[j]