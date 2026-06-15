'''
Ejercicio:

Simula un Torneo de Artes Marciales, al mas puro estilo de la saga, donde participaran
diferentes luchadores, y el sistema decidira quien es el ganador.

Luchadores: 
    * Nombre.
    * Tres atributos: velocidad, ataque, defensa
    (con valores 0 a 100 que tu decidiras).
    * Comienza cada batalla con 100 de salud.

Batalla: 
    * En cada batalla se enfrentan 2 luchadores.
    * El luchador con mas velocidad comienza atacando.
    * El daño se calcula restando el daño de ataque del atacante menos la defensa del oponente.
    * El oponente siempre tiene un 20% de posibilidad de esquivar el ataque.
    * Si la defensa es mayor que el ataque, recibe 10% del daño de ataque.
    * Despues de cada turno y ataque, el oponente pierde su salud.
    * La batalla finaliza cuando un luchador pierde toda su salud.

Torneo:
    * Un torneo solo es valido con un numero de luchadores potencia de 2.
    * El torneo debe crear parejas al azar en cada ronda.
    * Los luchadores se enfrentan en rondas eliminatorias.
    * El ganador avanza a la siguiente ronda hasta que solo quede uno.
    * Debes demostrar por consola todo lo que sucede en el torneo, asi como el ganador.
'''

import random

class Luchador:
    def __init__(self, nombre, velocidad, ataque, defensa):
        self.nombre = nombre
        self.velocidad = velocidad
        self.ataque = ataque
        self.defensa = defensa
        self.salud = 100

    def esquivar(self):
        return random.random() < 0.20

class Batalla:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def iniciar(self):
        if self.l1.velocidad > self.l2.velocidad: 
            atacante = self.l1
            defensor = self.l2
        elif self.l2.velocidad > self.l1.velocidad:
            atacante = self.l2
            defensor = self.l1
        else:
            atacante = random.choice([self.l1, self.l2])
            defensor = self.l1 if atacante is self.l2 else self.l2
        
        while atacante.salud > 0 and defensor.salud > 0:
            print(f"--- Inicia el combate ---")

            self.realizar_ataque(atacante, defensor)
            if defensor.salud <= 0:
                ganador = atacante
                return ganador
                
            atacante, defensor = defensor, atacante

    def realizar_ataque(self, atq, df):
        # Primero revisamos si el defensor esquiva el ataque
        if df.esquivar():
            print(f"{df.nombre} ha esquivado el ataque de {atq.nombre}")
            return
        
        # Calculamos el daño: base = ataque - defensa
        base = atq.ataque - df.defensa

        if base <= 0:
            # Defensa mayor al ataque -> recibe un 10 porciento del ataque
            ataque_final = atq.ataque * 0.10
        else:
            ataque_final = base

        # Aplicamos el daño
        df.salud -= ataque_final
        df.salud = max(0, df.salud)

        print(f"{atq.nombre} ataca a {df.nombre} causando {ataque_final} de daño. Salud restante de {df.nombre}: {df.salud}")

def torneo():
    # Creamos una lista para almacenar los luchadores
    luchadores = []

    n_luchadores = int(input("Inserta un numero de luchadores que sea multiplo de 2: "))
    if n_luchadores > 0 and (n_luchadores & (n_luchadores - 1)) == 0:
        print("Numero valido de luchadores valido")
    else: 
        print("Debe ser potencia de 2.")
        return

    for _ in range(n_luchadores):
        nombre_luchador = input("Inserte el nombre del luchador: ")
        velocidad_luchador = int(input("Inserte la velocidad del luchador: (0 - 100)"))
        ataque_luchador = int(input("Inserte el ataque del luchador: (0 - 100)"))
        defensa_luchador = int(input("Inserte la defensa del luchador: (0 - 100)"))

        if all(0 <= x <= 100 for x in [velocidad_luchador, ataque_luchador, defensa_luchador]):
            luchador = Luchador(nombre_luchador, velocidad_luchador, ataque_luchador, defensa_luchador)    
            luchadores.append(luchador)
        else:
            print(f"Alguno de los valores se salen del rango.") 

    while len(luchadores) > 1:
        print(f"\n--- Nueva ronda con {len(luchadores)} luchadores ---")
        random.shuffle(luchadores)
        ganadores = []

        for i in range(0, len(luchadores), 2):
            print(f"\nBatalla: {luchadores[i].nombre} vs {luchadores[i + 1].nombre}")
            ganador = Batalla(luchadores[i], luchadores[i + 1]).iniciar()
            print(f"Ganador: {ganador.nombre}")
            ganadores.append(ganador)

        luchadores = ganadores

    print(f"\nEl campeon del torneo es: {luchadores[0].nombre}")