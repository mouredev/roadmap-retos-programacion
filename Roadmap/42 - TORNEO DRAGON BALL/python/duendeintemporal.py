#42 { Retos para Programadores } TORNEO DRAGON BALL

# Bibliography reference:
# I use GPT as a reference and sometimes to correct or generate proper comments.

"""
 * EJERCICIO:
 * ¡El último videojuego de Dragon Ball ya está aquí!
 * Se llama Dragon Ball: Sparking! ZERO.
 *
 * Simula un Torneo de Artes Marciales, al más puro estilo
 * de la saga, donde participarán diferentes luchadores, y el
 * sistema decidirá quién es el ganador.
 *
 * Luchadores:
 * - Nombre.
 * - Tres atributos: velocidad, ataque y defensa
 *   (con valores entre 0 a 100 que tú decidirás).
 * - Comienza cada batalla con 100 de salud.
 * Batalla:
 * - En cada batalla se enfrentan 2 luchadores.
 * - El luchador con más velocidad comienza atacando.
 * - El daño se calcula restando el daño de ataque del
 *   atacante menos la defensa del oponente.
 * - El oponente siempre tiene un 20% de posibilidad de
 *   esquivar el ataque.
 * - Si la defensa es mayor que el ataque, recibe un 10%
 *   del daño de ataque.
 * - Después de cada turno y ataque, el oponente pierde salud.
 * - La batalla finaliza cuando un luchador pierde toda su salud.
 * Torneo:
 * - Un torneo sólo es válido con un número de luchadores
 *   potencia de 2.
 * - El torneo debe crear parejas al azar en cada ronda.
 * - Los luchadores se enfrentan en rondas eliminatorias.
 * - El ganador avanza a la siguiente ronda hasta que sólo
 *   quede uno.
 * - Debes mostrar por consola todo lo que sucede en el torneo,
 *   así como el ganador.

"""

log = print

import random
import time
import asyncio

class Fighter:
    def __init__(self, id, name, speed, attack, defense):
        self.id = id
        self.name = name
        self.speed = speed
        self.attack = attack
        self.defense = defense
        self.health = 100  # Each fighter starts with 100 health

    def calculate_damage(self, opponent):
        damage = max(self.attack - opponent.defense, 0)  # No negative damage

        # Check if the opponent dodges the attack
        if random.random() < 0.2:  # 20% chance to dodge
            return 0  # No damage dealt

        # If the opponent's defense is greater than the attack, reduce damage
        if opponent.defense > self.attack:
            damage *= 0.1  # 10% of the attack damage

        return int(damage)  # Return the damage as an integer


class Battle:
    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.attacker = fighter1 if fighter1.speed >= fighter2.speed else fighter2
        self.defender = fighter2 if self.attacker == fighter1 else fighter1

    def winner(self, win_fighter):
        log(f"{win_fighter.name} is the winner!")

    def loser(self, los_fighter):
        log(f"{los_fighter.name} is the loser!")

    async def start(self):
        while self.fighter1.health > 0 and self.fighter2.health > 0:
            damage = self.attacker.calculate_damage(self.defender)

            # Ensure a minimum level of damage
            min_damage = 10
            actual_damage = max(min_damage, damage)

            self.defender.health -= actual_damage

            # Log the attack and damage
            if actual_damage == min_damage:
                log(f"{self.attacker.name}'s attack was partially blocked by {self.defender.name}, dealing {actual_damage} damage.")
            else:
                log(f"{self.attacker.name} attacks {self.defender.name} for {actual_damage} damage.")
            log(f"{self.defender.name} has {self.defender.health} health left.")

            # Swap roles for the next turn
            self.attacker, self.defender = self.defender, self.attacker

            # Introduce a delay between attacks
            await asyncio.sleep(0.5)

        winner = self.fighter1 if self.fighter1.health > 0 else self.fighter2
        log(f"{winner.name} wins the battle!")
        self.winner(winner)
        self.loser(self.fighter1 if winner == self.fighter2 else self.fighter2)

        return winner


class Tournament:
    def __init__(self, fighters):
        if not self.is_power_of_two(len(fighters)):
            raise ValueError("Number of fighters must be a power of 2.")
        self.fighters = fighters

    @staticmethod
    def is_power_of_two(n):
        return (n & (n - 1)) == 0 and n > 0  # Check if n is a power of two

    async def start(self):
        log("Starting the tournament...")
        round = 1

        while len(self.fighters) > 1:
            log(f"\n--- Round {round} ---")

            winners = []
            for i in range(0, len(self.fighters), 2):
                battle = Battle(self.fighters[i], self.fighters[i + 1])
                winner = await battle.start()
                winners.append(winner)

            log("\nWinners of Round " + str(round) + ":")
            for fighter in winners:
                log("- " + fighter.name)

            self.fighters = winners  # Update fighters for the next round
            round += 1

        log(f"\nThe champion of the tournament is {self.fighters[0].name}!")


# Create fighters
fighters = [
    Fighter(1, 'Goku', 95, 80, 50),
    Fighter(2, 'Vegeta', 90, 85, 45),
    Fighter(3, 'Gohan', 85, 75, 55),
    Fighter(4, 'Piccolo', 80, 70, 60),
    Fighter(5, 'Frieza', 88, 90, 40),
    Fighter(6, 'Cell', 85, 80, 50),
    Fighter(7, 'Majin Buu', 70, 60, 70),
    Fighter(8, 'Trunks', 75, 65, 65)
]

# Function to start the tournament
async def main():
    tournament = Tournament(fighters)
    await tournament.start()

# Run the tournament
if __name__ == "__main__":
    asyncio.run(main())


# Possible Output:
"""   
Starting the tournament...

--- Round 1 ---
Goku attacks Vegeta for 35 damage.
Vegeta has 65 health left.
Vegeta attacks Goku for 35 damage.
Goku has 65 health left.
Goku attacks Vegeta for 35 damage.
Vegeta has 30 health left.
Vegeta's attack was partially blocked by Goku, dealing 10 damage.
Goku has 55 health left.
Goku attacks Vegeta for 35 damage.
Vegeta has -5 health left.
Goku wins the battle!
Goku is the winner!
Vegeta is the loser!
Gohan attacks Piccolo for 15 damage.
Piccolo has 85 health left.
Piccolo attacks Gohan for 15 damage.
Gohan has 85 health left.
Gohan's attack was partially blocked by Piccolo, dealing 10 damage.
Piccolo has 75 health left.
Piccolo attacks Gohan for 15 damage.
Gohan has 70 health left.
Gohan attacks Piccolo for 15 damage.
Piccolo has 60 health left.
Piccolo's attack was partially blocked by Gohan, dealing 10 damage.
Gohan has 60 health left.
Gohan attacks Piccolo for 15 damage.
Piccolo has 45 health left.
Piccolo attacks Gohan for 15 damage.
Gohan has 45 health left.
Gohan attacks Piccolo for 15 damage.
Piccolo has 30 health left.
Piccolo attacks Gohan for 15 damage.
Gohan has 30 health left.
Gohan attacks Piccolo for 15 damage.
Piccolo has 15 health left.
Piccolo attacks Gohan for 15 damage.
Gohan has 15 health left.
Gohan attacks Piccolo for 15 damage.
Piccolo has 0 health left.
Gohan wins the battle!
Gohan is the winner!
Piccolo is the loser!
Frieza's attack was partially blocked by Cell, dealing 10 damage.
Cell has 90 health left.
Cell's attack was partially blocked by Frieza, dealing 10 damage.
Frieza has 90 health left.
Frieza attacks Cell for 40 damage.
Cell has 50 health left.
Cell attacks Frieza for 40 damage.
Frieza has 50 health left.
Frieza attacks Cell for 40 damage.
Cell has 10 health left.
Cell attacks Frieza for 40 damage.
Frieza has 10 health left.
Frieza attacks Cell for 40 damage.
Cell has -30 health left.
Frieza wins the battle!
Frieza is the winner!
Cell is the loser!
Trunks's attack was partially blocked by Majin Buu, dealing 10 damage.
Majin Buu has 90 health left.
Majin Buu's attack was partially blocked by Trunks, dealing 10 damage.
Trunks has 90 health left.
Trunks's attack was partially blocked by Majin Buu, dealing 10 damage.
Majin Buu has 80 health left.
Majin Buu's attack was partially blocked by Trunks, dealing 10 damage.
Trunks has 80 health left.
Trunks's attack was partially blocked by Majin Buu, dealing 10 damage.
Majin Buu has 70 health left.
Majin Buu's attack was partially blocked by Trunks, dealing 10 damage.
Trunks has 70 health left.
Trunks's attack was partially blocked by Majin Buu, dealing 10 damage.
Majin Buu has 60 health left.
Majin Buu's attack was partially blocked by Trunks, dealing 10 damage.
Trunks has 60 health left.
Trunks's attack was partially blocked by Majin Buu, dealing 10 damage.
Majin Buu has 50 health left.
Majin Buu's attack was partially blocked by Trunks, dealing 10 damage.
Trunks has 50 health left.
Trunks's attack was partially blocked by Majin Buu, dealing 10 damage.
Majin Buu has 40 health left.
Majin Buu's attack was partially blocked by Trunks, dealing 10 damage.
Trunks has 40 health left.
Trunks's attack was partially blocked by Majin Buu, dealing 10 damage.
Majin Buu has 30 health left.
Majin Buu's attack was partially blocked by Trunks, dealing 10 damage.
Trunks has 30 health left.
Trunks's attack was partially blocked by Majin Buu, dealing 10 damage.
Majin Buu has 20 health left.
Majin Buu's attack was partially blocked by Trunks, dealing 10 damage.
Trunks has 20 health left.
Trunks's attack was partially blocked by Majin Buu, dealing 10 damage.
Majin Buu has 10 health left.
Majin Buu's attack was partially blocked by Trunks, dealing 10 damage.
Trunks has 10 health left.
Trunks's attack was partially blocked by Majin Buu, dealing 10 damage.
Majin Buu has 0 health left.
Trunks wins the battle!
Trunks is the winner!
Majin Buu is the loser!

Winners of Round 1:
- Goku
- Gohan
- Frieza
- Trunks

--- Round 2 ---
Goku attacks Gohan for 25 damage.
Gohan has -10 health left.
Goku wins the battle!
Goku is the winner!
Gohan is the loser!
Frieza attacks Trunks for 25 damage.
Trunks has -15 health left.
Frieza wins the battle!
Frieza is the winner!
Trunks is the loser!

Winners of Round 2:
- Goku
- Frieza

--- Round 3 ---
Goku's attack was partially blocked by Frieza, dealing 10 damage.
Frieza has 0 health left.
Goku wins the battle!
Goku is the winner!
Frieza is the loser!

Winners of Round 3:
- Goku

The champion of the tournament is Goku!

"""