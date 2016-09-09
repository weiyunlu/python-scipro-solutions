"""
Exercise 4.3: Read a number from file
Author: Weiyun Lu
"""

infile = open('f2c_data.txt', 'r')
infile.readline()
infile.readline()
infile.readline()
F = float(((infile.readline()).split())[2])
infile.close()
C = (5.0/9) * (F - 32)
print C