"""
Exercise 3.29: Simulate nested loops by hand
Author: Weiyun Lu
"""

n = 3

for i in range(1, n+1):
    for j in range(i):
        if j:
            print i, j

#Here's what happens.
#First, we loop over i = 1, 2, 3
#When i = 1, we look at j = 0.  if j fails for 0, so nothing prints.
#When i = 2, we look at j = 0, 1.  j succeeds for 1, so we print 2 1.
#When i = 3, we look at j = 0, 1, 2.  j succeeds for 1 and 2.

print '----------'

for i in range(1, 13, 2*n):
    for j in range(n):
        print i, j
        
#Here's what happens.
#We loop over i = 1, 7.  Adding 6 again gets us to 13, which is not included.
#For i = 1, we look at j = 0,1,2 and print 1 0, 1 1, 1 2.
#For i = 7, we look at j = 0,1,2 and print 7 0, 7 1, 7 2.
        
print '----------'

for i in range(-1,n):
    if i != 0:
        print i

#Here's what happens.
#We loop over i = -1, 0, 1, 2.
#For the values -1, 1, 2, the test succeeds and we print the number.

print '----------'

for i in range(1, 13, 2*n):
    for j in range (0, i, 2):
        for k in range (2, j, 1):
            b = i > j > k
            if b:
                print i, j, k
                
#Here's what happens.
#We loop first over i = 1, 7.
#When i = 1, we look at j = 0 only (adding 2 goes above the top of the range).
    #With i = 1, j = 0, we look at k values from 2 to j... which don't exist.
#Now let i = 7.  We look at j = 0, 2, 4, 6.
    #With i = 7, j = 0, 2 again give us no range to work with.
    #With i = 7, j = 4, we look at k = 2, 3.
            #i > j > k is true in both cases.
            #We print 7 4 3 and 7 4 2.
    #With i = 7, j = 6, we look at k = 2,3,4,5.
            #Print the 4 values, which all pass the test.
