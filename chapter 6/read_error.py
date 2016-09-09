"""
Exercise 6.4: Interpret output from a program
Author: Weiyun Lu
"""

from scitools.std import semilogy, array

infile = open('lnoutput.txt', 'r')
eps = [] #intialize three empty lists
exa = []
enn = []
for line in infile:
    if line.find('epsilon:') == -1: #if we can't find epsilon, skip this line
        continue
    else: #otherwise, process the line
        words = line.split(',')
        epsilon = float(words[0].split(':')[1].strip())
        exact = float(words[1].split(':')[1].strip())
        n = float(words[2].split('=')[1].strip())
        eps.append(epsilon)
        exa.append(exact)
        enn.append(n)
eps = array(eps) #convert lists to arrays
exa = array(exa)
enn = array(enn)
infile.close()

semilogy(enn, eps, '-b', enn, exa, '-r', xlabel = 'n', ylabel = 'Log of eps/error',
         legend = ['epsilon', 'exact error'], title = 'Ln sum errors')