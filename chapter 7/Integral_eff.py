"""
Exercise 7.22: Speed up repeated integral calculations
Author: Weiyun Lu
"""

def trapezoidal(f, a, x, n):
    h = (x-a) / float(n)
    I = 0.5 * f(a)
    for i in range(1, n):
        I += f(a + i*h)
    I += 0.5 * f(x)
    I *= h
    return I
    
class Integral_array:
    def __init__(self, f, a, n=100):
        self.f, self.a, self.n = f, a, n
    
    def __call__(self, x):  #We assume x is an input array of increasing values.
        f, a, n = self.f, self.a, self.n
        integrated = []     #Initialize empty array of answers.
        int_fx = trapezoidal(f, a, x[0], n)
        integrated.append(int_fx)
        for i in range(1, len(x)):
            int_fx = int_fx + trapezoidal(f, x[i-1], x[i], n)
            integrated.append(int_fx)
        return integrated
        
    def plot(self, x):
        y = self.__call__(x)
        import matplotlib.pyplot as plt
        plt.plot(x,y)
        plt.title('Trapezoidal approximation of the integral')
        
if __name__ == '__main__':
    f = lambda x : x**2 + 2*x + 1
    X = [1, 2, 4, 12]
    f_int = Integral_array(f, a=0)
    print 'Define f(x) = x^2 + 2x + 1.  Take X = [1,2,4,12].'
    print 'Using trapezoidal integration yields', f_int(X)
    f_int.plot(X)