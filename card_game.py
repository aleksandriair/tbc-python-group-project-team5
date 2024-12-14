from random import shuffle
from collections import Counter

class Card:
    def __init__(self, suit, value):
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

    def get_points(self, game_rules):
        return game_rules.calculate_points(self.hand)

    def get_suits_count(self):
        return Counter(card.suit for card in self.hand)

    def get_value_count(self):
        return Counter(card.value for card in self.hand)


class GameRules:
    def __init__(self):
        self.game_over = False
        self.winner = None

    def calculate_points(self, hand):
        points = 0
        for card in hand:
            if isinstance(card.value, int):
                points += card.value
            elif card.value == "A":
                points += 20
            elif card.value == "K":
                points += 13
            elif card.value == "Q":
                points += 12
            elif card.value == "J":
                points += 11
        return points

    def determine_winner(self, player1, player2, player3):
        players = [player1, player2, player3]
        player_points = [(player, player.get_points(self)) for player in players]

        player_points.sort(key=lambda x: x[1], reverse=True)

        if player_points[0][1] > player_points[1][1]:
            self.winner = player_points[0][0]
            return

        tied_players = [p for p, points in player_points if points == player_points[0][1]]

        max_same_suits = []
        max_suit_count = 0
        for player in tied_players:
            suit_counts = player.get_suits_count()
            player_max_suits = max(suit_counts.values())
            if player_max_suits > max_suit_count:
                max_same_suits = [player]
                max_suit_count = player_max_suits
            elif player_max_suits == max_suit_count:
                max_same_suits.append(player)

        if len(max_same_suits) == 1:
            self.winner = max_same_suits[0]
            return

        max_same_values = []
        max_value_count = 0
        for player in max_same_suits:
            value_count = player.get_value_count()
            player_max_values = max(value_count.values())
            if player_max_values > max_value_count:
                max_same_values = [player]
                max_value_count = player_max_values
            elif player_max_values == max_value_count:
                max_same_values.append(player)

        if len(max_same_values) == 1:
            self.winner = max_same_values[0]
        else:
            self.winner = None


def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    player3 = Player("Player 3")

    deck = Deck()
    deck.generate_deck()
    deck.shuffle()
    deck.deal_cards([player1, player2, player3])

    game_rules = GameRules()

    for player in [player1, player2, player3]:
        points = player.get_points(game_rules)
        print(f"{player.name}'s hand: {[str(card) for card in player.hand]}")
        print(f"{player.name}'s points: {points}")

    game_rules.determine_winner(player1, player2, player3)
    if game_rules.winner:
        print(f"\nThe winner is {game_rules.winner.name}")
    else:
        print("\nIt's a tie!")


if __name__ == "__main__":
    main()