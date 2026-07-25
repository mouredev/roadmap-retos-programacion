'''
Ejercicio:
Crea un programa que simule una pelea y determine un ganador.

El programa simula un combate por turnos, donde cada protagonista posee unos puntos de vida iniciales, un daño de ataque variable y diferentes cualidades de regeneracion y evasion de ataques.

Requisitos:
    1. El usuario debe determinar la vida inicial de cada protagonista.
    2. Cada personaje puede impartir un daño aleatorio:
        * Deadpool: Entre 10 y 100.
        * Wolverine: Entre 10 y 120.
    3. Si el daño es el maximo, el personaje que lo recibe no ataca en el siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
    4. Cada personaje puede evitar el ataque contrario:
        * Deadpool: 25% de posibilidades.
        * Wolverine: 20% de posibilidades.
    5. Un personaje pierde sus sus puntos de vida llegan a cero o menos.

Acciones: 
    1. Simula una batalla.
    2. Muestra el numero del turno (pausa de 1 segundo entre turnos).
    3. Muestra que pasa en cada turno.
    4. Muestra la vida en cada turno.
    5. Muestra el resultado final.
'''

import random
import time

class Protagonista:
    def __init__(self, nombre, vida_inicial):
        self.nombre = nombre
        self.vida = vida_inicial
        self.regenerando = False

    def atacar(self):
        pass

    def esquivar(self):
        pass

# Creamos las clases concretas
class Deadpool(Protagonista):
    def __init__(self, vida_inicial):
        super().__init__("Deadpool", vida_inicial)

    def atacar(self):
        return random.randint(10, 100)
    
    def esquivar(self):
        return random.random() < 0.25 # 25% de probabilidades
    
class Wolverine(Protagonista):
    def __init__(self, vida_inicial):
        super().__init__("Wolverine", vida_inicial)

    def atacar(self):
        return random.randint(10, 120)
    
    def esquivar(self):
        return random.random() < 0.20 # 20% de probabilidades
    
# Creamos la clase que tendra la responsabilidad de los turnos

class Batalla:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.turno = 1

    def iniciar(self):
        while self.p1.vida > 0 and self.p2.vida > 0:
            print(f"\n --- Turno {self.turno} ---")


            self.realizar_turno(self.p1, self.p2)
            if self.p2.vida <= 0:
                break

            self.realizar_turno(self.p2, self.p1)
            self.turno += 1
            time.sleep(1)

        ganador = self.p1 if self.p1.vida > 0 else self.p2
        print(f"\n {ganador.nombre} ha ganado la batalla!")

    def realizar_turno(self, atacante, defensor):
        if atacante.regenerando:
            print(f"{atacante.nombre} esta regenerando y no atacara este turno.")
            atacante.regenerando = False
            return
        
        if defensor.esquivar():
            print(f"{defensor.nombre} esquiva el ataque de {atacante.nombre}!")
            return
        
        ataque = atacante.atacar()
        print(f"{atacante.nombre} ataca a {defensor.nombre} causando {ataque} de daño.")
        defensor.vida -= ataque
        print(f"Vida restante: {defensor.nombre}: {defensor.vida}, {atacante.nombre}: {atacante.vida}")

        # Si el daño es maximo, el defensor se regenera y no ataca el siguiente turno
        max_daño = 100 if isinstance(atacante, Deadpool) else 120
        if ataque == max_daño:
            defensor.regenerando = True
            print(f"{defensor.nombre} recibio daño maximo y debe regenerarse el siguiente turno.")

def main():
    print("Por favor ingrese la vida de los personajes: ")
    v1 = int(input(""))
    v2 = int(input(""))

    # Creamos los personajes con la vida
    p1 = Deadpool(v1)
    p2 = Wolverine(v2)

    # Le preguntamos al usuario si desea iniciar la batalla
    iniciar = input("Desea iniciar la pelea (y/n): ").lower().strip()
    if iniciar == "y":
        control = Batalla(p1, p2)
        control.iniciar()
    else:
        print("Has cancelado la batalla")
    
main()