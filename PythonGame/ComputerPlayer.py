from Player import *
import random

class Computer(Player):
    def __init__(self, name, deck):
        Player.__init__(self, name, deck)
        self.opponentHas = []

    def chooseCard(self):
        candidates = list(self.opponentHas & self.hand.keys())
        if not candidates:
            candidates = random.choice(self.hand).value
        return random.choice(candidates)

