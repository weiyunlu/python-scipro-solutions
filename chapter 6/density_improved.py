"""
Exercise 6.3: Use string operations to improve a program
Author: Weiyun Lu
"""

def makedict(filename):
    mydict = {}
    with open(filename, 'r') as infile:
        for line in infile:
            substance = ' '.join(line.split()[:-1]).strip()
            density = float(line.split()[-1])
            mydict[substance] = density
        return mydict
        
def makedict2(filename):
    mydict={}
    with open(filename, 'r') as infile:
        for line in infile:
            substance = line[:11].strip()
            density = float(line[12:].strip())
            mydict[substance] = density
        return mydict

if __name__ == '__main__':
    import pprint
    pprint.pprint(makedict('densities.dat'))
    pprint.pprint(makedict2('densities.dat'))
    if makedict('densities.dat') == makedict2('densities.dat'):
        print 'The two versions of the function are equivalent.'
    else:
        print 'The two functions are not equivalent!  Fix your stuff, man!'