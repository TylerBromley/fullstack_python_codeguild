# Deck.py
import random


class Card:
    """  Create a card as a suit and rank """
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"Card({self.rank}, {self.suit})"

    def __eq__(self, card):
        return self.rank == card.rank


class Deck:
    """ Create and manipulate a deck of 52 playing cards"""
    def __init__(self):
        ranks = ['A'] + list(range(2, 11)) + list('JQK')
        suits = ['clubs', 'diamonds', 'hearts', 'spades']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]

    def __repr__(self):
        return str(self.cards)

    def __getitem__(self, i):
        return self.cards[i]

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def cut(self, i):
        self.cards = self.cards[i:] + self.cards[:i] 

    def draw(self):
        return self.cards.pop()

# deck = Deck()
# deck.shuffle()
# print(deck)
# deck.cut(8)
# print(deck)
# card = deck.draw()
# print(card)


