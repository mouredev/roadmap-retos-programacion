'''
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
'''
import random

class Olympics:

    def __init__(self) -> None:
        
        self.events: list = []
        self.participants: dict = {}
        self.results: dict = {}
        self.country_medals: dict = {}

    def register_event(self):
        
        event = input("Ingrese el nombre del evento: ").strip()

        if event in self.events:
            print("El evento ya se encuentra registrado.")
        else:
            self.events.append(event)
            print(f"Evento {event} registrado con éxito.")
        

    def register_participant(self):
        
        if not self.events:
            print("No se han registrado eventos.")
            return
        
        name = input("Ingrese el nombre del participante: ").strip()
        country = input("Ingrese el país del participante: ").strip()
        participant = Participant(name, country)

        print("Eventos registrados:")
        for index, event in enumerate(self.events):
            print(f"{index + 1}. {event}")

        event_choice = int(
            input(
                "Seleccione el evento en el que participará: "
                )
            )-1
        
        if event_choice >= 0 and event_choice < len(self.events):
            event = self.events[event_choice]
            if event in self.participants and participant in self.participants[event]:
                print(f"El participante {name} ya se encuentra registrado en el evento {event}.")
            else:
                if event not in self.participants:
                    self.participants[event] = []
                self.participants[event].append(participant)
                print(f"Participante {name} de {country} registrado en el evento {event}.")      
        else:
            print("Evento no válido.")
    
    def simulate_event(self):
        
        if not self.events:
            print("No se han registrado eventos.")
            return
        
        for event in self.events:
            
            if len(self.participants[event]) < 3:
                print(f"El evento {event} no cuenta con suficientes participantes (mínimo 3).")
                continue
                        
            if event in self.results: # Si el evento ya ha sido simulado no se vuelve a simular
                print(f"El evento {event} ya ha sido simulado.")
                continue

            event_participant = random.sample(self.participants[event], 3)
            random.shuffle(event_participant)
            gold, silver, bronze = event_participant
            self.results[event] = [gold, silver, bronze]
                       
            self.update_country_results(gold.country, "gold")
            self.update_country_results(silver.country, "silver")
            self.update_country_results(bronze.country, "bronze")

            print(f"Resultado simulación del evento: {event}.")
            print(f"Oro: {gold.name} - {gold.country}")
            print(f"Plata: {silver.name} - {silver.country}")
            print(f"Bronce: {bronze.name} - {bronze.country}")
    
    def update_country_results(self, country, medal):
        if country not in self.country_medals:
            self.country_medals[country] = {"gold": 0, "silver": 0, "bronze": 0}
        self.country_medals[country][medal] += 1

    def show_report(self):

        print("Informe Juegos Olimpicos: ")
        if self.results:
            for event, winners in self.results.items():
                print(f"Evento: {event}.")
                print(f"Oro: {winners[0].name} - {winners[0].country}")
                print(f"Plata: {winners[1].name} - {winners[1].country}")
                print(f"Bronce: {winners[2].name} - {winners[2].country}")
        else:
            print("No hay resultados para mostrar.")
        
        if self.country_medals:
            print("Ranking de países:")
            sorted_countries = sorted(self.country_medals.items(), key=lambda x: (x[1]["gold"], x[1]["silver"], x[1]["bronze"]), reverse=True)
            for country, medals in sorted_countries:
                print(f"{country}: {medals['gold']} oro, {medals['silver']} plata, {medals['bronze']} bronce.")
        else:
            print("No hay países con medallas.")

class Participant():

    def __init__(self, name: str, country: str) -> None:
        self.name = name
        self.country = country

    def __eq__(self, other: object) -> bool:
        
        if isinstance(other, Participant):
            return self.name == other.name and self.country == other.country 
        return False

    def __hash__(self) -> int:
        return hash((self.name, self.country))
    
if __name__ == '__main__':

    olympics = Olympics()

    print("Simulación de Juegos Olímpicos")
    while True:

        print("""
        1. Registro de eventos.
        2. Registro de participantes.
        3. Simulación de eventos.
        4. Creación de informes.
        5. Salir del programa.
        """)

        option = input("Seleccione una opción: ")

        match option:
            case "1":
                olympics.register_event()
            case "2":
                olympics.register_participant()
            case "3":
                olympics.simulate_event()
            case "4":
                olympics.show_report()
            case "5":
                print("Saliendo del simulador...")
                break
            case _:
                print("Opción no válida, seleccione una opción del menú")