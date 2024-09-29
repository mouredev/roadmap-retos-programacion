# #31 SIMULADOR JUEGOS OLÍMPICOS
## Ejercicio

"""
/*
 * EJERCICIO:
 * ¡Los JJOO de París 2024 han comenzado!
 * Crea un programa que simule la celebración de los juegos.
 * El programa debe permitir al usuario registrar eventos y participantes,
 * realizar la simulación de los eventos asignando posiciones de manera aleatoria
 * y generar un informe final. Todo ello por terminal.
 * Requisitos:
 * 1. Registrar eventos deportivos.
 * 2. Registrar participantes por nombre y país.
 * 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
 * 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
 * 5. Mostrar los ganadores por cada evento.
 * 6. Mostrar el ranking de países según el número de medallas.
 * Acciones:
 * 1. Registro de eventos.
 * 2. Registro de participantes.
 * 3. Simulación de eventos.
 * 4. Creación de informes.
 * 5. Salir del programa.
 */
"""

import random
import time


# Clase Registro
class Registro:
    participantes: dict = {}

    def __init__(self, nombre: str, pais: str):
        self.nombre: str = nombre
        self.pais: str = pais

    def agregar_participantes(self):
        self.participantes[self.nombre] = self.pais

# Clase Evento
class Evento:
    juegos: list = []

    def __init__(self, nombre_evento: str):
        self.nombre_evento = nombre_evento

    def agregar_evento(self):
        self.juegos.append(self.nombre_evento)

# Clase Simulador
class Simulador:
    def resultados(self, participantes: Registro) -> list:
        # Obtenemos los participantes (nombres y países)
        resultado: dict = participantes.participantes

        # Mezclamos a los participantes para simular resultados
        participantes_list = list(resultado.keys())  # Lista de nombres de personas
        random.shuffle(participantes_list)  # Mezcla aleatoria de los participantes

        # Mostramos los ganadores por persona (simulación)
        print(f"Ganadores del evento (persona): {participantes_list[:3]}\n")

        # Retornamos los países de los ganadores
        return [resultado[participante] for participante in participantes_list[:3]]

# Clase Informes
class Informes:
    medalla_oro: dict = {}
    medalla_plata: dict = {}
    medalla_bronce: dict = {}

    def informe(self, pais: list):
        # Asignamos medallas dependiendo de la cantidad de ganadores
        if len(pais) >= 1:
            if pais[0] in self.medalla_oro:
                self.medalla_oro[pais[0]] += 1
            else:
                self.medalla_oro[pais[0]] = 1

        if len(pais) >= 2:
            if pais[1] in self.medalla_plata:
                self.medalla_plata[pais[1]] += 1
            else:
                self.medalla_plata[pais[1]] = 1

        if len(pais) >= 3:
            if pais[2] in self.medalla_bronce:
                self.medalla_bronce[pais[2]] += 1
            else:
                self.medalla_bronce[pais[2]] = 1

    def mostrar_informe(self):
        # Imprimir informe de medallas por país
        print("*ORO*")
        for pais, cantidad in self.medalla_oro.items():
            print(f"{pais}: {cantidad} medallas de oro")
            time.sleep(0.2)

        print("\n*PLATA*")
        for pais, cantidad in self.medalla_plata.items():
            print(f"{pais}: {cantidad} medallas de plata")
            time.sleep(0.2)

        print("\n*BRONCE*")
        for pais, cantidad in self.medalla_bronce.items():
            print(f"{pais}: {cantidad} medallas de bronce")
            time.sleep(0.2)

        print("")


# Simulación del proceso
if __name__ == "__main__":
    # Crear registro de participantes
    registro1 = Registro("Juan", "Argentina")
    registro1.agregar_participantes()

    registro2 = Registro("Pedro", "Brasil")
    registro2.agregar_participantes()

    registro3 = Registro("Maria", "Colombia")
    registro3.agregar_participantes()

    registro4 = Registro("Ana", "Chile")
    registro4.agregar_participantes()

    registro5 = Registro("Luis", "Perú")
    registro5.agregar_participantes()

    # Crear el informe para almacenar los resultados generales
    informes = Informes()

    # Lista de eventos con el número de ganadores en cada uno
    eventos = ["Natación", "Atletismo", "Gimnasia","Velocidad","Salto"]

    # Crear simulador de eventos
    simulador = Simulador()

    # Simular los resultados de cada evento
    for nombre_evento in eventos:
        evento = Evento(nombre_evento)
        evento.agregar_evento()

        print(f"Simulando evento: {nombre_evento}")
        paises_ganadores = simulador.resultados(Registro)  # Obtiene los países ganadores

        # Pasar los resultados de este evento al informe
        informes.informe(paises_ganadores)
        time.sleep(0.4)

    # Mostrar informe final de medallas por país
    informes.mostrar_informe()
