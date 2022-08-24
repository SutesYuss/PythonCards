"""Template for Homework 8 in CSE 4256 at The Ohio State University.

Date: Mar 27, 2022
Author: Sudi Yussuf

Due date: Mar 27, 2022"""

import Homework8 as H

#test letter_freq
print(H.letter_freq("Hello"))

#test popular_letter
print(H.popular_letter("Hello"))

#test deal by creating deck, shuffling, and then dealing to 20 people and checking the first persond hand
deck = H.std_card_deck()
deck = H.mix_deck(deck)
print(len(deck))
print(H.deal(deck, 20)[0])
