"""
Exercise 8.13: Investigate the winning chances of some games
Author: Weiyun Lu
"""

import random
from math import sqrt

colors = ['red', 'yellow', 'green', 'brown']
nums = [5, 5, 3, 7]
hat = []

def hat_reset():
    for i in range(4):
        for j in range(nums[i]):
            hat.append(colors[i])
    random.shuffle(hat)

def draw_balls(n):
    hat_reset()
    drawn = []
    for i in range(n):
        ball = hat.pop(0)
        drawn.append(ball)
    return drawn
    
def ThreeRed(n):
    drawn = draw_balls(n)
    if drawn.count('red') == 3:
        return 60 - 2*n
    else:
        return -2*n

def ThreePlusBrown(n):
    drawn = draw_balls(n)
    if drawn.count('brown') >= 3:
        return 7 + 5 * sqrt(n) - 2*n
    else:
        return -2*n
        
def OneYellowOneBrown(n):
    drawn = draw_balls(n)
    if drawn.count('yellow') == 1 and drawn.count('brown') == 1:
        return n**3 - 26 - 2*n
    else:
        return -2*n

def Rainbow(n):
    drawn = draw_balls(n)
    if drawn.count('red') >= 1 and drawn.count('yellow') >= 1 and drawn.count('green') >= 1 and\
     drawn.count('brown') >= 1:
        return 23 - 2*n
    else:
        return -2*n
        
if __name__ == '__main__':
    print '-' * 110
    N = 250
    print '%20s %20s %20s %20s %20s' %('Game type', 'ThreeRed', 'ThreePlusBrown', 'OneYellowOneBrown',\
     'Rainbow')
    print '-' * 110
    for n in range(4, 11):
        winrates = []
        EVs = []
        for game in [ThreeRed, ThreePlusBrown, OneYellowOneBrown, Rainbow]:
            wins = 0
            net_profit = 0
            for k in range(N):
                this_round_profit = game(n)
                net_profit += this_round_profit
                if this_round_profit > 0:
                    wins += 1
            winrate = wins/float(N)
            EV = net_profit/float(N)
            winrates.append(winrate)
            EVs.append(EV)
        print '%10s %10s %20.2f %20.2f %20.2f %20.2f' %('n='+str(n), 'Winrate', winrates[0],\
         winrates[1], winrates[2], winrates[3])
        print '%10s %10s %20.2f %20.2f %20.2f %20.2f' %('', 'EV', EVs[0], EVs[1], EVs[2], EVs[3])
        print '-' * 110