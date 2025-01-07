#32 { Retos para Programadores } BATALLA DEADPOOL Y WOLVERINE

# Bibliography reference:
# I use GPT as a reference and sometimes to correct or generate proper comments.

"""  
* EJERCICIO:
 * ¡Deadpool y Wolverine se enfrentan en una batalla épica!
 * Crea un programa que simule la pelea y determine un ganador.
 * El programa simula un combate por turnos, donde cada protagonista posee unos
 * puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
 * de regeneración y evasión de ataques.
 * Requisitos:
 * 1. El usuario debe determinar la vida inicial de cada protagonista.
 * 2. Cada personaje puede impartir un daño aleatorio:
 *    - Deadpool: Entre 10 y 100.
 *    - Wolverine: Entre 10 y 120.
 * 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
 * siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
 * 4. Cada personaje puede evitar el ataque contrario:
 *    - Deadpool: 25% de posibilidades.
 *    - Wolverine: 20% de posibilidades.
 * 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
 * Acciones:
 * 1. Simula una batalla.
 * 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
 * 3. Muestra qué pasa en cada turno.
 * 4. Muestra la vida en cada turno.
 * 5. Muestra el resultado final.

"""

""" The original code version was created in JavaScript, which allows the use of CSS styles for effects and Data URI images to visualize the opponents. Since Python does not have a built-in way to handle CSS styles or HTML directly, we will focus on the logic of the combat system and simulate the battle in a console-based format. """

log = print

import random
import time

class Combatant:
    def __init__(self, name, avatar, life, atk_max, atk_min, defense):
        self.name = name
        self.avatar = avatar
        self.life = life
        self.attack_damage_max = atk_max
        self.attack_damage_min = atk_min
        self.defense = defense
        self.attack_potence = atk_max

class Battle:
    def __init__(self, c1, c2):
        self.combatant1 = c1
        self.combatant2 = c2
        self.result = ''
        self.battle_interval = None

    def start_battle(self):
        is_attacking = False

        while self.combatant1.life > 0 and self.combatant2.life > 0:
            if not is_attacking:
                is_attacking = True
                self.round()
                time.sleep(4.5)  # Simulate the time between attacks
                is_attacking = False
            time.sleep(1.5)  # Wait before the next round

    def attack(self, attacker, defender):
        log(f"Attacker: {attacker.name}, Defender: {defender.name}")

        avoid_attack = random.randint(0, 100)

        if avoid_attack < 101 - defender.defense:
            max_damage = min(attacker.attack_damage_max, attacker.attack_potence)
            min_damage = attacker.attack_damage_min
            damage = random.randint(min_damage, max_damage)

            defender.life -= damage
            attacker.attack_potence -= 10  # Decrease attack potency

            log(f"{attacker.name} dealt {damage} damage to {defender.name}. {defender.name} has {defender.life} life left.")

            if defender.life <= 0:
                self.declare_winner(attacker, defender)
                return

        else:
            log(f"{defender.name} blocked {attacker.name}'s attack.")

        if attacker.attack_potence < attacker.attack_damage_min:
            attacker.attack_potence = attacker.attack_damage_min

    def declare_winner(self, winner, loser):
        log(f"{winner.name} is the winner!")
        self.result = f"{winner.name} is the winner!"

    def round(self):
        if self.combatant1.life > 0 and self.combatant2.life > 0:
            position = random.randint(0, 1)
            if position == 1:
                self.attack(self.combatant1, self.combatant2)
            else:
                self.attack(self.combatant2, self.combatant1)
        else:
            if self.combatant1.life <= 0 and self.combatant2.life <= 0:
                log("It's a draw!")
            elif self.combatant1.life <= 0:
                self.declare_winner(self.combatant2, self.combatant1)
            else:
                self.declare_winner(self.combatant1, self.combatant2)

# Create combatants
WOLVERINE = Combatant('Wolverine', 'avatar', 100, 120, 10, 20)
DEADPOOL = Combatant('Deadpool', 'avatar', 100, 100, 10, 25)

# Start the battle
battle1 = Battle(WOLVERINE, DEADPOOL)

if __name__ == "__main__":
    battle1.start_battle()

"""  
Attacker: Wolverine, Defender: Deadpool
Wolverine dealt 38 damage to Deadpool. Deadpool has 62 life left.
Attacker: Wolverine, Defender: Deadpool
Wolverine dealt 57 damage to Deadpool. Deadpool has 5 life left.
Attacker: Wolverine, Defender: Deadpool
Deadpool blocked Wolverine's attack.
Attacker: Deadpool, Defender: Wolverine
Deadpool dealt 27 damage to Wolverine. Wolverine has 73 life left.
Attacker: Deadpool, Defender: Wolverine
Deadpool dealt 66 damage to Wolverine. Wolverine has 7 life left.
Attacker: Deadpool, Defender: Wolverine
Deadpool dealt 23 damage to Wolverine. Wolverine has -16 life left.
Deadpool is the winner!

"""