"""
Exercise 1.11: Compute teh air resistance on a football
Author: Weiyun Lu
"""

from math import pi
g = 9.81 #gravity in m/s^2
ro = 1.2 #density of air in kg/m^3
a = 0.11 #radius of football in m
A = pi * a**2 #cross sectional area of football
cd = 0.2 #drag coefficient
m = 0.43 #mass of football in kg
Vsof = 10 #velocity of soft kick in km/h
Vhar = 120 #velocity of hard kick in km/h
Vsoft = Vsof * (1/3.6)
Vhard = Vhar * (1/3.6)

Fg = m * g #gravity force on the football
Fdsoft = 0.5 * cd * ro * A * Vsoft**2
Fdhard = 0.5 * cd * ro * A * Vhard**2
Rsoft = Fdsoft / Fg
Rhard = Fdhard / Fg

print """The force of gravity on the football is %.1f Newtons.
         For a soft kick, the drag force is %.1f Newtons and the ratio of drag to gravity is %.2f.
         For a hard kick, the drag force is %.1f Newtons and the ratio of drag to gravity is %.2f."""\
         %(Fg,Fdsoft,Rsoft,Fdhard,Rhard)