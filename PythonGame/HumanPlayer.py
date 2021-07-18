from Player import *

class Human(Player):
    def __init__(self, name, deck):
        Player.__init__(self, name, deck)

    def chooseCard(self):
        # Get the user to choose a card to fish for
        choice  = -1
        while (choice < 1 or choice > 13 or self.isInHand(choice) == False):
            if (choice != -1):
                print 'Sorry, that input was invalid. Please enter a number between 1 and 13 equal to a card in your hand. (This will be the card you ask the opponent for)'
            choice = int(input('What card would you like to fish for?'))
        
        return choice