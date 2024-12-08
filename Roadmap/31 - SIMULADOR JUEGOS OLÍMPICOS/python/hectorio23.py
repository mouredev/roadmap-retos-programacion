# Autor:  Héctor Adán
# GitHub: https://github.com/hectorio23

from collections import defaultdict
import random

'''
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
'''

class Participant:
    def __init__(self, name, country):
        self.name = name
        self.country = country

class Event:
    def __init__(self, name):
        self.name = name
        self.participants = []

class OlympicGames:
    def __init__(self):
        self.events = []
        self.medal_tally = defaultdict(int)

    def register_event(self):
        event_name = input("Ingrese el nombre del evento: ")
        self.events.append(Event(event_name))

    def register_participant(self):
        event_name = input("Ingrese el nombre del evento: ")
        event = next((e for e in self.events if e.name == event_name), None)

        if event:
            participant_name = input("Ingrese el nombre del participante: ")
            country = input("Ingrese el país del participante: ")
            event.participants.append(Participant(participant_name, country))
        else:
            print("Evento no encontrado.")

    def simulate_event(self):
        for event in self.events:
            if len(event.participants) >= 3:
                participants = event.participants[:]
                random.shuffle(participants)

                print(f"Resultados del evento {event.name}:")
                print(f"Oro: {participants[0].name} ({participants[0].country})")
                print(f"Plata: {participants[1].name} ({participants[1].country})")
                print(f"Bronce: {participants[2].name} ({participants[2].country})")

                self.medal_tally[participants[0].country] += 3
                self.medal_tally[participants[1].country] += 2
                self.medal_tally[participants[2].country] += 1
            else:
                print(f"El evento {event.name} no tiene suficientes participantes.")

    def display_medal_tally(self):
        print("\nRanking de Medallas por País:")
        for country, points in sorted(self.medal_tally.items(), key=lambda x: x[1], reverse=True):
            print(f"{country}: {points} puntos")

    def run(self):
        while True:
            print("\n1. Registro de eventos\n2. Registro de participantes\n3. Simulación de eventos\n4. Creación de informes\n5. Salir")
            option = int(input("Seleccione una opción: "))

            if option == 1:
                self.register_event()
            elif option == 2:
                self.register_participant()
            elif option == 3:
                self.simulate_event()
            elif option == 4:
                self.display_medal_tally()
            elif option == 5:
                break
            else:
                print("Opción inválida.")

if __name__ == "__main__":
    OlympicGames().run()
