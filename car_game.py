import time
import random
import os

# --- Car Class ---

class Car:
    """
    Represents a car card with core attributes for the Top Trumps game.
    Attributes include brand, model, year, and four comparison metrics.
    """
    def __init__(self, brand, model, year, color, name_score, top_speed, cylinders, efficiency_score):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.name_score = name_score
        self.top_speed = top_speed  # in km/h
        self.cylinders = cylinders
        self.efficiency_score = efficiency_score  # score out of 10

    def show_info(self):
        """Returns a formatted string of the car's attributes."""
        return (f"{self.year} {self.brand} {self.model} in {self.color} | "
                f"Name Score: {self.name_score}, Top Speed: {self.top_speed} km/h, "
                f"Cylinders: {self.cylinders}, Efficiency: {self.efficiency_score}/10")

    def __str__(self):
        """Defines the print representation of the Car object."""
        return self.show_info()


# --- Game Logic Function ---

def compare_and_pop(list1, list2, measure):
    """
    Pops the top card from each list, compares them based on the measure,
    and returns the cards and the comparison result.
    """
    player = False
    computer = False
    same = False
    car1 = None
    car2 = None

    if list1 and list2:
        # Pop the top card from the front of each deck
        car1 = list1.pop(0)
        car2 = list2.pop(0)

        # 1: Name Score (Higher is better)
        if measure == 1:
            val1, val2 = car1.name_score, car2.name_score
            stat = "Name Score"
        # 2: Top Speed (Higher is better)
        elif measure == 2:
            val1, val2 = car1.top_speed, car2.top_speed
            stat = "Top Speed"
        # 3: Cylinders (Higher is better)
        elif measure == 3:
            val1, val2 = car1.cylinders, car2.cylinders
            stat = "Cylinders"
        # 4: Efficiency Score (Higher is better)
        elif measure == 4:
            val1, val2 = car1.efficiency_score, car2.efficiency_score
            stat = "Efficiency Score"
        else:
            # Handle unexpected measure input
            print("Invalid measure detected. Treating as a tie.")
            same = True
            stat = "Invalid Measure"

        # Determine winner if not a tie (or invalid measure)
        if not same:
            if val1 > val2:
                print(f"Player wins! {car1.brand} {car1.model} has a higher {stat} ({val1} > {val2}).")
                player = True
            elif val1 < val2:
                print(f"Computer wins! {car2.brand} {car2.model} has a higher {stat} ({val2} > {val1}).")
                computer = True
            else:
                print(f"Tie! Both cards have the same {stat} ({val1}).")
                same = True
    
    return car1, car2, player, computer, same


# --- Car Data Initialization ---

Car1 = Car("BMW", "X5", 2022, "Black", 8, 240, 6, 7)
Car2 = Car("Toyota", "Camry", 2020, "White", 7, 210, 4, 8)
Car3 = Car("Mercedes", "C-Class", 2019, "Silver", 9, 230, 4, 7)
Car4 = Car("Audi", "A4", 2021, "Red", 8, 225, 4, 7)
Car5 = Car("Kia", "Sportage", 2022, "Blue", 7, 200, 4, 8)
Car6 = Car("Hyundai", "Elantra", 2023, "Gray", 6, 195, 4, 9)
Car7 = Car("BMW", "X5", 2022, "Black", 8, 240, 6, 7)
Car8 = Car("Toyota", "Corolla", 2021, "White", 7, 190, 4, 8)
Car9 = Car("Mercedes", "E-Class", 2020, "Black", 9, 250, 6, 7)
Car10 = Car("Audi", "Q7", 2023, "Blue", 8, 245, 6, 6)
Car11 = Car("Kia", "Rio", 2019, "Silver", 7, 180, 4, 8)
Car12 = Car("Hyundai", "Sonata", 2020, "Red", 6, 200, 4, 9)
Car13 = Car("BMW", "M3", 2021, "Gray", 9, 280, 6, 6)
Car14 = Car("Toyota", "Camry", 2020, "White", 7, 210, 4, 8)
Car15 = Car("Mercedes", "C-Class", 2019, "Silver", 9, 230, 4, 7)
Car16 = Car("Audi", "A4", 2021, "Red", 8, 225, 4, 7)
Car17 = Car("Kia", "Sportage", 2022, "Blue", 7, 200, 4, 8)
Car18 = Car("Hyundai", "Elantra", 2023, "Gray", 6, 195, 4, 9)
Car19 = Car("BMW", "X6", 2020, "Black", 8, 250, 6, 7)
Car20 = Car("Toyota", "Yaris", 2022, "Red", 7, 180, 4, 9)
Car21 = Car("Mercedes", "GLA", 2023, "Blue", 9, 240, 4, 7)
Car22 = Car("Audi", "Q5", 2018, "Silver", 8, 230, 6, 7)
Car23 = Car("Kia", "Cerato", 2021, "White", 7, 190, 4, 8)
Car24 = Car("Hyundai", "Accent", 2019, "Gray", 6, 180, 4, 9)

cars = [
    Car1, Car2, Car3, Car4, Car5, Car6,
    Car7, Car8, Car9, Car10, Car11, Car12,
    Car13, Car14, Car15, Car16, Car17, Car18,
    Car19, Car20, Car21, Car22, Car23, Car24
]

random.shuffle(cars)

# Split the deck
Computer_Car = cars[:12]
Player_Car = cars[12:]

# Initialize the 'Pot' for tied cards (list handles multiple consecutive ties)
pot_cards = []

# --- Game Start Messages ---

print("Welcome to the game dear !")
print("Please Wait ... ")
time.sleep(3)

# Clear screen (works best on Windows with 'cls', or Unix/Linux/Mac with 'clear')
os.system('cls' if os.name == 'nt' else 'clear')

print("If you are ready Lets start")
time.sleep(1)

# Write player cars to a file for reference
with open("Player_Cars.txt", "w") as file:
    for i, car in enumerate(Player_Car, start=1):
        file.write(f"{i} - {car}\n")

print("Player Cars have been written to 'Player_Cars.txt'.")
print("You can see your cards in Player_Cars file in the local repository of this project.")
time.sleep(1)

# Determine who starts the first round (1 = Player, 0 = Computer)
num = random.choice([0, 1])

# --- Main Game Loop ---

while Computer_Car and Player_Car:

    # Original win condition: win when opponent's deck is small (10 cards or less)
    if len(Computer_Car) <= 8:
        print("\n==============================================")
        print("You Won! Computer has run out of competitive cards.")
        print("==============================================")
        break
    elif len(Player_Car) <= 8:
        print("\n==============================================")
        print("I Win Buddy !!!! You ran out of competitive cards.")
        print("==============================================")
        break

    # Display current deck status
    print(f"\n--- Round Start --- (Pot: {len(pot_cards)} cards)")
    print(f"Player Deck Size: {len(Player_Car)} | Computer Deck Size: {len(Computer_Car)}")

    # Player's top card
    Chosen_Player = Player_Car[0]
    print(f"\nThis is your card: {Chosen_Player}")

    # Computer's top card (hidden initially)
    Chosen_Computer = Computer_Car[0]

    # Decide on the measure based on whose turn it is
    measure = 0
    if num == 1:
        print("\nPlease you start! Choose a measure:")
        print("1- name_score \n2- top_speed\n3- cylinders\n4- efficiency_score")
        try:
            measure = int(input("Enter your measure for comparing (1-4): "))
            if measure not in [1, 2, 3, 4]:
                # Force a random choice if input is invalid
                measure = random.choice([1, 2, 3, 4])
                print(f"Invalid input. Computer chooses measure {measure} for you.")
        except ValueError:
            measure = random.choice([1, 2, 3, 4])
            print(f"Invalid input. Computer chooses measure {measure} for you.")
    else:
        print("I will Start by choosing a random measure (1 or 4).")
        # Computer's simple choice logic
        measure = random.choice([1, 4])


    # Announce the chosen measure
    measure_names = {1: "Name Score", 2: "Top Speed", 3: "Cylinders", 4: "Efficiency Score"}
    print(f"\nComparing based on: {measure_names.get(measure, 'Unknown Measure')}")
    print("The game is starting ... !")
    time.sleep(1)

    # Show the computer's card now that comparison is set
    print(f"This is my card: {Chosen_Computer}")
    time.sleep(1)


    # Compare the cards and pop them from the decks
    car1, car2, player, computer, same = compare_and_pop(Player_Car, Computer_Car, measure)
    print("Please wait...")
    time.sleep(2)

    # --- Result and Card Collection Logic (The Tie Fix) ---
    
    # Bundle the current two cards and all cards from the pot
    all_won_cards = [car1, car2] + pot_cards

    if player:
        # Player wins: takes current cards AND all pot cards
        print(f"\nPlayer takes {len(all_won_cards)} cards! ({len(pot_cards)} were in the pot)")
        Player_Car.extend(all_won_cards)
        pot_cards = []  # Pot is cleared
        num = 1 # Player keeps the turn

    elif computer:
        # Computer wins: takes current cards AND all pot cards
        print(f"\nComputer takes {len(all_won_cards)} cards! ({len(pot_cards)} were in the pot)")
        Computer_Car.extend(all_won_cards)
        pot_cards = []  # Pot is cleared
        num = 0 # Computer keeps the turn

    elif same:
        # Tie: current cards are added to the pot for the next winner
        print(f"\nTie! The two cards are added to the pot, now containing {len(pot_cards) + 2} cards.")
        pot_cards.append(car1)
        pot_cards.append(car2)
        # Turn does not change in a tie (the player who chose the measure chooses again)


    # Update the player's external card list file
    with open("Player_Cars.txt", "w") as file:
        for i, car in enumerate(Player_Car, start=1):
            file.write(f"{i} - {car}\n")
    
    time.sleep(2)
    input("Press Enter to continue to the next round...")

print("\nGame session finished.")

# --- ADDED CODE TO PAUSE THE CONSOLE ---
# This line prevents the console/terminal window from closing immediately 
# after the 'Game session finished' message is displayed.
input("The game has ended. Press Enter to close the window...")
