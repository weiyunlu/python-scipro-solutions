"""
Exercise 9.18: Make a calculus calculator class
Author: Weiyun Lu
"""

from Diff import *
from integrate import *
import sys
sys.path.insert(0, '../chapter 7')
from minmaxf import *
from numpy import *
import matplotlib.pyplot as plt

class CalculusCalculator:
    def __init__(self, f, a, b, resolution=1000):
        self.f, self.a, self.b, self.resolution = f, a, b, resolution
        self.dx_method = Central2
        self.int_method = Trapezoidal
        self.h = 1E-5
        
    def extreme_points(self):
        MM = MinMax(self.f, self.a, self.b, self.resolution)
        print MM
        
    def df(self, x):
        df_compute = self.dx_method(self.f, self.h)
        return df_compute(x)
        
    def integral(self):
        int_compute = self.int_method(self.a, self.b, self.resolution)
        return int_compute.integrate(self.f)
        
    def set_differentiation_method(self, method):
        self.dx_method = method
        
    def set_differentiation_sharpness(self, h):
        self.h = h
        
    def set_integration_method(self, method):
        self.int_method = method
        
    def plot(self):
        f, a, b, resolution = self.f, self.a, self.b, self.resolution
        x = linspace(a, b, resolution)
        y = f(x)
        plt.figure()
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        
    def plot_derivative(self):
        a, b, resolution = self.a, self.b, self.resolution
        df_compute = self.dx_method(self.f)
        x = linspace(a,b, resolution)
        y = df_compute(x)
        plt.figure()
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel("df(x)")
        
if __name__ == '__main__':
    f = lambda x : x**2*exp(-0.2*x)*sin(2*pi*x)
    print "Let f(x) = x^2 * exp(-0.2x) * sin(2pi*x)"
    c = CalculusCalculator(f, 0, 6, resolution=700)
    c.plot()
    c.plot_derivative()
    c.extreme_points()
    print "Integral over [0,6] using Trapezoidal method is", c.integral()
    print "Derivative at 2.51 using Central2 method is", c.df(2.51)
    c.set_differentiation_method(Central4)
    print "Derivative at 2.51 using Central4 method is", c.df(2.51)
    c.set_integration_method(Simpson)
    print "Integral over [0,6] using Simpson method is", c.integral()