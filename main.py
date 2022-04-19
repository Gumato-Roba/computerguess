
from email.parser import FeedParser
from itertools import Predicate
from random import randint


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
          guess = guess.randint(low,high)
        guess= low
        feedback= input(f'is {guess} too high(H),low(L) or correct(c)?? ').lower()
        if feedback == 'h':
            high= guess -1 
        elif feedback == 'l':
            low= guess + 1
    print(f'yay! The computer guessed your number, {guess},correctly!')

    computer_guess(10)
