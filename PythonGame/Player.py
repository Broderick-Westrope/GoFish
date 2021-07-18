from collections import defaultdict
import sys

class Player:
    def __init__(self, deck):
        self.hand = defaultdict(int)
        self.books = []
        self.deck = deck
        self.score = 0
        self.name = raw_input('Enter your name: ')
 
    def draw(self):
        cardDrawn = self.deck.pop()
        self.hand[cardDrawn] += 1
        print '%s drew a %s.' % (self.name,cardDrawn)
        self.checkForBooks()
        self.sortHand()
        return cardDrawn
 
    def checkForBooks(self):
        for key,val in self.hand.items():
            if val == 4:
                self.books.append(key)
                print '%s completed the book of %s\'s.' % (self.name,key)
                self.score += 1
                del self.hand[key]
        self.emptyCheck()
 
    def emptyCheck(self):
        if len(self.deck)!=0 and len(self.hand)==0:
            self.Draw()

    def displayHand(self):
        return ' '.join(str(key) for key,val in self.hand.iteritems() for i in range(val))
 
    def getMove(self):
        print '%s\'s hand: %s' % (self.name,self.displayHand())
        chooseCard = raw_input('What card do you want to fish for? ').strip()
        if chooseCard == 'quit':
            sys.exit(0)
        chooseCard = int(chooseCard)
        if chooseCard not in self.hand:
            print 'You don\'t have that card. Try again! (or enter quit to exit)'
            chooseCard = self.getMove()
        return chooseCard
 
    def fishFor(self, card):
        if card in self.hand:
            val = self.hand.pop(card)
            self.emptyCheck()
            return val
        else:
            return False

    def receiveCard(self, card, amount):
        self.hand[card] += amount
        self.checkForBooks()
        self.sortHand()

    # ========SORTING=========================================================

    def sortHand(self):
        self.__quickSort(0,len(self.hand)-1)

    def __quickSort(self, low, high):
        if len(self.hand) == 1:
                return self.hand
        if low < high:
        
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.__partition(low, high)
    
            # Separately sort elements before
            # partition and after partition
            self.__quickSort(low, pi-1)
            self.__quickSort(pi+1, high)

    def __partition(self, low, high):
        i = (low-1)         # index of smaller element
        pivot = self.hand[high]     # pivot
    
        for j in range(low, high):
        
            # If current element is smaller than or
            # equal to pivot
            if self.hand[j] <= pivot:
            
                # increment index of smaller element
                i = i+1
                self.hand[i], self.hand[j] = self.hand[j], self.hand[i]
    
        self.hand[i+1], self.hand[high] = self.hand[high], self.hand[i+1]
        return (i+1)