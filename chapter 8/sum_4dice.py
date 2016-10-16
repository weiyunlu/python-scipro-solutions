"""
Exercise 8.8: Decide if a dice game is fair
Author: Weiyun Lu
"""

import random
import sys

def win_one_round():
    dicerolls = []
    for i in range(4):
        dice = random.randint(1,6)
        dicerolls.append(dice)
    dicetotal = sum(dicerolls)
    if dicetotal < 9:
        return True
    else:
        return False
        
r = float(sys.argv[1])
N = int(sys.argv[2])

net_gain = 0

for i in range(N):
    win_this_round = win_one_round()
    if win_this_round:
        net_gain += r
    else:
        net_gain -= 1
        
EV = net_gain / float(N)

print("The game is rolling four dice - player wins if total is strictly less than 9.  With %d trials, \
$1.00 lost if the player loses and $%.2f won if the player wins, the player's net gain is $%.2f, with an \
expected value per game of $%.2f.") %(N, r, net_gain, EV)