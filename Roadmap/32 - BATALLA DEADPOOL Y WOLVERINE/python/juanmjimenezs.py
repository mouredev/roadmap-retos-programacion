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

from random import randint
import time

class Character:
    def __init__(self, name, live_points, max_damage, evasion):
        self.name = name
        self.live_points = live_points
        self.max_damage = max_damage
        self.evasion = evasion

    def attack(self, target):
        time.sleep(1)
        damage = randint(10, self.max_damage)
        print(f"{self.name} ataca a {target.name} con un daño potencial de {damage} puntos.")
        target.take_damage(damage)
    
    def take_damage(self, damage):
        if randint(0, 100) > self.evasion * 100:
            self.live_points -= damage
            print(f"{self.name} recibe {damage} puntos de daño.")
        else:
            print(f"{self.name} esquiva el ataque.")

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turn = 1

    def play(self):
        while self.player1.live_points > 0 and self.player2.live_points > 0:
            print(f"Turno {self.turn}")
            self.player1.attack(self.player2)
            if self.player2.live_points > 0:
                self.player2.attack(self.player1)
            self.display_status()
            self.turn += 1

    def display_status(self):
        print(f"{self.player1.name}: {self.player1.live_points} puntos de vida")
        print(f"{self.player2.name}: {self.player2.live_points} puntos de vida")

        if self.player1.live_points <= 0 or self.player2.live_points <= 0:
            if self.player1.live_points <= 0 and self.player2.live_points <= 0:
                print("Ambos jugadores han muerto.")
            elif self.player1.live_points <= 0:
                print(f"{self.player1.name} ha muerto.")
            elif self.player2.live_points <= 0:
                print(f"{self.player2.name} ha muerto.")


print("Esta es la épica batalla entre Deadpool y Wolverine!")
# Asking for Deadpool life score
deadpool_live_points = int(input("Por favor, ingresa los puntos de vida para Deadpool: "))
# Asking for Wolverine life score
wolverine_live_points = int(input("Por favor, ingresa los puntos de vida para Wolverine: "))

# Creating characters
deadpool = Character("Deadpool", deadpool_live_points, 100, 0.25)
wolverine = Character("Wolverine", wolverine_live_points, 120, 0.20)
game = Game(deadpool, wolverine)
game.play()
print("¡El combate ha terminado!")
