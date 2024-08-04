# ╔═════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado              ║
# ║ GitHub: https://github.com/Kenysdev ║
# ║ 2024 -  Python                      ║
# ╚═════════════════════════════════════╝

# ---------------------------------
# 31 * SIMULADOR JUEGOS OLÍMPICOS
# ---------------------------------

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

from abc import ABC, abstractmethod
from random import randint
import copy

# _______________
# -> Acciones:
MENU = """
SIMULADOR JUEGOS OLÍMPICOS:
--------------------------------------------------
| 1. Registrar evento        | 4. Crear informes |  
| 2. Registrar participante  | 5. Salir          |
| 3. Simulación de eventos   |                   |
--------------------------------------------------
"""

class AbstractDataTable(ABC):
    """Contrato sobre los métodos requeridos para cada tabla creada."""
    @abstractmethod
    def add(self) -> None:
        pass

    @abstractmethod
    def count(self) -> int:
        pass

    @abstractmethod
    def get_list(self) -> list:
        pass

#__________________________
class DataInMemory():
    __instance = None

    class EventsTable(AbstractDataTable):
        def __init__(self) -> None:
            self._dt: list = []
        
        def add(self, sport: str) -> None: 
            self._dt.append([sport])
        
        def count(self) -> int:
            return len(self._dt)

        def get_list(self) -> list:
            return copy.deepcopy(self._dt)


    class ParticipantsTable(AbstractDataTable):
        def __init__(self) -> None:
            self._dt: list = []

        def add(self, name: str, country: str) -> None: 
            self._dt.append([name, country])
        
        def count(self) -> int:
            return len(self._dt)

        def get_list(self) -> list:
            return copy.deepcopy(self._dt)

    class SimulationTable(AbstractDataTable):
        def __init__(self) -> None:
            self._dt: list = []

        def add(self, result_event: list) -> None:
            self._dt.append(result_event)
        
        def count(self) -> int:
            return len(self._dt)
        
        def get_list(self) -> list:
            return self._dt

    def _init_tables(self):
        self.events_table = self.EventsTable()
        self.participants_table = self.ParticipantsTable()
        self.simulation_table = self.SimulationTable()

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance._init_tables()
        return cls.__instance

#__________________________
class Input():
    def get(self, msg: str) -> str:
        while True:
            txt: str = input(msg)
            if len(txt) > 0:
                return txt
                break

#__________________________
# -> Requisitos:
# 1. Registrar eventos deportivos.
class Events():
    def __init__(self, data, input_):
        self.dt = data()
        self.input_ = input_()

    def add(self) -> None:
        print("AGREGAR EVENTO DEPORTIVO:")
        sport: str = self.input_.get("Deporte: ")
        self.dt.events_table.add(sport)
        print(f"{sport} fue agregado")
        #print(MENU)
        
#__________________________
# 2. Registrar participantes por nombre y país.
class Participants():
    def __init__(self, data, input_):
        self.dt = data()
        self.input_ = input_()

    def add(self) -> None:
        print("AGREGAR PARTICIPANTE:")
        name: str = self.input_.get("Nombre: ")
        country: str = self.input_.get("país: ")
        self.dt.participants_table.add(name, country)
        print(f"{name} fue agregado")
        #print(MENU)
        
#__________________________
# 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
# 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
 
class Simulation():
    def __init__(self, data):
        self.dt = data()

    def _qualify_participants(self) -> list:
        participants = self.dt.participants_table.get_list()
        for p in participants:
            p.append(randint(1, 100))
        
        participants.sort(key=lambda x: x[2], reverse=True)
        top_3_participants = participants[:3]

        medals = ['Oro', 'Plata', 'Bronce']
        for i, p in enumerate(top_3_participants):
            p.append(medals[i])
        
        return top_3_participants

    def _add_result_events(self):
        events = self.dt.events_table.get_list()
        simulation: list = []
        for e in events:
            top_3_result: list = self._qualify_participants()
            e.append(self._qualify_participants())
            simulation.append(e)

        self.dt.simulation_table.add(simulation)

    def start(self) -> None:
        if self.dt.events_table.count() >= 1:
            if self.dt.participants_table.count() >= 3:
                self._add_result_events()
                total_simulation = self.dt.simulation_table.count()
                print(f"Simulación '#{total_simulation}' creada.")
                print("Puedes ver el resultadoc con opcion: '4. Crear informes.'")
            else:
                print("Debe haber al menos 'tres' participantes.")
        else:
            print("Debe haber al menos un evento.")

#__________________________
# 5. Mostrar los ganadores por cada evento.
# 6. Mostrar el ranking de países según el número de medallas.
class Reports():
    def __init__(self, data):
        self.dt = data()
        self.ranking_countries: dict = {}

    def _generate_top_countries(self):
        countries = self.ranking_countries.items()
        sorted_rank = sorted(countries, key=lambda item: item[1], reverse=True)

        for i, (name, total) in enumerate(sorted_rank):
            print(f"'{i + 1}' - {name} -> Medallas: {total}")

    def _iterate_participants(self, participants):
        for i, participant in enumerate(participants):
            name, country, score, medal = participant
            
            print(f"'{i + 1}' - {name} - {country} -> Score: {score}, Medal: {medal}")

            # Registrar para generar ranking de países por numero de medallas.
            if country in self.ranking_countries:
                self.ranking_countries[country] += 1
            else:
                self.ranking_countries[country] = 1

    def _iterate_events(self, simulation):
        for event in simulation:
            event_name = event[0]
            participants = event[1]

            print(f"\nEvent: {event_name}:")
            self._iterate_participants(participants)

    def generate(self) -> None:
        simulations = self.dt.simulation_table.get_list()
        if simulations == []:
            print("Aún no hay simulaciones creadas.")

        for i, simulation in enumerate(simulations):
            simulation_id = i + 1
            
            print(f"\n______________\nSimulation {simulation_id}")
            self._iterate_events(simulation)

            print("\nRanking de países, según el número de medallas:") 
            self._generate_top_countries()
            self.ranking_countries.clear()

        #print(MENU)

#__________________________
class Program():
    def __init__(self, data, input_):
        self.input_ = input_()
        self._events = Events(data, input_)
        self._participants = Participants(data, input_)
        self._simulation = Simulation(data)
        self._reports = Reports(data)

    def run(self):
        print(MENU)
        while True:
            option = self.input_.get("\nOpción: ")
            match option:
                case "1": self._events.add()
                case "2": self._participants.add()
                case "3": self._simulation.start()
                case "4": self._reports.generate()
                case '5': print("Adios"); break
                case _: print("Seleccionar de '1 a 5'")

#__________________________
if __name__ == "__main__":
    program = Program(DataInMemory, Input)
    program.run()

# end
