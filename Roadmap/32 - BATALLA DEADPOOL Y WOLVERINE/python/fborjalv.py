"""

/*
 * EJERCICIO:
 * ¡Deadpool y Wolverine se enfrentan en una batalla épica!
 * Crea un programa que simule la pelea y determine un ganador.
 * El programa simula un combate por turnos, donde cada protagonista posee unos
 * puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
 * de regeneración y evasión de ataques.
 * Requisitos:
 * 1. El usuario debe determinar la vida inicial de cada protagonista. ✅
 * 2. Cada personaje puede impartir un daño aleatorio: ✅
 *    - Deadpool: Entre 10 y 100.
 *    - Wolverine: Entre 10 y 120.
 * 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el ✅
 * siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
 * 4. Cada personaje puede evitar el ataque contrario: ✅
 *    - Deadpool: 25% de posibilidades.
 *    - Wolverine: 20% de posibilidades.
 * 5. Un personaje pierde si sus puntos de vida llegan a cero o menos. ✅
 * Acciones:
 * 1. Simula una batalla. ✅
 * 2. Muestra el número del turno (pausa de 1 segundo entre turnos). ✅
 * 3. Muestra qué pasa en cada turno. ✅
 * 4. Muestra la vida en cada turno. ✅
 * 5. Muestra el resultado final. ✅
 */


"""

import random
from time import sleep
class Character:
    def __init__(self, health) -> None:
        self.name = ""
        self.health = health
        self.min_damage = 0
        self.max_damage = 0
        self.damage = 0
        self.evassion = 0
    def evade_attack(self):
        return random.random() < self.evassion

    def attack(self, enemy):
        self.damage = random.randint(self.min_damage, self.max_damage)
        if not enemy.evade_attack():
            enemy.health -= self.damage
            print(f"{self.name} ha golpeado a {enemy.name}. Ha realizado un ataque de {self.damage} puntos")
            print(f"Ahora la salud de {enemy.name} es de {enemy.health}")
        else:
            print(f"{enemy.name} ha evitado el ataque de {self.name}")

    def is_critical(self, enemy):
        if self.damage == self.max_damage:
            print(f"{self.name} le ha dado golpe críticoa {enemy.name}, que pierde un turno de ataque para regenerarse")
            return True
        else: 
            return False

class Deadpool(Character):
    def __init__(self, health) -> None:
        super().__init__(health)
        self.name = "Deadpool"
        self.min_damage = 10
        self.max_damage = 100
        self.evassion = 0.25


class Wolverine(Character):
    def __init__(self, health) -> None:
        super().__init__(health)
        self.name = "Wolverine"
        self.min_damage = 10
        self.max_damage = 120
        self.evassion = 0.2

class Game:

    def __init__(self) -> None:
        dp_health = int(input("Introduce puntos de salud para Deadpool: "))
        wv_health = int(input("Introduce puntos de salud para Wolverine: "))
        self.player1, self.player2  = random.sample([Deadpool(dp_health), Wolverine(wv_health)], 2)
        self.turn = 0

    def is_character_alive(self):
        if self.player1.health <= 0 or self.player2.health <=0:
            winner = max(self.player1, self.player2, key= lambda x: x.health)
            loser = min(self.player1, self.player2, key= lambda x: x.health)
            print(f"{winner.name} ha ganado el combate a {loser.name}")
            return False
        else: 
            return True


    def init_game(self):
        
        print(f"{self.player1.name} comienza atacando a {self.player2.name}")
        turn_off_player1 = False
        turn_off_player2 = False
        while self.player1.health > 0 and self.player2.health > 0:
            
            sleep(3)
            print(f"Turno: {self.turn} ----------")
            self.turn +=1
            if not turn_off_player1: 
                self.player1.attack(self.player2)
                if not self.is_character_alive(): break
                turn_off_player2 = False
                if self.player1.is_critical(self.player2):
                    turn_off_player2 = True

            if not turn_off_player2:    
                self.player2.attack(self.player1)
                if not self.is_character_alive(): break
                turn_off_player1 = False
                if self.player2.is_critical(self.player1):
                    turn_off_player1 = True
            

system = Game()
system.init_game()
