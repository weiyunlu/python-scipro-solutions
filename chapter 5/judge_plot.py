"""
Exercise 5.27: Judge a plot
Author: Weiyun Lu
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2,20)
y = np.cos(18 * np.pi * x)
X = np.linspace(0,2,1000)
Y = np.cos(18 * np.pi * X)

plt.plot(x,y)
plt.plot(X,Y)
plt.title('Plotting f(x)=cos(18*pi*x)')
plt.legend(['20 points', '2000 points'])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()