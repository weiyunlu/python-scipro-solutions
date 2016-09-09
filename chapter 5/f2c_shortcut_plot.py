"""
Exercise 5.12: Plot exact and inexact Fahrenheit-Celcius conversion formulas
Author: Weiyun Lu
"""

from scitools.std import linspace, plot

F = linspace(-20,120,20)
C_approx = (F-30) / 2.0
C_actual = (F-32) * 5.0/9

plot(F, C_approx, '-r', F, C_actual, '-b', legend=('approx C', 'actual C'),\
        xlabel='Fahrenheit', ylabel='Celcius')