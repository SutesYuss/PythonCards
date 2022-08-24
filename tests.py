import unittest
import Homework8 as H
from collections import namedtuple, deque, Counter


class HW8(unittest.TestCase):
  def testUniform(self):
    m = H.uniform(1.0,9.2)
    self.assertTrue(m<=9.2)
    self.assertTrue(m>=1.0)
    
  def testRandRange(self):
    m = H.randrange(1,9)
    self.assertTrue(m<=9)
    self.assertTrue(m>=1)
    
  def testChoice(self):
    s = ["j","l","t"]
    m = H.choice(s)
    self.assertTrue(m in s)
    
  def testStd_card_deck(self):
    deck = H.std_card_deck()
    self.assertTrue(len(deck) == 52)
    
  def testRiffle_shuffle(self):
    deck = H.std_card_deck()
    deck1 = H.riffle_shuffle(deck)
    self.assertTrue(len(deck1) == len(deck))
    
  def testMix_deck(self):
    deck = H.std_card_deck()
    deck2 = H.mix_deck(deck)
    deck1 = H.riffle_shuffle(deck)
    self.assertTrue(len(deck1) == len(deck) == len(deck2))
    
  def testDeal(self):
    deck = H.std_card_deck()
    deck2 = H.mix_deck(deck)
    x = H.deal(deck2,20)
    self.assertTrue(len(x)==20)
    
  def testLetter_freq(self):
    x = H.letter_freq("Hello")
    self.assertTrue(x.most_common(1)[0][0]== "l")
    
  def testPopular_letter(self):
    x = H.popular_letter("Hello")
    self.assertTrue(x == "l")

unittest.main()