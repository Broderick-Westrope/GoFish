import os
import time

from Deck import *
from HumanPlayer import *
from ComputerPlayer import *


class Game:
    def __init__(self):
        # Initialise the deck
        self.deck = ('2 3 4 5 6 7 8 9 10 J Q K A '*4).split(' ')
        self.deck.remove('')

        # Initialise the players
        self.players = [Human(self.deck),Computer(self.deck)] #makes counting turns easier


    # checks if hands/decks are empty using the any method
    def checkGameOver(self): 
            return self.deck or self.player[0].hand or self.player[1].hand
    
    def play(self):
        random.shuffle(self.deck)
        for i in xrange(7): # Deal the initial hand
            self.players[0].Draw()
            self.players[1].Draw()
        startingPlayer = random.randint(0,1)
        turn = 0

        while self.checkGameOver():
            print '\n** %ss Turn (%s:%d %s:%d) %d cards remaining in the deck. **' % (self.players[whoseTurn], self.players[0].name, self.players[0].score, self.players[1].name, self.players[1].score, len(self.deck))
            whoseTurn = (turn+startingPlayer)%2
            otherPlayer = (turn+1+startingPlayer)%2
            while True: # Loop till the player doesnt get the card they wanted
                cardFished = self.players[whoseTurn].getMove()
                result = self.players[otherPlayer].fishFor(cardFished)
                if not result: # Draw and end turn if we didn't get the card
                    drawn = self.players[whoseTurn].draw()
                    if drawn == cardFished:
                        # TODO Print that they drew the card they were after
                    else:
                        break
                print '%s got %d more %s.' % (self.player[whoseTurn].name,result, cardFished)
                self.player[whoseTurn].gotCard(cardFished,result)
                if not self.endOfPlayCheck(): break
            turn+=1
            # Give the user time to read then clear the screen
            self.delayedCLS(3)
        print '\nScores: \n%s: %d\n%s: %d\n' % (self.player[0].name,self.player[0].score,
                                          self.player[1].name,self.player[1].score)
        if self.player[0].score>self.player[1].score:
            print self.player[0].name,'won!'
        elif self.player[0].score==self.player[1].score:
            print 'Draw!'
        else:
            print self.player[1].name,'won!'
        #TODO: Add the ability to start a new game
    
    def restockHands(self):
        if len(self.player.hand)<=0:
            print '\nYour hand was empty so you drew a card...'
            self.player.draw(self.deck)
        if len(self.computer.hand)<=0:
            print '\nYour opponents hand was empty so they drew a card...'
            self.computer.draw(self.deck)
        
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