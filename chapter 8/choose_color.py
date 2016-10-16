"""
Exercise 8.4: Draw balls from a hat
Author: Weiyun Lu
"""

import random

colors = ['red', 'blue', 'yellow', 'purple']

def hat_reset():
    hat = []
    for color in colors:
        for i in range(10):
            hat.append(color)
    random.shuffle(hat)
    return hat
    
def trial_hat(n):
    successes = 0
    for i in range(n):
        hat = hat_reset()
        balls = []
        for j in range(10):
            ball = hat.pop(0)
            balls.append(ball)
        if balls.count('blue') == 2 and balls.count('purple') == 2:
            successes += 1
    return successes/float(n)
    
print("A hat has 10 red, blue, yellow, and purple balls.  If we take 10 balls randomly, what is the \
probability that we have exactly two blue balls and exactly two purple balls?  Let's test empirically...")

n = eval(raw_input('Enter how many times you would like to run the experiment: '))
print("The observed probability of success is %g." %(trial_hat(n)))