"""
/*
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
 */
"""
from random import randint,choice
import time

# Descripciones de los ataques
DESCRIPTION_DAMAGE_DEADPOOL = ["Puñetazo en la cara",
                            "Patada en la entrepierna",
                            "Nalgada Cariñosa",
                            "Katanazo en el pecho",
                            "Salto con doble tirabuzon en la rodilla"
                            ]
DESCRIPTION_DAMAGE_WOLVERINE = ["Cabezazo",
                                "Ataque de garras de Adamantium",
                                "Lanzamiento de Puro a los ojos",
                                "Puñetazo al higado"]

# Clase para los Deadpoll y Wolverine
class SuperHero:
    def __init__(self,nombre,vida,damage_max,agilidad,descriptions) -> None:
        self.nombre = nombre
        self.vida = vida
        self.damage_max = damage_max
        self.agilidad = agilidad
        self.is_shock = False
        self.descriptions = descriptions

    def ataque(self,enemigo):

        if not self.is_shock:
            damage_turn = randint(10,self.damage_max+1)
            turno = f"Turno de {self.nombre}:"
            
            if not enemigo.esquivar():
                enemigo.vida -= damage_turn
                
                if enemigo.vida < 0:
                    enemigo.vida = 0
                turno += f"{choice(self.descriptions)} y le hace {damage_turn} puntos de daño\n"

                if damage_turn == self.damage_max:
                    enemigo.shock = True
                    turno += f"{enemigo.nombre} esta en shock por ataque CRITICO!!!"

            else:
                turno += f"{enemigo.nombre} ha esquivado el ataque"

            print(turno)
            print(f"Vida de {enemigo.nombre}: {enemigo.vida}")

        else:
            self.is_shock = False
            print(f"{self.nombre} se esta regenerando")
        print()


    def esquivar(self):
        if randint(1,101) <= self.agilidad:
            return True
        else:
            return False 

# Clase para simular los turnos
class Combate:
    def __init__(self,vida_dead, vida_wolve) -> None:
        self.deadpool = SuperHero("Deadpool",vida_dead,100,25,DESCRIPTION_DAMAGE_DEADPOOL)
        self.wolverine = SuperHero("Wolverine", vida_wolve,120,20,DESCRIPTION_DAMAGE_WOLVERINE)
        self.n_turno = 1


    def combate(self):
        print(f"Inicio del Turno nº {self.n_turno}")
        self.deadpool.ataque(self.wolverine)
        if self.wolverine.vida > 0:
            self.wolverine.ataque(self.deadpool)
        print(f"Fin del Turno nº {self.n_turno}\n")
        time.sleep(1)
        if self.deadpool.vida <= 0 or self.wolverine.vida <= 0:
            if self.deadpool.vida == 0:
                self.ganador = self.wolverine.nombre.title()
            else:
                self.ganador = self.deadpool.nombre.title()
            return False
        else:
            self.n_turno += 1
            return True
        
    def bucle(self):
        check = True
        while check:
            check = self.combate()
        print("Combate Terminado:")
        print(f"Vida de Deadpool: {self.deadpool.vida}")
        print(f"Vida de Wolverine: {self.wolverine.vida}")
        print(f"El ganador del Combate Moure en el turno nº {self.n_turno} es: {self.ganador}")

# Prueba
vida_dead = int(input("Indique la vida de Deadpool: "))
vida_wolve = int(input("Indique la vida de Wolverine: "))

simulacion = Combate(vida_dead,vida_wolve)
simulacion.bucle()