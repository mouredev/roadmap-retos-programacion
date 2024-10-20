import random
import math

# Function to check if a number is a power of 2
def is_power_of_two(n):
    if n <= 0:
        return False
    log2_n = math.log2(n)
    return log2_n.is_integer()

# Get the number of fighters ensuring it's a power of 2
def get_number_of_fighters() -> int:
    while True:
        number_of_fighters = input("Enter the number of fighters (must be a power of 2): ")
        if validate_input(number_of_fighters, min_value=2) and is_power_of_two(int(number_of_fighters)):
            return int(number_of_fighters)
        else:
            print("Please enter a number that is a power of 2 (e.g., 2, 4, 8, 16, 32, etc.)")

# Unified validation function for input
def validate_input(input_value, even=False, min_value=0, max_value=100) -> bool:
    try:
        number = int(input_value)
        if even and number % 2 != 0:
            print("Please enter an even number.")
            return False
        if not (min_value <= number <= max_value):
            print(f"Please enter a number between {min_value} and {max_value}.")
            return False
        return True
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return False

# Function to create a list of fighters by collecting their stats
def create_fighters(number_of_fighters) -> list:
    fighters_list = []
    for i in range(number_of_fighters):
        name = input(f"Enter fighter's name #{i + 1}: ")
        strength = get_fighter_property(f"Enter {name}'s strength (1-100): ", min_value=1)
        defense = get_fighter_property(f"Enter {name}'s defense (0-100): ")
        velocity = get_fighter_property(f"Enter {name}'s speed (0-100): ")
        fighters_list.append(Fighter(name, strength, defense, velocity))
        print()
    return fighters_list

# Function to get and validate a fighter's property
def get_fighter_property(property_text, min_value = 0) -> int:
    while True:
        property_value = input(property_text)
        if validate_input(property_value, min_value=min_value):
            return int(property_value)

# Function to shuffle fighters and pair them up
def prepare_combats(fighters):
    print("Preparing matchups...\n")
    random.shuffle(fighters)
    return [fighters[i:i + 2] for i in range(0, len(fighters), 2)]

# Start the tournament and progress through rounds
def start_tournament(fighters):
    print("The tournament begins!\n")
    round_number = 1
    while len(fighters) > 1:
        print(f"Round #{round_number}")
        combats = prepare_combats(fighters)
        fighters = play_round(combats)
        for fighter in fighters:
            fighter.reset_health()  # Reset health for the next round
        round_number += 1
    return fighters[0]

# Play a round and return the list of winners
def play_round(fights):
    winners = []
    for fighters in fights:
        print(f"{fighters[0].name} vs {fighters[1].name}")
        winner = combat(fighters)
        winners.append(winner)
        print(f"{winner.name} wins the match!\n")
    return winners

# Manage the combat logic between two fighters
def combat(fighters):
    fighter_1, fighter_2 = (fighters[0], fighters[1]) if fighters[0].velocity > fighters[1].velocity else (fighters[1], fighters[0])
    turn = 1
    while fighter_1.health_points > 0 and fighter_2.health_points > 0:
        print(f"Turn #{turn}: {fighter_1.name} attacks {fighter_2.name}")
        combat_turn(fighter_1, fighter_2)
        if fighter_2.health_points > 0:  # If fighter 2 survives, they counterattack
            print(f"Turn #{turn}: {fighter_2.name} counterattacks {fighter_1.name}")
            combat_turn(fighter_2, fighter_1)
        print(f"{fighter_1.name}: {fighter_1.health_points} HP, {fighter_2.name}: {fighter_2.health_points} HP\n")
        turn += 1
    return fighter_1 if fighter_2.health_points <= 0 else fighter_2

# Simulate one attack between two fighters
def combat_turn(attacker, defender):
    if random.random() > 0.2:  # 80% chance to hit
        damage = max(1, attacker.strength * 0.1) if attacker.strength >= defender.defense else max(1, attacker.strength - defender.defense)
        defender.health_points -= damage  # Ensure defender loses health points
        print(f"{attacker.name} hits {defender.name} for {damage:.2f} damage!")
    else:
        print(f"{defender.name} dodges the attack!")

# Fighter class definition with a health reset method
class Fighter:
    def __init__(self, name, strength, defense, velocity):
        self.name = name
        self.strength = strength
        self.defense = defense
        self.velocity = velocity
        self.health_points = 100

    def reset_health(self):
        self.health_points = 100  # Reset health to 100 before each new round

    def __repr__(self):
        return f"{self.name}: Strength {self.strength}, Defense {self.defense}, Speed {self.velocity}"

# Main function to initiate the tournament
def main():
    print("Welcome to the Budokai Tenkaichi Tournament!\n")
    number_of_fighters = get_number_of_fighters()
    fighters = create_fighters(number_of_fighters)
    print("\nThe participants are:")
    for fighter in fighters:
        print(fighter)
    winner = start_tournament(fighters)
    print(f"\nThe tournament champion is {winner.name}!")

if __name__ == '__main__':
    main()
