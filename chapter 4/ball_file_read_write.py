"""
Exercise 4.14: Evaluate a formula for data in a file
Author: Weiyun Lu
"""

g = 9.81

def read_file(F):
    v0 = float( ((F.readline()).split())[1] )
    F.readline()
    t_values = []
    for line in F:
        line_values = line.split()
        for t in line_values:
            t_values.append(float(t))
    return v0, t_values

def make_table(G):
    v0 = G[0]
    G[1].sort()
    print '%15s %15s' %('Time', 'Position')
    print '----------------------------------'
    for t in G[1]:
        y = v0*t - 0.5*g*t**2
        print '%15.12f %15.12f' %(t, y)
        
def test_read():
    velo = 5
    vals = [0.2, 1.3, 1]
    outfile = open('ball_test.txt', 'w')
    outfile.write('v0: 5\nt:\n0.2 1.3\n1')
    outfile.close()
    testfile = open('ball_test.txt', 'r')
    success = read_file(testfile) == (velo, vals)
    testfile.close()
    msg = 'Test for read_file failed!'
    assert success, msg
    
test_read()
filename = raw_input('Enter the name of a text file including the extension: ')
FILE = open(filename, 'r')
READFILE = read_file(FILE)
make_table(READFILE)
FILE.close()