"""
Exercise 3.33: Write a sort function for a list of 4-tuples
Author: Weiyun Lu
"""

data = [
('Alpha Centauri A',    4.3,  0.26,      1.56),
('Alpha Centauri B',    4.3,  0.077,     0.45),
('Alpha Centauri C',    4.2,  0.00001,   0.00006),
("Barnard's Star",      6.0,  0.00004,   0.0005),
('Wolf 359',            7.7,  0.000001,  0.00002),
('BD +36 degrees 2147', 8.2,  0.0003,    0.006),
('Luyten 726-8 A',      8.4,  0.000003,  0.00006),
('Luyten 726-8 B',      8.4,  0.000002,  0.00004),
('Sirius A',            8.6,  1.00,      23.6),
('Sirius B',            8.6,  0.001,     0.003),
('Ross 154',            9.4,  0.00002,   0.0005),
]

def table(data, a_key):
    print '---------------------------------------------------------'  
    print '%20s %10s %10s %10s' %('Star name', 'dist. sun', 'Brightness', 'Luminosity')
    print '---------------------------------------------------------'    
    for row in sorted(data, key=a_key):
        print '%20s %10.1f %10.6f %10.6f' %row
    print '---------------------------------------------------------'
    
print 'Sorted by distance from sun:'
table(data, lambda a : a[1])

print 'Sorted by brightness:'
table(data, lambda a : a[2])

print 'Sorted by luminosity:'
table(data, lambda a : a[3])