class Player:
    def __init__(self, name, deck):
        self.name = name
        self.books = 0
        self.hand = []
        self.newHand(7, deck)
        self.quickSort(0,len(self.hand)-1)
    
    def newHand(self, size, deck):
        for i in range(0,size):
            self.draw(deck)

    def draw(self, deck):
        card = deck.drawCard()
        self.hand.append(card)
        self.quickSort(0,len(self.hand)-1)
        return card

    def addCard(self, card):
        self.hand.append(card)
        self.quickSort(0,len(self.hand)-1)
    
    def showHand(self):
        for c in self.hand:
            c.show()
    
    def getFished(self, value):
        results = []
        for c in self.hand:
            if c.value == value:
                results.append(c)
        for i in results:
            self.hand.remove(i)
        return results

    def isInHand(self, value):
        for c in self.hand:
            if c.value==value:
                return True
        return False
    

    def checkForBooks(self):
        numerics = []
        for c in self.hand:
            numerics.append(c.value)
        
        blacklist = []
        for c in numerics:
            if numerics.count(c) >= 4:
                blacklist.append(c)
                self.books += 1
                for i in range(numerics.count(c)):
                    numerics.remove(c)

        for t in blacklist:
            for c in self.hand:
                if t == c.value:
                    self.hand.remove(c)

        return blacklist
    

    def partition(self, low, high):
        i = (low-1)         # index of smaller element
        pivot = self.hand[high].value     # pivot
    
        for j in range(low, high):
        
            # If current element is smaller than or
            # equal to pivot
            if self.hand[j].value <= pivot:
            
                # increment index of smaller element
                i = i+1
                self.hand[i], self.hand[j] = self.hand[j], self.hand[i]
    
        self.hand[i+1], self.hand[high] = self.hand[high], self.hand[i+1]
        return (i+1)


    def quickSort(self, low, high):
        if len(self.hand) == 1:
                return self.hand
        if low < high:
        
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.partition(low, high)
    
            # Separately sort elements before
            # partition and after partition
            self.quickSort(low, pi-1)
            self.quickSort(pi+1, high)