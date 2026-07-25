# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23
import random

class Fighter:
    """Representa un luchador con atributos y salud inicial."""
    def __init__(self, name, speed, attack, defense):
        self.name = name
        self.speed = speed
        self.attack = attack
        self.defense = defense
        self.health = 100

    def take_damage(self, attacker):
        """Calcula el daño recibido tras un ataque."""
        
        # 20% posibilidad de esquivar
        if random.random() < 0.2:  
            print(f"{self.name} esquivó el ataque de {attacker.name}!")
            return
        damage = max(0, attacker.attack - self.defense)
        if self.defense > attacker.attack:

            # Recibe solo el 10% del daño
            damage *= 0.1  
        self.health -= damage
        print(f"{self.name} recibió {damage:.2f} puntos de daño de {attacker.name}. Salud restante: {self.health:.2f}")

def battle(fighter1, fighter2):
    """Simula una batalla entre dos luchadores."""
    print(f"¡Comienza la batalla entre {fighter1.name} y {fighter2.name}!")
    attacker, defender = (fighter1, fighter2) if fighter1.speed >= fighter2.speed else (fighter2, fighter1)
    
    while fighter1.health > 0 and fighter2.health > 0:
        defender.take_damage(attacker)
        
        # Cambiar roles
        attacker, defender = defender, attacker  
    
    winner = fighter1 if fighter1.health > 0 else fighter2
    print(f"¡{winner.name} gana la batalla!\n")
    return winner

def tournament(fighters):
    """Organiza un torneo de eliminación directa."""
    if len(fighters) & (len(fighters) - 1) != 0:
        raise ValueError("El número de luchadores debe ser potencia de 2.")
    
    round_number = 1
    while len(fighters) > 1:
        print(f"--- Ronda {round_number} ---")
        random.shuffle(fighters)
        next_round = []
        for i in range(0, len(fighters), 2):
            winner = battle(fighters[i], fighters[i + 1])
            next_round.append(winner)
        fighters = next_round
        round_number += 1
    
    print(f"¡El ganador del torneo es {fighters[0].name}!")

# Ejemplo de uso
fighters = [
    Fighter("Goku", 90, 95, 80),
    Fighter("Vegeta", 85, 90, 85),
    Fighter("Piccolo", 75, 80, 90),
    Fighter("Frieza", 80, 85, 75),
]

tournament(fighters)
