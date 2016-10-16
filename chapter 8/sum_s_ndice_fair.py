"""
Exercise 8.9: Adjust a game to make it fair
Author: Weiyun Lu
"""

import random

def dice_trial(s, n):
    dicerolls = []
    for i in range(n):
        dice = random.randint(1,6)
        dicerolls.append(dice)
    dicetotal = sum(dicerolls)
    if dicetotal < s:
        return 1
    else:
        return 0

def dice_prob(s, n, N=1000000):
    wins = 0
    for i in range(N):
        this_round = dice_trial(s, n)
        wins += this_round
    return wins/float(N)
    
if __name__ == '__main__':
    dice_game_prob = dice_prob(9, 4)
    reward = 1 / float(dice_game_prob)
    print('The dice game from exercise 8.8 with player losing $1 on a loss and winning $10 on a win was\
 not fair.  The probability of winning is p = %g, and since the cost is 1, then the reward should be\
 r = 1/p = %g.') %(dice_game_prob, reward)