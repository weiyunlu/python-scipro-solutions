"""
Author: Weiyun Lu
Exercise 7.21: Make a class for piecewise constant functions
"""

class PiecewiseConstant:
    def __init__(self, data, endpoint):
        self.data = data
        self.endpoint = endpoint
        
    def value(self, x):
        data = self.data
        endpoint = self.endpoint
        value = 0
        for i in range(len(data)-1):
            if data[i][1] <= x <= data[i+1][1]: #if x in [x_i, x_{i+1}], return v_i
                value = data[i][0]
        if data[-1][1] <= x <= endpoint: #if x in [x_n, {x_n+1}], return v_n
            value = data[-1][0]
        return value
        
    def __call__(self, x):
        if isinstance(x, (int,float)):
            return self.value(x)
        elif isinstance(x, (np.ndarray, list, tuple)):
            value_set = []
            for j in range(len(x)):
                y = self.value(x[j])
                value_set.append(y)
            return value_set
            
    def plot(self):
        from matplotlib.pyplot import plot, axis          
        X = []; Y = []
        data = self.data
        endpoint = self.endpoint
        for i in range(len(data)):
            x = data[i][1]
            if i+1 < (len(data)):
                x_next = data[i+1][1]
            else:
                x_next = endpoint
            X.append(x)
            X.append(x_next)
            Y.append(self.__call__(x))
            Y.append(self.__call__(x))
        X.append(endpoint)
        Y.append(self.__call__(endpoint))
        plot(X, Y)
        axis([X[0], X[-1], min(Y)-0.05, max(Y)+0.05])
            

if __name__ == '__main__':
    import numpy as np
    print 'Test run:'
    print 'f = PiecewiseConstant([(0.4, 1), (0.2, 1.5), (0.1, 3)], endpoint=4)'
    f = PiecewiseConstant([(0.4, 1), (0.2, 1.5), (0.1, 3)], endpoint=4)
    print 'print f(1.5), f(1.75), f(4)'
    print '>', f(1.5), f(1.75), f(4)
    print 'x = np.linspace(0,4,21) \nprint f(x)'
    x = np.linspace(0,4,21)
    print '>', f(x)
    print 'f.plot()'
    f.plot()