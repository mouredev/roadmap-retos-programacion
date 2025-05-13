"""
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
"""
from enum import Enum
from abc import ABC, abstractmethod
import random
#from uuid import uuid4 Se utiliza para obtener calves unitarias. Al final no lo use.

# Enumeración que representa los países posibles en los eventos.
class Country(Enum):
    SPAIN = 1
    GERMANY = 2
    EEUU = 3
    RUSSLAND = 4
    CHINA = 5
    FRANCE = 6
    ITALY = 7
    UK = 8
    CANADA = 9
    PORTUGAL = 10
    CHILE = 11
    ARGENTINA = 12

# Enumeración que representa las medallas posibles en los eventos.
class Medals(Enum):
    GOLD = 0
    SILVER = 1
    BRONZE = 2

# Clase que representa un evento en los Juegos Olímpicos.
class Event:
    def __init__(self, name: str):
        self.name = name
        self.participants = [] # Lista de participantes en el evento.
        self.finished = False # Estado del evento: si ya se ha finalizado o no.
        self.standings = [] # Los puestos (ganadores) del evento.

    # Comparación de eventos por nombre (para evitar duplicados).
    def __eq__(self, other):
        return self.name == other.name
    
    # Se sobrecarga el hash para que los eventos puedan ser usados en conjuntos o diccionarios.
    def __hash__(self):
        return hash((self.name))


# Clase que gestiona los eventos (registro de eventos).
class EventsManager:
    def __init__(self):
        self.events = [] # Lista de todos los eventos registrados.

    def register_event(self, event: Event):
        if event not in self.events:
            self.events.append(event)
        else:
            print("El evento ya esta registrado.")

# Clase que representa a un participante en un evento.
class Participant:
    def __init__(self, name: str, country: Country):
        self.name = name
        self.country = country

    def __eq__(self, other):
        return (self.name == other.name and self.country == other.country)
    
    def __hash__(self):
        return hash((self.name, self.country))
    


# Clase encargada de generar los informes de los eventos y países.
class ReportManager:
    def __init__(self):
        self.event_winners = {} # Almacena los ganadores de cada evento.
        self.country_winners ={} # Almacena las victorias por país.

    def add_event_winners(self, event: Event):
        self.event_winners[event] = event.standings[0:3]

    def add_country_winners(self):
        for event, winners in self.event_winners.items():
            for index, participant in enumerate(winners):
                if participant.country not in self.country_winners:
                    self.country_winners[participant.country] = [0,0,0]
                self.country_winners[participant.country][index] += 1


# Interfaz abstracta para las opciones del menú (patrón de diseño Command).
class OptionInterface(ABC):
    @abstractmethod
    def execute(self):
        pass

# Clase que implementa la opción de registrar un evento.
class EventRegistry(OptionInterface):
    def execute(self, events_manager):
        event_name = input("Introduce el nombre del evento: ").lower()
        event = Event(event_name)
        if event not in events_manager.events:
            events_manager.register_event(event)
        else:
            print("El evento ya esta registrado.")

# Clase que implementa la opción de registrar un participante en un evento.
class ParticipantRegistry(OptionInterface):

    #Comprueba si hay al menos un evento diponible.
    def available_events(self, events_manager: EventsManager) -> bool:
        for event in events_manager.events:
            if not event.finished:
                return True
        return False
    
    def execute(self, events_manager):
        if len(events_manager.events) > 0 and self.available_events(events_manager):
            while True:
                print("Eventos diponibles:")
                for index, event in enumerate(events_manager.events):
                    if not event.finished:
                        print(f"\t {index + 1}.- {event.name}")
                try:
                    event_option = int(input("Introduce el número del evento donde quieres registrar al participante: "))
                    if event_option <=0 or event_option > len(events_manager.events) or events_manager.events[event_option -1].finished:
                        raise ValueError
                    break
                except ValueError:
                    print("Introduce una opcion correcta.")
                    continue
            event = events_manager.events[event_option - 1]
            while True:
                participant_name = input("Introduce el nombre del participante: ").lower()
                if participant_name:
                    break
                else:
                    print("Debes introducir un nombre. No dejes el campo vacío.")
            print("Países disponibles:")
            for country in Country:
                print(f"- {country.name.capitalize()}")
            while True:
                participant_country = input("Introduce el pais del participante: ").upper()
                try:
                    country_enum = Country[participant_country]
                    break
                except KeyError:
                    print("País incorrecto, inténtalo de nuevo.")
            participant = Participant(participant_name, country_enum)
            if participant not in event.participants:
                event.participants.append(participant)
            else:
                print(f"El participante {participant.name.capitalize()} de {participant.country.name} ya esta registrado en el evento '{event.name}'")
        else:
            print("No hay eventos disponibles. Registra primero un evento para poder registrar participantes.")


# Clase que simula la realización de los eventos.
class SimulateEvents(OptionInterface):
    def execute(self, events_manager):
        for event in events_manager.events:
            if not event.finished:
                if  len(event.participants) >= 3:
                    shuffled = event.participants[:] # Crea una coipa de la lista para trabajar con ella.
                    random.shuffle(shuffled) # Baraja los participantes aleatoriamente para determinar los resultados.
                    event.standings = shuffled
                    event.finished = True
                    print(f"El evento {event.name} ha tenido lugar.")
                else:
                    print(f" El evento {event.name} sólo tiene {len(event.participants)} participantes. Necesita 3.")
            else:
                print(f"El evento {event.name} ya ha terminado.")


# Clase que crea los informes de los eventos y países.
class CreateInforms(OptionInterface):
    def execute(self, events_manager: EventsManager):
        informs_manager = ReportManager()
        for event in events_manager.events:
            if event.finished:
                informs_manager.add_event_winners(event)
        informs_manager.add_country_winners()

        print("WINNERS FOR EVENT:")
        for event, winners in informs_manager.event_winners.items():
            print(f"{event.name.capitalize()} Standings:")
            for index, winner in enumerate(winners):
                tabs = "\t" * (index + 1)
                print(f"{tabs}{Medals(index).name}: {winner.name} - {winner.country.name}")

        print("\nCOUNTRY STANDINGS:")
        country_standigs = sorted(informs_manager.country_winners.items(), key=lambda item: (-item[1][0], -item[1][1], -item[1][2]))
        print("COUNTRY  -  GOLD  -  SILVER  -  BRONZE")
        for country, medals in country_standigs:
            print(f"{country.name}     -     {medals[0]}     -     {medals[1]}     -     {medals[2]}")


# Clase que maneja la interfaz de las opciones del menú (Command pattern).
class OptionMenuService:
    def __init__(self, option_interface: OptionInterface, events) -> None:
        self.option_interface = option_interface
        self.events = events

    def execute_option(self):
        self.option_interface.execute(self.events)



def main():
    print("JJOO Paris 2024")
    events_manager = EventsManager()

    # Diccionario de opciones con objetos Command
    options = {
        1: OptionMenuService(EventRegistry(), events_manager),
        2: OptionMenuService(ParticipantRegistry(), events_manager),
        3: OptionMenuService(SimulateEvents(), events_manager),
        4: OptionMenuService(CreateInforms(), events_manager),
    }

    while True:
        print("1. Register event")
        print("2. Register participant")
        print("3. Simulate events")
        print("4. Create informs")
        print("5. Exit")
        try:
            option = int(input("Introduce una opción: "))
            if option == 5:
                print("Saliendo del sistema. ¡Hasta luego!")
                break
            elif option in options:
                options[option].execute_option()
            else:
                print("La opción elegida no existe. Elige una opción válida.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número del 1 al 5.")


main()
