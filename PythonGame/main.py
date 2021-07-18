import os
import time

from Player import *
from ComputerPlayer import *


class Game:
    def __init__(self):
        # Initialise the deck
        self.deck = list(range(1,14)*4)

        # Initialise the players
        self.players = [Player(self.deck),Computer(self.deck)]


    def checkGameOver(self): 
            return self.deck and self.players[0].hand and self.players[1].hand
    

    def play(self):
        # Shuffle the cards
        print 'Shuffling...'
        random.shuffle(self.deck)
        time.sleep(2)

        # Deal the cards
        print 'Dealing...'
        for i in xrange(7): # Deal the initial hand
            time.sleep(0.5)
            self.players[0].draw()
            time.sleep(0.5)
            self.players[1].draw()
        
        # Flip a coin for the starting player
        print '\nFlipping a coin...'
        time.sleep(1)
        startingPlayer = random.randint(0,1)
        print '%s is starting' % (self.players[startingPlayer].name)
        turn = 0

        raw_input("Press Enter to continue...")

        # Loop turns till the game is over
        while self.checkGameOver():
            whoseTurn = (turn + startingPlayer) % 2
            otherPlayer = (turn + 1 + startingPlayer) % 2
            print '\n** %ss Turn (%s:%d %s:%d) %d cards remaining in the deck. **' % (self.players[whoseTurn].name, self.players[0].name, self.players[0].score, self.players[1].name, self.players[1].score, len(self.deck))
            
            # Loop till the player doesn't get the card they wanted
            while True: 
                cardFished = self.players[whoseTurn].getMove()
                result = self.players[otherPlayer].fishFor(cardFished)
                if not result: # Draw and end turn if we didn't get the card
                    print '\n%s didn\'t have any %ss' % (self.players[otherPlayer].name, cardFished)
                    drawn = self.players[whoseTurn].draw()
                    if drawn == cardFished:
                        print '\n%s drew the %s they were after!' % (self.players[whoseTurn].name, drawn)
                    else:
                        break
                print '\n%s got %d more %s.' % (self.players[whoseTurn].name,result, cardFished)
                self.players[whoseTurn].receiveCard(cardFished,result)
                if not self.checkGameOver(): break # Not gameOver means there are still cards in hands and deck
            turn+=1
            
            # Give the user time to read, then clear the screen
            self.delayedCLS(3)
        
        # Display the final score
        print '\nScores: \n%s: %d\n%s: %d\n' % (self.players[0].name,self.players[0].score,
                                          self.players[1].name,self.players[1].score)        
        # Display the final outcome
        if self.players[0].score>self.players[1].score:
            print self.players[0].name,'won!'
        elif self.players[0].score==self.players[1].score:
            print 'Draw!'
        else:
            print self.players[1].name,'won!'
    

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
game.play()