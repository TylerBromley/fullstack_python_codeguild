# Blackjack.py
from Deck import Card, Deck

class Hand:
    """ Represents a hand in blackjack """
    def __init__(self, card1, card2):
        self.cards = [card1, card2]
        face = {k:10 for k in 'JQK'}
        number = {k:k for k in range(2, 11)}
        self.points =  {'A': 1}
        self.points.update(number)
        self.points.update(face)

    def __repr__(self):
        return str(self.cards)

    def score(self):
        return sum([self.points[card.rank] for card in self.cards])
        
        # equivalent to comprehension above
        # total = 0
        # for card in self.cards:
        #     total += points[crd.rank]
        # return total

    def add(self, card):
        self.cards.append(card)

class Dealer(Hand):
    def __init__(self, card1, card2):
        super().__init__(card1, card2)

    def one_face_down(self):
        hidden = Card('Hidden', 'Hidden')
        return [hidden] + self.cards[1:]

    def visible_score(self):
        hidden = self.cards[0]
        return self.score() - self.points[hidden.rank]

class Game:
    def __init__(self, cut_index, num_players=1):
        self.deck = Deck()
        self.deck.shuffle()
        self.deck.cut(cut_index)

        # create player hands
        self.players = []
        for i in range(num_players):
            player = Hand(self.deck.draw(), self.deck.draw())
            self.players.append(player)

        # create dealer
        self.dealer = Dealer(self.deck.draw(), self.deck.draw())

    def play(self):
        print("-"*48)
        print("Dealer's hand")
        print(self.dealer.one_face_down())
        print("Dealer's score")
        print(self.dealer.visible_score())
        print("-"*48)
        # loop over all of the players
        for i, player in enumerate(self.players):
            print("-"*48)
            print(f"Player {i}'s turn")
            print(f"Score: {player.score()}")
            print("-"*48)
            print(player) # display player's hand
            # each turn the player gets the option to hit or stay
            while player.score() < 21:
                while True:
                    move = input("Hit or stay?: ").strip().lower()
                    if move in ['hit', 'h', 'stay', 's']:
                        break
                if move.startswith('h'):
                    player.add(self.deck.draw())
                    print(player)
                    print("-"*48)
                    print(f"Score: {player.score()}")
                    print("-"*48)
                else:
                    break
            if player.score() > 21:
                print('Player busted')
            elif player.score == 21:
                print('Blackjack!')

        # dealer's move
        print("-"*48)
        print("Dealer's turn")
        print("-"*48)
        print(self.dealer.one_face_down())
        while self.dealer.score() < 21:
            if self.dealer.score() < 17:
                print('Dealer hits!')
                self.dealer.add(self.deck.draw())
                print(self.dealer.one_face_down())
                dealer_score = self.dealer.score()
            elif self.dealer.score() < 21:
                print('Dealer stays!')
                break
            elif self.dealer.score() == 21:
                print("Blackjack for the dealer!")
                break
            else:
                print("Dealer busted!")
                break
            print(self.dealer)
            print(self.dealer.score())

        for i, player in enumerate(self.players):
            if (player.score() > 21) or player.score() <= self.dealer.score() <= 21:
                print(f"Player {i} loses!")
            elif (21 >= player.score() > self.dealer.score()) or self.dealer.score() > 21:
                print(f"Player {i} wins!")

blackjack = Game(1)
blackjack.play()


