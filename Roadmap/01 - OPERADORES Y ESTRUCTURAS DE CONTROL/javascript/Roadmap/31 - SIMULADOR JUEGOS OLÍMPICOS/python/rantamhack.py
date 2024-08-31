

'''
 * EJERCICIO:
 * ¡Los JJOO de Pari­s 2024 han comenzado!
 * Crea un programa que simule la celebración de los juegos.
 * El programa debe permitir al usuario registrar eventos y participantes,
 * realizar la simulación de los eventos asignando posiciones de manera aleatoria
 * y generar un informe final. Todo ello por terminal.
 * Requisitos:
 * 1. Registrar eventos deportivos.
 * 2. Registrar participantes por nombre y paí­s.
 * 3. Simular eventos de manera aleatoria en base a los participantes (má­nimo 3).
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

import random


class Event:
    def __init__(self, name):
        self.name = name
        self.participants = []
        
    def add_participant(self, participant):
        self.participants.append(participant)
        
        
class Participants:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        
        
        
class SimulateEvent:
    def __init__(self, events, results):
        self.events = events
        self.results = results
    
    def simulate(self):
        for event in self.events:
            random.shuffle(event.participants)
            self.results[event.name] = event.participants[:3]  
            
            
class Report:
    def __init__(self, results):
        self.results = results
    
    def create_report(self):
        for event, winners in self.results.items():
            print(f"Evento:  {event}")
            medals = ["Gold", "Silver", "Bronze"]
            for i, winner in enumerate(winners):
                print(f"{medals[i]}: {winner.name} ({winner.country})")


class OlympiceGames:
    def __init__(self):      
        self.events = []
        self.participants = []
        self.results = {}
        
    def register_event(self, event_name):
        event = Event(event_name)
        if event_name not in [e.name for e in self.events]:
            self.events.append(event)
        else:
            print("El evento ya está registrado")
            
    def register_participant(self, name, country, event_name):
        participant = Participants(name, country)
        self.participants.append(participant)
        for event in self.events:
            if event.name ==  event_name:
                event.add_participant(participant)
            break  
        else:
            print("El evento no está registrado")

    def simulate_events(self):  
        simulator = SimulateEvent(self.events, self.results)
        simulator.simulate()  
        
    def generate_report(self):
        report = Report(self.results)
        report.create_report()                       
    
    def show_menu(self):
        while True:
            print("\nMenu: ")
            print("\n\t1. Registrar Evento")
            print("\n\t2. Registrar Participante")
            print("\n\t3. Simular Evento")
            print("\n\t4. Generar informe")
            print("\n\t5. Salir")
            print("\n\t6. Mostrar eventos y participantes guardados")
             
            option = input("\n\tSeleccione una opción del menú: ") 
            
            if option == "1":
                event_name = input("Pon el nombre del nuevo evento: ")
                self.register_event(event_name)
                
            elif option == "2":
                name = input("Escriba el nombre del participante: ")
                country = input("Escriba el pais al que pertenece el nuevo participante: ")
                event_name = input("Escriba el nombre del evento en el que desea inscribirse: ")
                self.register_participant(name, country, event_name)
                    
            elif option == "3":
                self.simulate_events()
                
            elif option == "4":
                self.generate_report()
                
            elif option == "5":
                break
            
            elif option == "6":
                print("\nEventos guardados:")
                for event in self.events:
                    print(f"{event.name}")

                print("\nParticipantes guardados: ")
                for participant in self.participants:
                    print(f" {participant.name} ({participant.country})")

            else:
                print("Opcion incorrecta, por favor elige una opcion entre la 1 y la 6")   
            
            
paris2024 = OlympiceGames()
paris2024.show_menu()          
            
    
        
