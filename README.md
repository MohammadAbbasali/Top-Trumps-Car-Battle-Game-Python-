# Top Trumps – Car Battle Game

**Top Trumps – Car Battle Game** is a console-based Python project where players compete against the computer using a deck of car cards.  
Each car has different performance stats — such as **Top Speed**, **Cylinders**, and **Efficiency Score** — and each round compares one chosen attribute to determine who wins.  
The winner collects both cards, and the game continues until one player runs out of competitive cards.

---

## Features
- 24 unique car cards from well-known brands (BMW, Mercedes, Audi, Toyota, Kia, Hyundai)
- Player vs Computer battle system with both random and user-selected comparison attributes
- Tie-handling logic with a **pot system** that carries cards to the next round
- Player’s deck is automatically saved to a local file (`Player_Cars.txt`)
- Simple and interactive console interface
- Automatic game flow that tracks turns, deck sizes, and winning conditions

---

## Technologies Used
- **Language:** Python 3  
- **Libraries:** `random`, `time`, `os`

---

## How to Play

1. **Clone or download** this repository:
   ```bash
   git clone https://github.com/yourusername/top-trumps-car-game.git
   cd top-trumps-car-game


# Run the game:

python car_game.py



Follow the on-screen instructions:

View your current top car card.

Choose a stat to compare (Name Score, Top Speed, Cylinders, or Efficiency).

The winner collects both cards and continues the next round.

If there’s a tie, cards go into the “pot” until the next win.



Game Objective :
Continue playing rounds to win as many cards as possible.
If the computer’s deck drops to 8 cards or fewer — you win!
If your deck drops to 8 or fewer — the computer wins.



File Output: 
During gameplay, your current deck is saved to:
Player_Cars.txt



Example Gameplay :
Welcome to the game dear!
Please Wait ...
If you are ready, let's start!

This is your card: 2022 BMW X5 in Black | Name Score: 8, Top Speed: 240 km/h, Cylinders: 6, Efficiency: 7/10
Please you start! Choose a measure:
1 - name_score
2 - top_speed
3 - cylinders
4 - efficiency_score




Future Improvements :

Add a graphical user interface (GUI) using tkinter or pygame

Add a leaderboard and persistent save system

Add sound effects and animations




Developed by MohamadMahdi Abasali

