"""
Exercise 6.8: Make a nested dictionary from a file
Author: Weiyun Lu
"""

import matplotlib.pyplot as plt
import numpy as np

mu_data = {} #initialize empty dictionary
with open('viscosity_of_gases.dat', 'r') as infile:
    for line in infile:
        if line[0]=='#' or line.isspace(): #skip comment and whitespace lines
            continue
        else: #otherwise, process
            words = line.split()
            mu_0 = float(words[-1].strip())
            T_0 = float(words[-2].strip())
            C = float(words[-3].strip())
            name = ' '.join(words[:-3]).strip()
            mu_data[name] = ({'mu_0': mu_0, 'T_0': T_0, 'C': C})

def mu(T, gas, mu_data):
    T_z = mu_data[gas]['T_0']
    mu_z = mu_data[gas]['mu_0']
    C_z = mu_data[gas]['C']
    return mu_z * ((float(T_z)-T)/(T + C_z)) * (float(T)/T_z) ** 1.5

T = np.linspace(223,373,151)
mu = np.vectorize(mu)
mu_air = mu(T, 'air', mu_data)
mu_carbo = mu(T, 'carbon dioxide', mu_data)
mu_hydro = mu(T, 'hydrogen', mu_data)

def plotme(x,y):
    plt.plot(x,y)
    plt.xlabel('Temperature (Kelvin)')
    plt.ylabel('Viscocity (Mu)')

plt.figure()
plotme(T, mu_air)
plt.title('Viscocity of Air')

plt.figure()
plotme(T,mu_carbo)
plt.title('Viscocity of Carbon Dioxide')

plt.figure()
plotme(T,mu_hydro)
plt.title('Viscocity of Hydrogen')