"""
Exercise 5.14: Plot data in a two-column file
Author: Weiyun Lu
"""

from scitools.std import plot, array, average

myfile = open('xydat.txt', 'r')
x = []
y = []

for line in myfile:
    w1 = float(line.split()[0])
    w2 = float(line.split()[1])
    x.append(w1)
    y.append(w2)

plot(x, y)
y = array(y)
avg = average(y)
maxi = max(y)
mini = min(y)
myfile.close()

print 'The mean is', avg, 'the min value is', mini, 'and the max value is', maxi, '.'