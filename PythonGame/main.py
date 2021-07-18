import os
import time

from Deck import *
from HumanPlayer import *
from ComputerPlayer import *


class Game:
    def __init__(self):
        # Initialise the deck
        self.deck = Deck()
        self.deck.shuffle()

        # Initialise the players
        self.player = Human('Player', self.deck)
        self.computer = Computer('Computer', self.deck)

        # Begin the game
        self.turn = 'P1' if (random.randint(0,1) == 0) else 'P2'
        self.currentPlayer = self.player if (self.turn == 'P1') else self.computer
        self.checkForBooks(self.currentPlayer)
        self.gameover = False
        self.beginGame()

    
    def checkGameOver(self):
        return True if (len(self.deck.cards) <= 0) else False
    

    def beginGame(self):
        while self.checkGameOver()==False:
            # Print scores, hand, and turn
            self.printScores()
            self.displayHand()
            print '\nYour turn' if (self.turn=='P1') else '\nOpponents turn'

            # Choose and fish for card
            _input = self.currentPlayer.chooseCard()
            results = self.player.getFished(_input) if (self.turn=='P2') else self.computer.getFished(_input)

            # Add the cards to the players hand
            for i in results:
                self.currentPlayer.addCard(i)

            # Print outcome
            print ('\nThe opponent didn\'t have the card you wanted. Go Fish!') if (len(results)==0) else ('You got %d card/s from the opponent' % (len(results)))

            # Go again if we got what we fished for, otherwise enter the if statement
            goAgain = False if (len(results) == 0) else True
            if goAgain == False:
                # Draw a card and check if it happens to be what we were after, if so have another go
                drawn = self.currentPlayer.draw(self.deck)
                if(drawn.value == _input):
                    goAgain = True
                    print '\nYou drew a %d like you were looking for so you get another turn!' % (drawn.value)
                else:
                    print '\nYou drew a %d.' % (drawn.value)
            
            # Check for books
            self.checkForBooks(self.currentPlayer)

            # Restock Hands
            self.restockHands()

            # Switch turns if we need to
            if goAgain == False:
                self.turn = 'P1' if (self.turn == 'P2') else 'P2'
                self.currentPlayer = self.player if (self.turn == 'P1') else self.computer
            
            # Give the user time to read then clear the screen
            self.delayedCLS(3)

        # Print the results of the game
        print '\nGame Over. You had %d books and your opponent has %d.' % (self.player.books, self.computer.books)
        print 'You won!!' if (self.player.books > self.computer.books) else 'You Lost :('
        #TODO: Add the ability to start a new game


    def displayHand(self):
        print '\n**Your hand**'
        self.player.showHand()

        # print '\nOpponents hand:'
        # self.computer.showHand()
    
    def restockHands(self):
        if len(self.player.hand)<=0:
            print '\nYour hand was empty so you drew a card...'
            self.player.draw(self.deck)
        if len(self.computer.hand)<=0:
            print '\nYour opponents hand was empty so they drew a card...'
            self.computer.draw(self.deck)
    
    def checkForBooks(self, player):
        newBooks = player.checkForBooks()
        if len(newBooks) > 0:
            print 'Got another point by getting all four %ds' % (newBooks[0])
    
    def printScores(self):
        print '\n**Score**'
        print 'You: {}    Computer: {}'.format(self.player.books, self.computer.books)
    
    def delayedCLS(self, length):    
        while length:
            mins, secs = divmod(length, 60)
            timer = 'Continuing in {}...'.format(secs)
            print timer + '\r',
            time.sleep(1)
            length -= 1

        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')


game = Game()