import card
import random


class Deck:
    def __init__(self):

        suits = ["Hearts", "Clubs", "Spades", "Diamonds"]
        self.deck = []
        for suit in suits:
            for rank in range(1, 14):
                new_card = card.Card(rank, suit)
                self.deck.append(new_card)

    def shuffle(self):
        random.shuffle(self.deck)

    def dealacard(self):
        range_of_pick = len(self.deck)
        updated_card = self.deck.pop(0)
        return updated_card
