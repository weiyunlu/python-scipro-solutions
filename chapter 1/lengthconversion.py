"""
Exercise 1.4: Convert from meters to British length units
Author: Weiyun Lu
"""

m = 640 #meters
i = m*100/2.54 #inches
f = i/12.0 #feet
y = f/3.0 #yards
mi = y/1760.0 #miles
print m, 'meters corresponds to', '%.4f inches, %.4f feet, %.4f yards, or %.4f miles' %(i,f,y,mi)