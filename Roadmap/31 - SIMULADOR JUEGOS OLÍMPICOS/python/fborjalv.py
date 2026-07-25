"""
/*
 * EJERCICIO:
 * ¡Los JJOO de París 2024 han comenzado!
 * Crea un programa que simule la celebración de los juegos.
 * El programa debe permitir al usuario registrar eventos y participantes,
 * realizar la simulación de los eventos asignando posiciones de manera aleatoria
 * y generar un informe final. Todo ello por terminal.
 * Requisitos:
 * 1. Registrar eventos deportivos. ✅
 * 2. Registrar participantes por nombre y país. ✅
 * 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3). ✅
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

"""
-- registrar eventos deportivos
-- registrar participante por nombre y pais 
-- simular eventos
-- asignar medallas 

"""

from abc import ABC, abstractmethod



import random


class OlympicsGames():

    def __init__(self) -> None:
        self.participant_registry = ParticipantRegistry()
        self.event_registry = EventRegistry()
        self.my_report = Report()

    def show_menu(self):
        while True:
            print("-- Menú principal --")
            print("1. Registro de eventos")
            print("2. Registro de participantes.")
            print("3. Simulación de eventos.")
            print("4. Creación de informes.")
            print("5. Salir del programa.")
            option = input("Introduce una opción: ")

            match option:
                case "1":
                    print("Registro de eventos")
                    name = input("Introduce el nombre del evento: ")
                    event = Event(name)
                    self.event_registry.add_event(event)

                case "2":
                    print("Registro de participantes")
                    name = input("Introduce el nombre del deporista: ")
                    country = input("Introduce el país al que representa: ")
                    deportist = Participant(name, country)
                    self.participant_registry.add_participant(deportist)

                case "3":
                    print("Simulación de eventos")
                    self.participant_registry.show_participant()
                    self.event_registry.show_events()
                    event.simulation(self.participant_registry.list_participant)
                    print(event.result)
                    event.award_medals(self.participant_registry.list_participant)
                    self.participant_registry.show_participant()
                case "4":
                    print("Creación de informes")
                    self.my_report.show_winners_by_event(self.event_registry)
                    self.my_report.show_ranking_by_country(self.participant_registry)
                case "5":
                    print("Saliendo del programa")
                    break

class Participant():
    
    def __init__(self, name, country) -> None:
        self.name = name
        self.country = country
        self.medals = {"GOLD": 0, "SILVER": 0, "BRONZE": 0}

class ParticipantRegistry(OlympicsGames):
    def __init__(self) -> None:
        self.list_participant = []
    def add_participant(self, Participant):
        self.list_participant.append(Participant)
    def show_participant(self):
        for participant in self.list_participant:
            print(f"Nombre: {participant.name},  Pais: {participant.country}, Medallas: {participant.medals}")

class Event():

    result = {}
    def __init__(self, sport_name) -> None:
        self.sport_name = sport_name

    def simulation(self, participant_list: list):
        if len(participant_list) < 3:
            print("El Evento no se puede realizar por falta de participantes")
        else: 
            self.result["sport"] = self.sport_name
            winners = random.sample(participant_list, k=3)
            self.result["winners"] = {"GOLD": winners[0].name, "SILVER": winners[1].name, "BRONZE":winners[2].name}

    def award_medals(self, participant_list):
        for medal, name in self.result["winners"].items():
            for participant in participant_list:
                if participant.name == name:
                    participant.medals[medal] += 1
                    break

class EventRegistry(OlympicsGames):

    def __init__(self) -> None:
        self.event_list = []
    def add_event(self, event):
        self.event_list.append(event)
    def show_events(self):
        for event in self.event_list:
            print(f"Nombre del evento: {event.sport_name}")


class Report():

    def __init__(self) -> None:
        pass

    def show_winners_by_event(self, event_registry):
        for event in event_registry.event_list:
            print(f"Deporte: {event.result['sport']}")
            print("; ".join([str(f"{medal, winner}") for medal, winner in event.result['winners'].items()]))

    def show_ranking_by_country(self, participant_registry):
        country_medals = {}
        for participant in participant_registry.list_participant:
            if participant.country not in country_medals:
                country_medals[participant.country] = 0
            country_medals[participant.country] += sum(participant.medals.values())
        print(country_medals)

sistem = OlympicsGames()
sistem.show_menu()