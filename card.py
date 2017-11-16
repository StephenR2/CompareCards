class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getsuit(self):
        return self.suit

    def getrank(self):
        return self.rank

    def __str__(self):
        return str(self.rank) + " Of " + self.suit
