from random import shuffle
from collections import Counter


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.suit}-{self.value}"


class Deck:
    def __init__(self):
        self.cards = []

    def generate_deck(self):
        suits = ["S", "H", "D", "C"]
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K']
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        shuffle(self.cards)

    def deal_cards(self, players):
        for player in players:
            player.hand.clear()
            for _ in range(5):
                player.hand.append(self.cards.pop())

    def replace_card(self, player, old_card_index):
        if 0 <= old_card_index < len(player.hand):
            old_card = player.hand.pop(old_card_index)
            self.cards.append(old_card)
            self.shuffle()
            new_card = self.cards.pop()
            player.hand.append(new_card)
        else:
            print(f"Invalid card index: {old_card_index}")


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def get_points(self, game_rules):
        return game_rules.calculate_points(self.hand)

    def get_suits_count(self):
        return Counter(card.suit for card in self.hand)

    def get_value_count(self):
        return Counter(card.value for card in self.hand)

    def replace_card(self, index, deck):
        deck.replace_card(self, index)

    def display_hand(self):
        return f"{self.name}'s hand: {[str(card) for card in self.hand]}"


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


class Game:
    def __init__(self, players):
        self.players = players
        self.deck = Deck()
        self.game_rules = GameRules()
        self.round_number = 1

    def display_all_hands(self):
        print("\nCurrent hands:")
        for player in self.players:
            print(player.display_hand())

    def get_valid_yes_no_input(self, player_name):
        print(f"\n{player_name}, do you want to replace a card? (yes/no): ")
        while True:
            choice = input().strip().lower()
            if choice in ['yes', 'no', 'y', 'n']:
                return choice in ['yes', 'y']
            print("Invalid input. Please enter 'yes' or 'no' (or 'y' or 'n'): ")

    def get_valid_card_index(self):
        print("Please enter the index from [0-4] of the card you want to replace: ")
        while True:
            try:
                index = int(input())
                if 0 <= index <= 4:
                    return index
                print("Invalid index. Please enter a number between 0 and 4: ")
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 4: ")

    def play_round(self):
        print(f"\n=== Round {self.round_number} ===")

        if self.round_number == 1:
            self.deck.generate_deck()
            self.deck.shuffle()
            self.deck.deal_cards(self.players)

        self.display_all_hands()

        for player in list(self.players):
            print(f"\n{player.display_hand()}")
            want_to_replace = self.get_valid_yes_no_input(player.name)

            if want_to_replace:
                index = self.get_valid_card_index()
                player.replace_card(index, self.deck)
                print(f"After replacement: {player.display_hand()}")

        

        print("\nFinal hands and points for this round:")
        for player in self.players:
            points = player.get_points(self.game_rules)
            print(f"{player.display_hand()} - Points: {points}")

        loser = min(self.players, key=lambda p: p.get_points(self.game_rules))
        print(f"\n{loser.name} is eliminated")
        self.players.remove(loser)
        self.round_number += 1
        
        
        if len(self.players) > 1:
            print("\nDealing 5 new cards to remaining players:")
            self.deck.deal_cards(self.players) 
            
    def start_game(self):
        while len(self.players) > 1:
            self.play_round()

        if len(self.players) == 1:
            print(f"\nThe winner is {self.players[0].name}!")
        else:
            print("\nIt's a tie!")


def main():
    player_names = []
    for i in range(3):
        print(f"Enter name for Player {i + 1}: ")
        name = input()
        player_names.append(name)

    players = [Player(name) for name in player_names]
    game = Game(players)

    print("\nGame started!")
    game.start_game()


if __name__ == "__main__":
    main() 