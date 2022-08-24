"""Template for Homework 8 in CSE 4256 at The Ohio State University.

Date: Mar 27, 2022
Author: Sudi Yussuf

Due date: Mar 27, 2022"""

from collections import namedtuple, deque, Counter
from random import random
from typing import Any, Sequence
def uniform(a: float, b: float) -> float:
    """Returns a uniformly-distributed real number in the interval [a, b)."""
    return a + ((b-a) * random())
def randrange(start: int, stop: int) -> int:
    """Returns a uniformly distributed integer in the interval [start, stop)."""
    return int(start + ((stop-start) * random()))
def choice(seq: Sequence) -> Any:
    """Returns a randomly-chosen element of `seq`."""
    l = randrange(0,len(seq))
    return(seq[l])
  

Card = None
def std_card_deck() -> deque:
    """Returns a deque containing 52 Cards, the standard 52 playing cards."""
    suits = ["CLUBS", "SPADES", "HEARTS", "DIAMONDS"]
    values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
    Card = namedtuple("Card", ["suit", "value"])
    cards = deque()
    for s in suits:
      for v in values:
        cards.append(Card(s, v))

    return(cards)
  
def riffle_shuffle(deck: deque) -> None:
    """Simulates a 'riffle shuffle' of a deck of cards."""
    d1 = deque()
    d2 = deque()
    i = 0
    while deck:
      d1.append(deck.pop())
      d2.append(deck.pop())
      i+=1
    while d2 and d1:
      r = random()
      if r < 0.5:
        deck.append(d1.pop())
      if r > 0.5:
        deck.append(d2.pop())
    if d2:
      while d2:
        deck.append(d2.pop())
    else:
      while d1:
        deck.append(d1.pop())
    return(deck)
 
def mix_deck(deck: deque) -> None:
    """Puts deck in a random order."""
    i = 0
    while i < (randrange(10,52)):
      deck = riffle_shuffle(deck)
      i += 1
    return(deck)

def deal(deck: deque, n_players: int) -> list:
    """Deals the cards n_players ways."""
    players = [[] for i in range(n_players)]
    while deck:
      i = 0
      while i < n_players:
        if deck:
          d = deck.pop()
          players[i].append(d)
        i= i+1
    return(players)

        
    
def letter_freq(s: str) -> Counter:
    """Counts the number of times each letter appears in `s`."""
    counts=Counter(s) 
    return counts


def popular_letter(s: str) -> str:
    """Returns the letter in `s` that appears most often."""
    counts=Counter(s) 
    return counts.most_common(1)[0][0]
