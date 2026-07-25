"""
Owner: José Lorente López | joselorente1105@gmail.com | Linkedin: www.linkedin.com/in/josé-lorente-lópez-0121b7148

Description: A Dragon Ball Sparking Zero-themed Python tournament simulator with classes for managing fighters and orchestrating battles, including speed-based turns and dynamic matchups.

Coding: UTF-8
"""

import random

class Fighter():
    """
    A class representing a fighter in the tournament.
    """
    
    def __init__(self, name, speed, attack, defense, health=100, turn=False):
        """
        Initialize a Fighter with specified attributes.

        Args:
            name (str): The name of the fighter.
            speed (int): The speed of the fighter, used to determine turn order.
            attack (int): The attack power of the fighter.
            defense (int): The defense rating of the fighter.
            health (float, optional): Initial health of the fighter. Defaults to 100.
            turn (bool, optional): Indicates if the fighter starts with the turn. Defaults to False.

        Returns:
            None
        """

        self.name = name
        self.speed = speed
        self.attack = attack
        self.defense = defense
        self.health = health
        self.turn = turn
    
    def get_name(self):
        """
        Get the name of the fighter.

        Returns:
            str: The name of the fighter.
        """

        return self.name
    
    def get_speed(self):
        """
        Get the speed attribute of the fighter.

        Returns:
            int: The speed of the fighter.
        """

        return self.speed
    
    def get_attack(self):
        """
        Get the attack attribute of the fighter.

        Returns:
            int: The attack power of the fighter.
        """
        return self.attack
    
    def get_defense(self):
        """
        Get the defense attribute of the fighter.

        Returns:
            int: The defense capability of the fighter.
        """

        return self.defense
    
    def get_health(self):
        """
        Get the current health of the fighter.

        Returns:
            float: The remaining health of the fighter.
        """

        return self.health

    def get_turn(self):
        """
        Get the current turn status of the fighter.

        Returns:
            bool: True if it's the fighter's turn, otherwise False.
        """

        return self.turn
    
    def set_health(self, health):
        """
        Set the health of the fighter.

        Args:
            health (float): The new health value to set for the fighter.

        Returns:
            None
        """

        self.health = health
    
    def set_turn(self, turn):
        """
        Set the turn status of the fighter.

        Args:
            turn (bool): True if the fighter should have the next turn, otherwise False.

        Returns:
            None
        """

        self.turn = turn


class Tournament():
    """
    A class representing a Dragon Ball Sparking Zero tournament where fighters compete in rounds.
    """
    
    def __init__(self) -> None:
        """
        Initialize the Tournament class.
        """
        pass

    @staticmethod
    def round(attacker, defender):
        """
        Simulates a round where the attacker attacks the defender, potentially causing damage.

        Args:
            attacker (Fighter): The fighter initiating the attack.
            defender (Fighter): The fighter attempting to defend against the attack.

        Returns:
            None
        """

        # Calculate the potential damage based on the difference between attack and defense.
        # If the defense of the defender is greater than the attack of the attacker, the minimum damage is 5.0
        attack_damage = max(attacker.get_attack() - defender.get_defense(), 5.0)

        # If the defender's defense is greater than the attacker's attack, reduce the damage.
        if defender.get_defense() > attacker.get_attack():
            # Reduce the defender's health by 10% of the calculated damage.
            reduced_damage = 0.1 * attack_damage
            defender.set_health(health=defender.get_health() - reduced_damage)
        else:
            # Apply the full damage if the defense is insufficient.
            defender.set_health(health=defender.get_health() - attack_damage)
                
    @staticmethod
    def fight(fighter1, fighter2):
        """
        Simulates a fight between two fighters until one of them loses all their health.

        Args:
            fighter1 (Fighter): The first fighter participating in the battle.
            fighter2 (Fighter): The second fighter participating in the battle.

        Returns:
            tuple: A tuple containing the winner (Fighter) and the loser (Fighter).

        The fight proceeds in turns, determined by the speed of the fighters:
            - The faster fighter gets the first turn.
            - During a turn, the attacking fighter has an 80% chance to successfully hit the opponent.
            - If the attack is successful, the 'round' method is called to calculate and apply damage.
            - If the attack fails, the opponent avoids the attack.
            - Turns alternate between the fighters until one of them has no health remaining.
        """

        # Determine who starts based on speed.
        if fighter1.get_speed() < fighter2.get_speed():
            fighter2.set_turn(turn=True)
        else:
            fighter1.set_turn(turn=True)

        while fighter1.get_health() > 0 and fighter2.get_health() > 0:
            # If it is fighter1's turn
            if fighter1.get_turn():
                if random.random() < 0.8:
                    Tournament.round(attacker=fighter1, defender=fighter2)
                    print(f"   {fighter2.get_name()} has been injured. Health: {fighter2.get_health()}")
                else:
                    print(f"   {fighter2.get_name()} has avoided the attack!")

                # Change the turn to fighter2
                fighter1.set_turn(turn=False)
                fighter2.set_turn(turn=True)

            # If it is fighter2's turn
            else:
                if random.random() < 0.8:
                    Tournament.round(attacker=fighter2, defender=fighter1)
                    print(f"   {fighter1.get_name()} has been injured. Health: {fighter1.get_health()}")
                else:
                    print(f"   {fighter1.get_name()} has avoided the attack!")

                # Change the turn to fighter1
                fighter2.set_turn(turn=False)
                fighter1.set_turn(turn=True)
    
        # Determine the winner based on remaining health.
        if fighter1.get_health() > 0:
            return fighter1, fighter2
        else:
            return fighter2, fighter1

    def __define_fighters(self):
        """
        Defines a list of fighters participating in the tournament.

        This method creates a list of Fighter objects, each representing a character
        with specific attributes like speed, attack, and defense. The list includes
        well-known characters from the Dragon Ball universe with varying combat abilities.

        Args:
            None

        Returns:
            None
        """

        self.fighters = [
            Fighter("Goku", speed=95, attack=100, defense=75),
            Fighter("Vegeta", speed=90, attack=95, defense=70),
            Fighter("Piccolo", speed=80, attack=75, defense=60),
            Fighter("Gohan", speed=85, attack=90, defense=65),
            Fighter("Trunks", speed=88, attack=85, defense=60),
            Fighter("Krillin", speed=70, attack=60, defense=55),
            Fighter("Frieza", speed=92, attack=98, defense=65),
            Fighter("Cell", speed=89, attack=97, defense=70),
            Fighter("Majin Buu", speed=75, attack=93, defense=65),
            Fighter("Android 18", speed=85, attack=80, defense=55),
            Fighter("Broly", speed=94, attack=99, defense=80),
            Fighter("Tien", speed=72, attack=65, defense=40),
            Fighter("Yamcha", speed=68, attack=55, defense=10),
            Fighter("Beerus", speed=100, attack=100, defense=80),
            Fighter("Jiren", speed=99, attack=98, defense=78),
            Fighter("Hit", speed=95, attack=97, defense=75)
        ]

    def __select_number_fighters(self):
        """
        Prompts the user to select the number of fighters for the tournament.

        This method asks the user to input the desired number of fighters.
        The input must be a positive integer, a power of 2, and less than or equal 
        to the total number of available fighters. If the input is invalid, the user 
        is prompted to try again until a valid input is provided.

        Args:
            None

        Returns:
            None
        """

        while True:
            try:
                print('Select the number of fighters: ')
                self.number_of_fighters = int(input())
                print(" ")

                if self.number_of_fighters > len(self.fighters):
                    print(f"The number must be less than or equal to {len(self.fighters)}. Please try again.")
                elif self.number_of_fighters > 0 and (self.number_of_fighters & (self.number_of_fighters - 1)) == 0:
                    print(f"Selected {self.number_of_fighters} fighters.\n")
                    break
                else:
                    print("The number must be a power of 2 (e.g., 2, 4, 8, 16). Please try again.")

            except ValueError:
                print("Invalid input. Please enter a positive integer.")

    def __pair_fighters(self):
        """
        Randomly pairs up fighters for the tournament battles.

        This method selects a random subset of fighters based on the specified number
        of fighters and pairs them for the initial matchups. Each pair represents a 
        matchup between two fighters, which will later engage in combat.

        Args:
            None

        Returns:
            None
        """

        selected_fighters = random.sample(self.fighters, self.number_of_fighters)
        self.pairs = [(selected_fighters[i], selected_fighters[i+1]) for i in range(0, len(selected_fighters), 2)]
        
        print("Matchups generated:")
        for fighter1, fighter2 in self.pairs:
            print(f"   {fighter1.name} vs {fighter2.name}")

    def __tournament_fights(self):
        """
        Conducts the tournament rounds until a final winner is determined.

        This method iteratively manages the rounds of the tournament by pairing fighters,
        conducting fights, and advancing the winners to the next round. It prints out
        the details of each matchup, including fighters' stats, and the outcome of each match.
        After each round, it re-pairs the winners for the next round and announces the losers.
        The process continues until only one final winner remains.

        Args:
            None

        Returns:
            None
        """

        round_number = 1
        while len(self.pairs) >= 2:
            winners = []
            lossers = []

            print(f"\n================== Round {round_number} ==================\n")

            for i, pair in enumerate(self.pairs):
                # Print the details of the fighters
                print(f"Match {i + 1}: {pair[0].get_name()} vs {pair[1].get_name()}\n")
                print(f"Health of {pair[0].get_name()}: {pair[0].get_health()} - Speed: {pair[0].get_speed()} - Defense: {pair[0].get_defense()} - Attack: {pair[0].get_attack()}")
                print(f"Health of {pair[1].get_name()}: {pair[1].get_health()} - Speed: {pair[1].get_speed()} - Defense: {pair[1].get_defense()} - Attack: {pair[1].get_attack()}\n")

                # Call the fight method and get the winner and loser
                winner, losser = Tournament.fight(fighter1=pair[0], fighter2=pair[1])
                winners.append(winner)
                lossers.append(losser)
                print(f"\nThe winner is: {winner.get_name()}\n")

            # Generate new pairings with the winners
            self.pairs = [(winners[i], winners[i+1]) for i in range(0, len(winners), 2)]
            print(" ")
            print(f"Round losers: {[losser.get_name() for losser in lossers]}\n")

            # Increment the round number for the next iteration
            round_number += 1

        # Final round between the last two fighters
        print(f"\n================== FINAL ROUND ==================\n")
        
        print(f"Health of {self.pairs[0][0].get_name()}: {self.pairs[0][0].get_health()} - Speed: {self.pairs[0][0].get_speed()} - Defense: {self.pairs[0][0].get_defense()} - Attack: {self.pairs[0][0].get_attack()}")
        print(f"Health of {self.pairs[0][1].get_name()}: {self.pairs[0][1].get_health()} - Speed: {self.pairs[0][1].get_speed()} - Defense: {self.pairs[0][1].get_defense()} - Attack: {self.pairs[0][1].get_attack()}\n")

        winner, losser = Tournament.fight(fighter1=self.pairs[0][0], fighter2=self.pairs[0][1])
        final_winner = winner

        print(f"\n=========== Winner ===========\n")
        print(f"The ultimate champion is: {final_winner.get_name()}\n")

    def run(self):
        """
        Runs the complete process of the tournament.

        This method orchestrates the entire tournament flow by calling the necessary 
        methods in sequence. It defines the fighters, allows the user to select the 
        number of participants, pairs up the fighters, and initiates the tournament 
        matches until a champion is determined.
        """

        self.__define_fighters()
        self.__select_number_fighters()
        self.__pair_fighters()
        self.__tournament_fights()


def main():
    """
    Runs the main function of the project.
    """

    print("\nWELCOME TO DRAGON BALL SPARKING ZERO TOURNAMENT!!!\n")

    Tournament().run()


if __name__ == "__main__":
    main()