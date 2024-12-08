"""
/*
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
 */
"""

from __future__ import annotations
from random import random,randint
import math

class Luchador():
    def __init__(self,name:str,speed:float,attack:float,defense:float) -> None:
        self._name = name
        self._speed = speed
        self._attack = attack
        self._defense = defense
        self._health = 100
    
    #----Getters-----
    @property
    def name(self)->str:
        return self._name
    @property
    def speed(self)->float:
        return self._speed
    @property
    def attack(self)->float:
        return self._attack
    @property
    def defense(self)->float:
        return self._defense
    @property
    def health(self)->float:
        return self._health
    

    #----Setters----
    @name.setter
    def name(self,n_nombre:str)->None:
        self._name = n_nombre
    @speed.setter
    def speed(self,n_speed:float)->None:
        self._speed = n_speed
    @attack.setter
    def attack(self,n_attack:float)->None:
        self._attack = n_attack
    @defense.setter
    def defense(self,n_def:float)->None:
        self._defense = n_def
    @health.setter
    def health(self,n_health:float)->None:
        self._health = n_health
    

    def Atacar(self)->float:
        return self._attack
    

    def __str__(self)->str:
        return self._name

def atacar(atacante:Luchador,defensor:Luchador):
    miss = random()
    if miss <= 0.20:
        print(f"{atacante} falló el ataque")
        return defensor.health
    elif defensor.defense > atacante.attack:
        damage = 0.10 * atacante.attack
    else: damage = atacante.attack - defensor.defense
    
    defensor.health -= damage
    print(f"{defensor.name} recibio {damage} de daño, salud actual: {defensor.health}")
    return defensor.health

def Combate(luchador1:Luchador,luchador2:Luchador)->Luchador:

    print(f"{luchador1} vs {luchador2}")
    #Definir el primero en atacar
    #Reglas: Primero ataca el que más velocidad tenga, si tienen igual velocidad
    #voy a generar un número aleatorio entre 1 y 10, si el número <5 ataca primero el 1 y viceversa
    end = False
    coin = randint(1,10)
    
    if luchador1.speed > luchador2.speed or (luchador1.speed == luchador2.speed and coin <=5):
        while not end:
            luchador2.health = atacar(luchador1,luchador2)
            if luchador2.health <= 0:
                winner = luchador1
                break
            luchador1.health = atacar(luchador2,luchador1)
            if luchador1.health <= 0:
                winner = luchador2
                break
    else: 
        while not end:
            luchador1.health = atacar(luchador2,luchador1)
            if luchador1.health <= 0:
                winner = luchador2
                break
            luchador2.health = atacar(luchador1,luchador2)
            if luchador2.health <= 0:
                winner = luchador1
                break
    print(f"El ganador de la ronda es: {winner}")
    winner.health = 100
    return winner


def Torneo(Luchadores):

    end = False

    while not end:
        cant_luchadores = len(Luchadores)
        cant_grupos = math.log2(cant_luchadores)
        cursor = 0
        grupos = []
        winners = []
        for n in range(int(cant_grupos)):
            grupos.append([Luchadores[cursor],Luchadores[cursor+1]])
            cursor += 2
        for n in range(int(cant_grupos)):
            winners.append(Combate(grupos[n][0],grupos[n][1]))
        Luchadores = winners[::]
        if len(Luchadores) == 1:
            end = True
        

    
    print(f"El ganador del torneo es {Luchadores[0]}")

def main():
    
    fighter1 = Luchador("A",40,80,20)
    fighter2 = Luchador("B",70,90,10)
    fighter3 = Luchador("C",20,70,40)
    fighter4 = Luchador("D",50,50,50)
    pausa = input("pausa")
    Luchadores = [fighter1,fighter2,fighter3,fighter4]

    Torneo(Luchadores)



if __name__ == '__main__':
    main()
