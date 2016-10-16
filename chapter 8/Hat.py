"""
Exercise 8.19: Make a class for drawing balls from a hat
Author: Weiyun Lu
"""

import random

class Hat:
    
    def __init__(self, **kwargs): #allows a variable number of keyword colors and numbers
        self.hat = []
        self.colordict = kwargs
        self.reset()
    
    def reset(self):
        self.hat = []
        for color in self.colordict.keys():
            self.hat += [color]*self.colordict[color]
        random.shuffle(self.hat)

    def draw(self, n):
        drawn = []
        for i in range(n):
            ball = self.hat.pop(0)
            drawn.append(ball)
        return drawn
        
if __name__ == '__main__':
    Myhat = Hat(blue = 6, brown = 8, green = 3)
    N = 100000
    successes = 0
    for i in range(N):
        Myhat.reset()
        drawn_balls = Myhat.draw(6)
        success = drawn_balls.count('blue') == 2 and drawn_balls.count('brown') == 2
        successes += success
    prob_myhat = successes / float(N)
    print('My hat has 6 blue balls, 8 brown balls, and 3 green balls.  I draw six balls - I win if I have'),
    print('2 brown and 2 blue balls.  Running %d trials, the chance of winning is around %g.')\
        %(N, prob_myhat)