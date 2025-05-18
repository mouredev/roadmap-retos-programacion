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

from abc import ABC, abstractmethod
import random
import time

PAUSE_DURATION = 3

class SuperHero(ABC): # La clase abstracta superhero, sirve de intarfaz y centraliza metodos comunes.
    def __init__(self, life_points):
        self.life_points = life_points
        self.regenerating = False

    @abstractmethod
    def calculate_attack_damage(self) -> int:
        pass

    @abstractmethod
    def is_max_damage(self, damage: int) -> bool:
        pass

    def reduce_health(self, attack_points):
        self.life_points = max(0, self.life_points - attack_points)

    @abstractmethod
    def dodge_attack(self) -> bool:
        pass

    @abstractmethod
    def must_skip_turn_due_to_regeneration(self) ->bool:
        pass

    def attack(self, damage: int, critic_damage: bool):
        name = self.__class__.__name__
        if not self.dodge_attack():
            self.reduce_health(damage)
            print(f"{name} recibe el ataque de fuerza {damage}. Vida restante: {self.life_points}")
            time.sleep(PAUSE_DURATION)
            if critic_damage:
                print(f"El ataque es crítico. {name} debe regenerarse.")
                time.sleep(PAUSE_DURATION)
                self.regenerating = True
        else:
            print(f"{name} [VIDA:{self.life_points}] consigue evitar el ataque.")
            time.sleep(PAUSE_DURATION)


class Wolverine(SuperHero):# Define sus propias habilidades
    def calculate_attack_damage(self):
        return random.randint(1,12) * 10
    
    def is_max_damage(self, damage):
        return damage == 120

    def dodge_attack(self):
        return random.randint(1, 5) == 1

    def must_skip_turn_due_to_regeneration(self):
        if self.regenerating == True:
            print(f"Wolverine [VIDA:{self.life_points}] tiene que regenerarse. No ataca en este turno")
            time.sleep(PAUSE_DURATION)
            self.regenerating = False
            return True
        return False
    

class Deadpool(SuperHero):
    def calculate_attack_damage(self):
        return random.randint(1,10) * 10
    
    def is_max_damage(self, damage):
        return damage == 100

    def dodge_attack(self):
        return random.randint(1, 4) == 1

    def must_skip_turn_due_to_regeneration(self):
        if self.regenerating == True:
            print(f"Deadpool [VIDA:{self.life_points}] tiene que regenerarse. No ataca en este turno")
            time.sleep(PAUSE_DURATION)
            self.regenerating = False
            return True
        return False
    

class Battle:# Gestiona los turnos y la batalla en si.
    def __init__(self, hero1: SuperHero, hero2: SuperHero):
        self.heroes = [hero1, hero2]
        random.shuffle(self.heroes)# Para que empiece una de forma aleatoria.

    def check_active_battle(self):
        for heroe in self.heroes:
            if heroe.life_points == 0:
                return False
        return True

    def start_battle(self):
        turn = 1
        aux_count = 1
        while self.check_active_battle():
            if aux_count % 2 != 0:
                print(f"TURNO {turn}:")
                turn += 1
            active_heroe: SuperHero = self.heroes.pop(0)
            print(f"Turno de {active_heroe.__class__.__name__} [VIDA:{active_heroe.life_points}]")
            time.sleep(PAUSE_DURATION)
            if active_heroe.must_skip_turn_due_to_regeneration():
                self.heroes.append(active_heroe)
            else:
                attack_damage = active_heroe.calculate_attack_damage()
                print(f"{active_heroe.__class__.__name__} [VIDA:{active_heroe.life_points}] ataca con fuerza {attack_damage}")
                time.sleep(PAUSE_DURATION)
                self.heroes[0].attack(attack_damage, active_heroe.is_max_damage(attack_damage))
                self.heroes.append(active_heroe)
            aux_count += 1
        winner = [h for h in self.heroes if h.life_points > 0][0]
        print(f"\n{winner.__class__.__name__} ha ganado la batalla con {winner.life_points} puntos de vida.")


def main():
    wolverine_life = int(input("Vida de Wolverine: "))
    deadpool_life = int(input("Vida de Deadpool: "))
    wolverine = Wolverine(wolverine_life)
    deadpool = Deadpool(deadpool_life)
    Battle(wolverine, deadpool).start_battle()

main()   