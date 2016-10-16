"""
Exercise 8.33: Make classes for 2D random walk
Author: Weiyun Lu
"""

import random
import matplotlib.pyplot as plt

class Particle:
    
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.x_positions = [x]
        self.y_positions = [y]
        self.t = 0
        
    def move(self):
        direction = random.randint(1, 4)
        if direction == 1:
            self.x += 1
        elif direction == 2:
            self.y += 1
        elif direction == 3:
            self.x -= 1
        elif direction == 4:
            self.y -= 1
        self.x_positions.append(self.x)
        self.y_positions.append(self.y)
        self.t += 1
    
class Particles:
    
    def __init__(self, particles):
        self.particles = particles
        
    def move(self):
        for particle in self.particles:
            particle.move()
    
    def plot(self):
        plt.figure()
        x_values = [particle.x for particle in self.particles]
        y_values = [particle.y for particle in self.particles]
        plt.plot(x_values, y_values, 'bo')
        
    def moves(self, n):
        for i in range(n):
            self.move()
            self.plot()
            
if __name__ == '__main__':
    particle_initial = []
    for i in range(25):
        origin_particle = Particle(0, 0)
        particle_initial.append(origin_particle)
    my_particles = Particles(particle_initial)
    my_particles.moves(50)