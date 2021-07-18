import random
import csv
from collections import defaultdict

from Player import *

class Computer(Player):
    def __init__(self,deck):
        self.name = 'Computer'
        self.hand = defaultdict(int)
        self.books = []
        self.deck = deck
        self.opponentHas = set()
        self.guesses = defaultdict(int)
        self.score = 0
 
    def draw(self):
        cardDrawn = self.deck.pop()
        self.hand[cardDrawn] += 1
        print '%s drew a card.' % (self.name)
        self.checkForBooks()
        self.sortHand()
        return cardDrawn

    ##AI: guesses cards that knows you have, then tries cards he has at random.
    ##Improvements: remember if the card was rejected before, guess probabilities
    def getMove(self):
        print '%s\'s hand: %s' % (self.name,self.displayHand())
        candidates = list(self.opponentHas & set(self.hand.keys()))
        if not candidates:
            candidates = self.hand.keys()
        move = random.choice(candidates)
        print '%s fishes for %s.' % (self.name,move)
        self.guesses[move] += 1
        return move
 
    # Same as for humans players, but adds the card fished for to opponentHas list.
    def fishFor(self, card): 
        self.opponentHas.add(card)
        # If card in hand, returns count and removes the card from hand
        if card in self.hand: 
            val = self.hand.pop(card)
            self.emptyCheck()
            return val
        else:
            return False
 
    def receiveCard(self, card, amount):
        self.hand[card] += amount
        self.opponentHas.discard(card)
        self.checkForBooks()
        self.sortHand()