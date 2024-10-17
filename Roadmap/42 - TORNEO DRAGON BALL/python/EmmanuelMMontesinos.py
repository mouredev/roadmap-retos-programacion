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

import random

class Luchador:
    def __init__(self, nombre, velocidad, ataque, defensa):
        self.nombre = nombre
        self.velocidad = velocidad
        self.ataque = ataque
        self.defensa = defensa
        self.salud = 100
        self.descripcion_ataque = [
            "Patada Baja",
            "Patada Media",
            "Patada Alta",
            "Golpe Lateral",
            "Puñetazo",
            "Rafaga de Golpes",
            "Bola de Ki",
            "Tactica especial",
        ]

    def __str__(self) -> str:
        return f"{self.nombre} - Salud: {self.salud}\n(Velocidad: {self.velocidad}, Ataque: {self.ataque}, Defensa: {self.defensa})"

    def atacar(self, oponente):
        if random.randint(1,101) < 20:
            print(f"{oponente.nombre} esquiva el ataque de {self.nombre}")
        else:
            if self.ataque > oponente.defensa:
                damage = self.ataque - oponente.defensa
                oponente.salud -= damage
            
            else:
                print(f"{oponente.nombre} ha recibido 10% de daño")
                damage = self.ataque * 0.1
                oponente.salud -= damage
        
            print(f"{oponente.nombre} ha recibido {damage} de daño por {random.choice(self.descripcion_ataque)} de {self.nombre}\n")
    

class Torneo:

    def __init__(self,lista_luchadores):
        random.shuffle(lista_luchadores)
        self.lista_luchadores = lista_luchadores
        self.nombre = " Torneo Dragon Ball: Sparking! ZERO"
        self.edicion = 1
        self.grupo_1 = []
        self.grupo_2 = []
        self.eliminados = []
        self.ganadores = {}
        self.rondas = {
            1: "Final",
            2: "Semifinal",
            4: "Cuartos de final",
            8: "Octavos de final",
        }
    def __str__(self) -> str:
        return f"{self.nombre} - Edicion: {self.edicion}\nLuchadores inscritos: {len(self.lista_luchadores)}\n{[luchador.nombre for luchador in self.lista_luchadores]}"

    def iniciar_torneo(self):
        num_luchadores = len(self.lista_luchadores)

        if num_luchadores % 2 == 0:
            print("-"*20)
            print("Iniciando torneo...")

            if num_luchadores > 16:
                print("Hay demasiados luchadores, solo son seleccionados los primeros 16 inscritos.")
                self.lista_luchadores = self.lista_luchadores[:15]
            elif num_luchadores <= 0:
                print("No hay luchadores inscritos")
                return False

            

            for luchador in range(0, len(self.lista_luchadores), 2):
                self.grupo_1.append(self.lista_luchadores[luchador])
                self.grupo_2.append(self.lista_luchadores[luchador+1])

            print()
            print(f"Grupo 1: {[luchador.nombre for luchador in self.grupo_1]}")
            print("-"*20)
            print(f"Grupo 2: {[luchador.nombre for luchador in self.grupo_2]}\n")

            self.bucle()
    def ronda(self, grupo, nombre_grupo):
        clase_ronda = self.rondas[len(grupo)] if nombre_grupo != 'Finalistas' else 'Final'
        grupo_ronda = grupo.copy()
        random.shuffle(grupo_ronda)
        print(nombre_grupo)
        for luchador in range(0, len(grupo_ronda), 2):
            luchador_1 = grupo[luchador]
            luchador_2 = grupo[luchador+1]
            primero, segundo = (luchador_1, luchador_2) if luchador_1.velocidad > luchador_2.velocidad else (luchador_2, luchador_1)

            print(f"{primero.nombre} vs. {segundo.nombre}")
            print("-"*20)

            ronda = 0
            while primero.salud >= 1 and segundo.salud >= 1:
                ronda += 1
                print("-"*20)
                print(f"Ronda: {ronda}")
                print(f"Vida de {luchador_1.nombre}: {luchador_1.salud} | Velocidad: {luchador_1.velocidad} | Ataque: {luchador_1.ataque} | Defensa: {luchador_1.defensa}") 
                print(f"Vida de {luchador_2.nombre}: {luchador_2.salud} | Velocidad: {luchador_2.velocidad} | Ataque: {luchador_2.ataque} | Defensa: {luchador_2.defensa}\n")
                primero.atacar(segundo)
                if segundo.salud <= 0:
                    break
                segundo.atacar(primero)
                print(f"Vida de {luchador_1.nombre}: {luchador_1.salud}")
                print(f"Vida de {luchador_2.nombre}: {luchador_2.salud}\n")

            perdedor = luchador_1 if luchador_1.salud < luchador_2.salud else luchador_2
            ganador = luchador_1 if luchador_1.salud > luchador_2.salud else luchador_2
            print(f"{ganador.nombre} ha ganado la pelea de {clase_ronda} del {nombre_grupo}")
            self.eliminados.append(perdedor)
            grupo_ronda.remove(perdedor)
            
        return grupo_ronda

    def bucle(self):
        while len(self.grupo_1) >= 2 and len(self.grupo_2) >= 2:
            print("-"*20)
            print(f"Ronda: {self.rondas[len(self.grupo_1)]}\n")
            
            self.grupo_1 = self.ronda(self.grupo_1, "Grupo 1")
            self.grupo_2 = self.ronda(self.grupo_2, "Grupo 2")
            print("-"*20)
            print(f"Clasificando Grupo 1: {[luchador.nombre for luchador in self.grupo_1]}")
            print(f"Clasificando Grupo 2: {[luchador.nombre for luchador in self.grupo_2]}")
            print(f"Eliminados: {[luchador.nombre for luchador in self.eliminados]}\n")
            print("-"*20)

        print(f"Combate final entre {self.grupo_1[0].nombre} y {self.grupo_2[0].nombre}")
        finalistas = [self.grupo_1[0], self.grupo_2[0]]
        self.ronda(finalistas, "Finalistas")
        print("-"*20)
        print(f"El ganador del torneo nº {self.edicion} es: {finalistas[0].nombre}")
        self.ganadores[self.edicion] = finalistas[0].nombre
        self.edicion += 1


            

# Prueba
goku = Luchador("Goku", 100, 100, 100)
gohan = Luchador("Gohan", 90, 90, 90)
vegeta = Luchador("Vegeta", 80, 80, 80)
picolo = Luchador("Picolo", 70, 70, 70)
yamcha = Luchador("Yamcha", 60, 60, 60)
krilin = Luchador("Krilin", 50, 50, 50)
freezer = Luchador("Freezer", 40, 40, 40)
cell = Luchador("Cell", 30, 30, 30)

print(goku)
print(gohan)
print(vegeta)
print(picolo)

torneo = Torneo([goku, gohan, vegeta, picolo, yamcha, krilin, freezer, cell])
print(torneo)

torneo.iniciar_torneo()