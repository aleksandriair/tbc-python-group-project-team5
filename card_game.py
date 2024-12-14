from random import shuffle

class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
    def __str__(self):
        return f"{self.suit} - {self.value}"

class Deck:
    def __init__(self):
        self.cards = []
    def generate_deck(self):
        suits = ["S", "H", "D", "C"]
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K']
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit,value))
    def shuffle(self):
         shuffle(self.cards)
    def deal_cards(self,players):
        for player in players:
            for _ in range(5):
               player.hand.append(self.cards.pop())

class Player:
    def __init__ (self,name):
        self.name = name
        self.hand = []
    
    
player1 = Player("Player 1")
player2 = Player("Player 2")
player3 = Player("Player 3")

deck = Deck()
deck.generate_deck()
deck.shuffle()
deck.deal_cards([player1, player2, player3])

for player in [player1, player2, player3]:
    print(f"{player.name}'s hand: {[str(card) for card in player.hand]}")