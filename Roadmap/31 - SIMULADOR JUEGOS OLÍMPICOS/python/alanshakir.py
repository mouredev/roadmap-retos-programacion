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
class Participant:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Participant):
            return self.name == value.name and self.country == value.country
        return False
    
    def __hash__(self) -> int:
        return hash(self.name, self.country)

class OlimpicsGames:
    def __init__(self):
        self.events = []
        self.participants = {}
        self.results = {}
        self.country_results = {}

    
    def register_event(self):
        event = input("Introduce el nombre del evento deportivo: ").strip()
        if event in self.events:
            print(f"{event} ya esta registrado")
        else:

            self.events.append(event)
            print(f"{event} registrado exitosamente")
    
    def register_participant(self):
        if not self.events:
            print("No hay eventos registrados")
            return
        else: 
            name = input("Introduce el nombre del participante: ").strip()
            country = input("Introduce el pais del participante: ").strip()
            participant = Participant(name, country)

            print("Eventos disponible")
            for index, event in enumerate(self.events):
                print(f"{index +1}. {event}")

            event_choice = int(input("Selecciona un indice para asignar evento al participante: ")) - 1

            if event_choice >= 0 and event_choice <= len(self.events):
                event = self.events[event_choice]
                if event in self.participants and participant in self.participants[event]:
                    print(f"{participant} ya esta registrado en el evento")
                else:
                    if event not in self.participants:
                        self.participants[event] = []
                    self.participants[event].append(participant)
                    print(f"participante {name} se ha registrado en el evento {event}")
            else:
                print("Evento invalido")

    def simulator_events(self):
        if not self.events:
            print("No hay eventos registrados")
            return
        for event in self.events:
            if len(self.participants[event]) < 3:
                print(f"no hay participantes suficientes para el {event}")
                continue
            event_participants = random.sample(self.participants[event], 3)
            random.shuffle(event_participants)

            gold, silver, bronze = event_participants
            self.results[event] = [gold, silver, bronze]

            self.update_country_results(gold.country, "gold")
            self.update_country_results(silver.country, "silver")
            self.update_country_results(bronze.country, "bronze")

            print(f"resultados de la simulacion: {event}")
            print(f"Oro: {gold.name} ({gold.country})")
            print(f"Silver: {silver.name} ({silver.country})")
            print(f"Bronze: {bronze.name} ({bronze.country})")
    
    def update_country_results(self, country, medal):
        if country not in self.country_results:
            self.country_results[country] = {
                "gold" : 0,
                "silver" : 0,
                "bronze": 0
            }
        self.country_results[country][medal] += 1

    def create_report(self):
        print("Informe juegos")
        if self.results:
            for event, winners in self.results.items():
                print(f"resultados: {event}")
                print(f"Oro: {winners[0].name} ({winners[0].country})")
                print(f"Silver: {winners[1].name} ({winners[1].country})")
                print(f"Bronze: {winners[2].name} ({winners[2].country})")
        else:
            print("No hay eventos registrados")
        
        if self.country_results:
            for country, medals in sorted(self.country_results.items(), key=lambda x: (x[1]["gold"], x[1]["silver"], x[1]["bronze"]), reverse=True):
                print(f"{country}: Oro {medals['gold']}, Silver {medals['silver']}, Bronze {medals['bronze']}")
        else:
            print("No hay medallas por pais")   




olimpics = OlimpicsGames()
print("Simulador de juegos olimpicos")
while True:
    print()
    print("1. Registro de eventos.") 
    print("2. Registro de participantes.")
    print("3. Simulación de eventos.")
    print("4. Creación de informes.")
    print("5. Salir del programa.")
    print()

    option = input("Elige una accion: ")
    print()
    match option:
        case "1":
            olimpics.register_event()
        case "2":
            olimpics.register_participant()
        case "3":
            olimpics.simulator_events()
        case "4":
            olimpics.create_report()
        case "5":
            print("Fin de la simulacion.")
            break
