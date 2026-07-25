### Simulador Juegos Olímpicos
import random

class Athlete():
    
    def __init__(self, name: str, country: str):
        self.name = name
        self.country = country
        
    # Comprobación de si estamos trabajando con un mismo atleta
    def __eq__(self, athlete: object)->bool:
        if isinstance(athlete, Athlete):
            return self.name == athlete.name and self.country == athlete.country
        return False
    
class OlimpicGames():
    
    def __init__(self):
        self.events = []
        self.participants = {}
        self.event_results = {}
        self.country_results = {}
    
    #Registro de evento
    def register_event(self):
        
        event_name = input("Introduce el nombre del evento: ")
        
        if event_name.lower() in self.events:
            print(f"El evento {event_name.capitalize()} ya está registrado.")
        else:
            self.events.append(event_name.lower())
            print(f"El evento {event_name.capitalize()} se ha registrado correctamente")
    
    # Listar eventos disponibles
    def list_events(self):
        
        if not self.events:
            print("No hay eventos registrados. Por favor, regístra un evento primero.")
        else:
            print("Eventos disponibles:")
            for i, event in enumerate(self.events):
                print(f"{i+1}. {event.capitalize()}")
    
    #Registro de participante
    def register_participant(self):
        
        if not self.events:
            print("No hay eventos registrados. Por favor, regístra un evento primero.")
        else:
            name = input("Introduce el nombre del atleta: ")
            country = input("Introduce el país del atleta: ")
            #athlete = Athlete(name, country)
            
            # Tenemos que mostrar la lista de eventos disponibles para inscribir al atleta.
            self.list_events()
            option = int(input("Indica el evento en el quieres inscribir al participante: "))
            
            #Comprobación de opción correcta:
            while (option < 1 or option > len(self.events)) or not isinstance(option, int):
                print("Error, debes indicar una de las opciones de eventos que te listamos: ")
                option = int(input("Indica el evento en el quieres inscribir al participante: "))
            
            # Añadimos al diccionario de participantes el evento y la lista de participantes.
            if not self.events[option-1] in self.participants:
                self.participants[self.events[option-1]] = []
                
            # Tenemos que comprobar que el participante no esté ya inscrito
            if Athlete(name, country) in self.participants[self.events[option-1]]:
                print(f"El atleta {name} ya está inscrito en el evento {self.events[option-1].capitalize()}")
            else:
                self.participants[self.events[option-1]].append(Athlete(name, country))
                print(f"El atleta {name} se ha inscrito correctamente en el evento {self.events[option-1].capitalize()}")
            
    # Listar participantes inscritos por evento    
    def list_participants(self):
        
        if not self.participants:
            print("No hay participantes inscritos. Por favor, inscribe un participante primero.")
        else:
            print("Participantes inscritos:")
            for event, participants in self.participants.items():
                print(f"Evento: {event.capitalize()}")
                for i, participant in enumerate(participants):
                    print(f"{i+1}. {participant.name} - {participant.country}")
    
    #Asignar medallas tras evento
    def assign_medal(self, country: str, position: int):
        if not country in self.country_results:
            self.country_results[country] = [0,0,0] #Orden Oro, Plata, Bronce
        self.country_results[country][position] +=1
    
    '''
    Para el ranking y simulando a como ocurre en realidad vamos a darle
    mas valor a las medallas de oro que de plata y a las de plata sobre 
    las de bronce:
    oro x 5
    plata x 2
    bronce x 1
    '''
    #Ranking según Paises
    def show_ranking(self):
        
        ranking = []
        
        if not self.country_results:
            print("No hay resultados de eventos. Registra eventos, participantes y simulalos")
        else:
            for country, results in self.country_results.items():
                score = results[0]*5 + results[1]*2 + results[2]
                ranking.append((country, score, results[0], results[1], results[2]))
            
            # Ordenar el ranking por el puntaje de mayor a menor
            ranking.sort(key=lambda x: x[1], reverse=True)
            
            print("Ranking de países:")
            for country, score, gold, silver, bronze in ranking:
                print(f"{country}: Oro: {gold} Plata: {silver} Bronce: {bronze} - Puntuación: {score}")

    #Mostrar resultados de un evento
    def show_event_results(self):
        #Mostramos los eventos disponibles
        self.list_events()
        
        option = int(input("Indica el evento sobre el que consultar el resultado: "))
            
        #Comprobación de opción correcta:
        while (option < 1 or option > len(self.events)) or not isinstance(option, int):
            print("Error, debes indicar una de las opciones de eventos que te listamos: ")
            option = int(input("Indica el evento sobre el que consultar el resultado: "))
        print(f"Posicion  Participante  País")
        print(f"=============================")
        for i, participant in enumerate(self.event_results[self.events[option-1]]):
            if i+1 == 1:
                print(f"{i+1}. {participant.name} - {participant.country} - Medalla de Oro")
            elif i+1 == 2:
                print(f"{i+1}. {participant.name} - {participant.country} - Medalla de Plata")
            elif i+1 == 3:
                print(f"{i+1}. {participant.name} - {participant.country} - Medalla de Bronce")
            else:
                print(f"{i+1}. {participant.name} - {participant.country}")
    #Simular un evento
    def simulate_event(self):
        self.list_events()
        
        option = int(input("Indica el evento que quieres simular: "))
        #Comprobación de opción correcta:
        while (option < 1 or option > len(self.events)) or not isinstance(option, int):
            print("Error, debes indicar una de las opciones de eventos que te listamos: ")
            option = int(input("Indica el evento que quieres simular: "))
        
        #Minimo de participantes
        if not len(self.events[option-1]) >= 3:
            print(f"El evento {self.events[option-1].capitalize()} no tiene el mínimo de participantes")
        else:
            #Simulación del evento
            if not self.events[option-1] in self.event_results:
                self.event_results[self.events[option-1]] = []
            
                print(f"Simulando el evento {self.events[option-1].capitalize()}...")
                positions = random.sample(self.participants[self.events[option-1]], len(self.participants[self.events[option-1]]))
                self.event_results[self.events[option-1]] = positions
                
                #Mostramos el resultado de la simulación del evento y guardamos las medallas en el medallero de cada País.
                print(f"El resultado del evento {self.events[option-1].capitalize()} es: ")
                for i, participant in enumerate(self.event_results[self.events[option-1]]):
                    if i+1 == 1:
                        print(f"{i+1}. {participant.name} - {participant.country} - Medalla de Oro")
                        self.assign_medal(country=participant.country, position=i)
                    elif i+1 == 2:
                        print(f"{i+1}. {participant.name} - {participant.country} - Medalla de Plata")
                        self.assign_medal(country=participant.country, position=i)
                    elif i+1 == 3:
                        print(f"{i+1}. {participant.name} - {participant.country} - Medalla de Bronce")
                        self.assign_medal(country=participant.country, position=i)
                    else:
                        print(f"{i+1}. {participant.name} - {participant.country}")
                print(f"Fin de la simulación del evento {self.events[option-1].capitalize()}...")
                
paris2024 = OlimpicGames()

paris2024.register_event()
paris2024.register_event()
paris2024.register_participant()
paris2024.register_participant()
paris2024.register_participant()
paris2024.register_participant()
paris2024.register_participant()
paris2024.register_participant()
paris2024.register_participant()
paris2024.register_participant()
paris2024.list_participants()
paris2024.simulate_event()
paris2024.simulate_event()
paris2024.show_event_results()
paris2024.show_ranking()