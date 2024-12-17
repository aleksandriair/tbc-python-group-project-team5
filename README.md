# Card Game

## 📝 Project Description
A command-line card game where 3 players compete in rounds using a standard deck of cards. Players can replace cards strategically, and the player with the lowest points in each round is eliminated. The game continues until only one player remains.

## 🔍 Methodology
The game uses a point-based system where:
* Number cards (2-10) are worth their face value
* Ace = 20 points
* King = 13 points
* Queen = 12 points
* Jack = 11 points

Players are eliminated based on having the lowest points in each round. In case of a tie, the game considers:
1. The number of cards of the same suit
2. The number of cards of the same value

## 🚀 Installation & Usage
* Ensure Python 3.x is installed on your system
* No additional packages are required
* Run the game using:
```bash
python card_game.py
```

## 📁 Project Structure
The project consists of several classes:
* `Card`: Represents individual cards with suit and value
* `Deck`: Manages the deck of cards and dealing
* `Player`: Handles player information and card manipulation
* `GameRules`: Contains point calculation and winner determination logic
* `Game`: Controls the game flow and rounds

## ✨ Contributors
Team 5:
* Guranda Jikia
* Ketevan Davreshidze
* Aleksandra Shalibashvili
