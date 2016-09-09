"""
Author: Weiyun Lu
Exercise 7.33: Find local and global extrema of a function (discrete approximation)
"""

import numpy as np

class MinMax:
    def __init__(self, f, a, b, n):
        self.f = f
        self.a = a
        self.b = b
        self.n = n
        self.X = np.linspace(a,b,n+1)
        self._find_extrema()
        
    def _find_extrema(self):
        f = self.f
        n = self.n
        X = self.X
        self.Pmin, self.Pmax, self.Fmin, self.Fmax = [], [], [], []
        if X[0] > X[1]:
            self.Pmax.append(X[0])
        else:
            self.Pmin.append(X[0])
        for i in range(1, n):
            if f(X[i-1]) > f(X[i]) < f(X[i+1]):
                self.Pmin.append(X[i])
            if f(X[i-1]) < f(X[i]) > f(X[i+1]):
                self.Pmax.append(X[i])
        if X[-1] > X[-2]:
            self.Pmax.append(X[-1])
        else:
            self.pmin.append(X[-1])
        f = np.vectorize(f)
        self.Fmin = f(self.Pmin)
        self.Fmax = f(self.Pmax)
    
    def get_all_minima(self):
        return zip(self.Pmin, self.Fmin)
        
    def get_all_maxima(self):
        return zip(self.Pmax, self. Fmax)
    
    def get_global_maximum(self):
        localmaxes = self.get_all_maxima()
        gmax = (localmaxes[0])
        for i in range(len(localmaxes)):
            if localmaxes[i][1] > gmax[1]:
                gmax = localmaxes[i]
        return gmax
        
    def get_global_minimum(self):
        localmins = self.get_all_minima()
        gmin = (localmins[0])
        for i in range(len(localmins)):
            if localmins[i][1] < gmin[1]:
                gmin = localmins[i]
        return gmin

    def __str__(self):
        all_minima_list = ''
        all_maxima_list = ''
        localmins = self.get_all_minima()
        localmaxes = self.get_all_maxima()
        for i in range(len(localmins)):
            all_minima_list += '%.4f, ' %(localmins[i][0])
        for i in range(len(localmaxes)):
            all_maxima_list += '%.4f, ' %(localmaxes[i][0])
        all_minima_list = all_minima_list[:-2]
        all_maxima_list = all_maxima_list[:-2]
        return 'All minima: ' + all_minima_list + '\nAll maxima: ' +\
            all_maxima_list + '\nGlobal minimum: ' + '%.4f' %self.get_global_minimum()[0]\
            + '\nGlobal maximum: ' + '%.4f' %self.get_global_maximum()[0]
            
if __name__ == '__main__':
    def f(x):
        return (x**2)*np.exp(-0.2*x)*np.sin(2*np.pi*x)
    print 'Define f(x) = x^2 * exp(-0.2x) * sin(2pi*x) on [0,4]'
    m = MinMax(f, 0, 4, 5001)
    print m