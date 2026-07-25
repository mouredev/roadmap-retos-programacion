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

import random

class Luchador:
    def __init__(self, nombre, velocidad, ataque, defensa):
        self.nombre = nombre
        self.velocidad = velocidad
        self.ataque = ataque
        self.defensa = defensa
        self.salud = 100

    def esquivar(self):
        return random.random() < 0.2

    def recibir_danio(self, danio):
        if self.esquivar():
            print(f"{self.nombre} esquivó el ataque!")
            return

        if self.defensa > danio:
            danio *= 0.1
        else:
            danio -= self.defensa
        self.salud -= danio
        print(f"{self.nombre} recibe {danio} de daño. Salud actual: {self.salud}")

def batalla(luchador1, luchador2):
    print(f"¡{luchador1.nombre} vs {luchador2.nombre}!")

    while luchador1.salud > 0 and luchador2.salud > 0:
        if luchador1.velocidad >= luchador2.velocidad:
            luchador1, luchador2 = luchador1, luchador2
        else:
            luchador1, luchador2 = luchador2, luchador1

        luchador2.recibir_danio(luchador1.ataque)
        if luchador2.salud <= 0:
            print(f"¡{luchador1.nombre} gana!")
            return luchador1

        luchador1, luchador2 = luchador2, luchador1

def torneo(luchadores):
    if (len(luchadores) & (len(luchadores) - 1)) != 0:
        raise ValueError("El número de luchadores debe ser una potencia de 2")

    while len(luchadores) > 1:
        random.shuffle(luchadores)
        ganadores = []

        for i in range(0, len(luchadores), 2):
            ganador = batalla(luchadores[i], luchadores[i + 1])
            ganadores.append(ganador)

        luchadores = ganadores

    print(f"¡El ganador del torneo es {luchadores[0].nombre}!")

# Ejemplo de uso
luchadores = [
    Luchador("Goku", 90, 95, 85),
    Luchador("Vegeta", 85, 90, 90),
    Luchador("Piccolo", 75, 85, 95),
    Luchador("Gohan", 80, 80, 80),
]

torneo(luchadores)
