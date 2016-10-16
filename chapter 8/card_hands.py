"""
Exercise 8.7: Compute the probability of hands of cards
Author: Weiyun Lu
"""

from Deck import *
from cards import *

def simulate_deals(N):
    twopairs = 0
    flushes = 0
    quads = 0
    for i in range(N):
        deck = Deck()
        hand = deck.hand(5)
        if same_rank(hand, 2) == 2:
            twopairs += 1
        if 5 in same_suit(hand).values():
            flushes += 1
        if same_rank(hand, 4) == 1:
            quads +=1
    twopairs_prob = twopairs / float(N)
    flushes_prob = flushes / float(N)
    quads_prob = quads / float(N)
    return twopairs_prob, flushes_prob, quads_prob

N = eval(raw_input('We calculate probability of getting two pair, a flush, and a four-of-a-kind in a \
hand of five cards by Monte Carlo simulation.  Enter how many times to run the experiment: '))

twopairs_prob, flush_prob, quad_prob = simulate_deals(N)

print('The observed probabilities are %g for two pair, %g for a flush, and %g for four-of-a-kind.')\
    %(twopairs_prob, flush_prob, quad_prob)