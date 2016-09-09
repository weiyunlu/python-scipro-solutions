"""
Exercise 5.28: Plot the viscosity of water
Author: Weiyun Lu
"""

from scitools.std import plot, linspace

A = 2.414e-5
B = 247.8
C = 140.0
mu = lambda T : A * 10**(B / (T-C)) #viscosity in terms of Kelvin
mu_celcius = lambda T : mu (T+273) #calculate mu in terms of celcius

x = linspace(0,100,100)
y = mu_celcius(x)

plot(x, y, '-b', xlabel='Temperature (C)', ylabel='Viscosity (Pa s)', \
    title='Viscocity of Water')