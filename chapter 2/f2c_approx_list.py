"""
Exercise 2.15: Store data in lists
Author: Weiyun Lu
"""

print '--------------------'
Fn = 0
dF = 10
F = []; C=[]; C2=[]
print '%5s %8s %8s'% ('F', 'C', 'C2')
while Fn <= 100:
    Cn = 5.0/9 * (Fn-32)
    Cn2 = (Fn-30)/2.0
    F.append(Fn), C.append(Cn), C2.append(Cn2)
    Fn = Fn + dF
conversion = [[F[i], C[i], C2[i]] for i in range(len(F))]
for i in range(len(conversion)):
    print '%5d %8.4f %8.4f' % (conversion[i][0], conversion[i][1], conversion[i][2])
print '--------------------'