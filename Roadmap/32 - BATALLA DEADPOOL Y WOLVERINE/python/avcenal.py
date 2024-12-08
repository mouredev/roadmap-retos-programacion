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
from abc import ABC,abstractmethod
from random import randint
from time import sleep,time
import logging

#Congiguración del nivel del log a mostrar
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s -- %(levelname)s: %(message)s",
                    datefmt="%d/%m/%Y - %H:%M:%S")

#decorador para mostrar que función se ha ejecutado y cuando
def time_decorator(function):
    def original_function(*args):
        result = function(*args)
        logging.debug(f"Se ha ejecutado la función \"{function.__name__}\"")
        return result
    return original_function

#CLASES ABSTRACTAS
class AbstractCharacter(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def attack(self):
        pass

#Clases de los personajes que heredan de la abstracta
class DeadPool(AbstractCharacter):
    def __init__(self,life:int = 0):
        self.name:str = "Deadpool"
        self.life:int = life
        self.strength:int = 100
        self.agility:int = 25

    @time_decorator
    def attack(self):
        return randint(10,self.strength) #random entre 10 y 100 para determinar el ataque de Deadpool
    
class Wolverine(AbstractCharacter):
    def __init__(self,life:int = 0 ):
        self.name:str = "Wolverine"
        self.life:int = life
        self.strength:int = 120
        self.agility:int = 20
    
    @time_decorator
    def attack(self):
        return randint(10,self.strength) #random entre 10 y 100 para determinar el ataque de Wolverine
    
#clase que engloba los métodos necesarios para ejecutar la batalla
class Battle():

    def set_life(self,fighter:AbstractCharacter): #para determinar la vida en la batalla de un personaje
        while True:
            try:
                life = int(input (f"Dime los puntos de vida de {fighter.name} por favor: "))
            except:
                logging.warning("El dato introducido no es un número") #se controla que se introduzca un número válido
                print("Parece que has introducido algo que no es un número...")
            else:
                if life <= 0:
                    logging.warning("El número es cero o menor que cero")
                    print("Por favor introduce un número positivo mayor que cero...")
                else:
                    fighter.life = life
                    break

    def __life_to_zero(self,fighter:AbstractCharacter): #Función privada que se encarga de cambiar la vida del personaje a 0 (solo en caso de que su vida baje de 0)
        fighter.life = 0

    def __hit(self,attacker:AbstractCharacter,defender:AbstractCharacter): #Función privada que ejecuta el golpe del atacante al defensor
        hit = attacker.attack()                                            # devuelve el entero del golpe para calcular después si es crítico o no
        print(f"{attacker.name.upper()} golpea a {defender.name}")                 # en la función principal
        dodge_chance = randint(0,100)
        if dodge_chance <= defender.agility:
            logging.info(f"** {defender.name.upper()} ESQUIVA **")
            print(f"{defender.name} esquiva el ataque")
            hit = 0 # al esquivar, el gole del atacante ha de ser 0 porque no ha impactado
        else:
            print(f"Y hace {hit} puntos de daño")
            defender.life -= hit
        return hit

    def battle(self,fighter_1:AbstractCharacter,fighter_2:AbstractCharacter,turn:int = 1): #función recursiva que recibe los dos atacantes y el turno (si no se recibe turno, se entiende que es el turno número 1)
        if fighter_1.life == 0:                             # caso base 1: el combatiente 1 no tiene vida
            logging.info(f"Gana el combate {fighter_2.name}")
            print(f"¡¡FIN DE LA PELEA!! El ganador es {fighter_2.name}\n".upper())
        elif fighter_2.life == 0:                           #caso base 2: el combatiente 2 no tiene vida
            logging.info(f"Gana el combate {fighter_1.name}")
            print(f"¡¡FIN DE LA PELEA!! El ganador es {fighter_1.name}\n".upper())
        else:                                               #si no es ningún caso base, se simula el turno
            print(f"--- TURNO {turn} ---")
            hit = self.__hit(fighter_1,fighter_2)
            if fighter_1.life <0: #con estos dos IF se controla que no aparezca ningún número negativo en el resultado de la vida de cada personaje
                self.__life_to_zero(fighter=fighter_1)
            if fighter_2.life <0:
                self.__life_to_zero(fighter=fighter_2)
            print(f"-- Vida restante de {fighter_1.name} {fighter_1.life}\n-- Vida restante de {fighter_2.name} {fighter_2.life}\n")
            turn += 1
            sleep(1)
            if hit == fighter_1.strength and fighter_2.life > 0:
                logging.info("** GOLPE CRÍTICO **")
                print(f"** Como ha sido un golpe crítico, {fighter_2.name} tiene que regenerarse y no puede atacar en el siguiente turno **\n")
                self.battle(fighter_1,fighter_2,turn)       #si es crítico se llama a la misma función respetando el mismo orden de los combatiente y no "pasa el turno"
            else:
                self.battle(fighter_2,fighter_1,turn)       #si no es crítico, se invierte el orden de los combatientes para que "pase el turno"

print("\nTe doy la bienvenida a la mas que esperada y ansiada pelea en la Tierra 10005 entre.... ¡¡¡¡DEADPOOL y WOLVERINE!!!\n")
wade_wilson = DeadPool()
logan = Wolverine()
battle = Battle()
battle.set_life(wade_wilson)
battle.set_life(logan)
logging.info("Comienza la pelea")
print("Todo listo... LFG!!\n")
sleep(1)
start_time = time()
battle.battle(wade_wilson,logan)
end_time = time()
logging.info(f"El combate ha durado {end_time-start_time:.4} segundos") # se muestra en el log cuántos segundos ha tardado en acabar la pelea
