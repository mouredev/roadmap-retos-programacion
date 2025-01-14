from random import randint, choice

class SignEvent:
    """
    Registra un evento
    """
    event_list = [] #Listado de eventos
    
    def __init__ (self, name: str):
        self.name = name
        SignEvent.event_list.append(self)       
        

class SignParticipant:
    """
    Registra un participante
    """   
    def __init__(self, name: str, country: str):
        self.name = name
        self.country = country
        self.wins = 0
        
        # Verifica si el país ya está en la lista de países, lo agrega si no esta
        if country not in [c.country for c in CountryRanking.countries_list]:
            CountryRanking(country)
    
    def __str__(self):
        return f"{self.name} de {self.country}"
        

class Event(SignEvent):
    """
    Inicia el evento y agrega a los participantes
    """
    def __init__(self, name: str):
        super().__init__(name)
        self.participants_list = []

    def add_participant(self, participant: SignParticipant):
        self.participants_list.append(participant)
    
    def get_participants(self):
        return self.participants_list


class StartEvent:
    """
    Da comienzo a un evento de manera aleatoria
    """
    def start(self):
        if SignEvent.event_list:
            # Inicializamos un evento aleatorio y se elimina de la lista
            random_index = randint(0, len(SignEvent.event_list)-1)
            random_event = SignEvent.event_list.pop(random_index)
            print(f'\nComienza el evento {random_event.name}!!')
            
            return random_event
        
        else:
            print('Se acabaron los eventos, gracias por asistir.')
            
            return None

    
class SimulEvent():
    """
    Simula el evento elegido
    """
    @staticmethod
    def start(event: Event):
        #Simula los 'combate'
        winner_1 = SimulEvent.fight(event, 0, 1)
        winner_2 = SimulEvent.fight(event, 2, 3)
        
        # Combate entre los ganadores de los combates anteriores
        SimulEvent.fight(event, winner_1, winner_2)
        
        # Muestra el ranking
        EventRanking.ranking(event)

    
    @staticmethod
    def fight(event: Event, index1: int, index2: int):
        p_1 = event.participants_list[index1]    
        p_2 = event.participants_list[index2] 

        print(f"{p_1} VS {p_2}")
        
        winner = choice([p_1, p_2])
        print(f"{winner.name} ha vencido!!\n")
        winner.wins += 1
        
        # Retorna el índice del ganador en la lista de participantes
        return event.participants_list.index(winner)
        

class EventRanking():
    @staticmethod
    def ranking(event: Event):
            ranking = sorted(event.participants_list, key = lambda x : x.wins, reverse=True) 
            medals = ['oro', 'plata', 'cobre']
            
            for index, participant in enumerate(ranking):
                if index < 3:
                    print(f"Medalla de {medals[index]} para {participant} - {participant.wins} victorias")
                    index_country = next((i for i, c in enumerate(CountryRanking.countries_list) if c.country == participant.country), None)
                    if index_country is not None:
                        CountryRanking.countries_list[index_country].medals[index] += 1
                        CountryRanking.countries_list[index_country].update_total_medals()
                

class CountryRanking():
    countries_list = []
    
    def __init__(self, country):
        self.country = country
        self.medals = [0, 0, 0]  # [oro, plata, cobre]
        self.total = 0
        CountryRanking.countries_list.append(self)
    
    def update_total_medals(self):
        self.total = sum(self.medals)
    
    def __str__(self):
        return self.country
    
    @staticmethod
    def ranking():
        ranking = sorted(CountryRanking.countries_list, key = lambda x : x.total, reverse=True) 

        print("\nClasificación por países:")
        for index,country in enumerate(ranking):
            print(f"{index + 1} - {country.country} - Oro: {country.medals[0]}, Plata: {country.medals[1]}, Cobre: {country.medals[2]}, Total: {country.total}")



# Agregamos varios eventos y participantes
event_1 = Event('Atletismo')
event_1.add_participant(SignParticipant('Daniel Galvan', 'España'))
event_1.add_participant(SignParticipant('Mark Ruffalo', 'Usa'))
event_1.add_participant(SignParticipant('Tofu Minamato', 'Japon'))
event_1.add_participant(SignParticipant('Milano milanesa', 'Italia'))


event_2 = Event('Baloncesto')
event_2.add_participant(SignParticipant('Daniel Galvan', 'España'))
event_2.add_participant(SignParticipant('Mark Ruffalo', 'Usa'))
event_2.add_participant(SignParticipant('Tofu Minamato', 'Japon'))
event_2.add_participant(SignParticipant('Milano milanesa', 'Italia'))

event_3 = Event('Boxeo')
event_3.add_participant(SignParticipant('Daniel Galvan', 'España'))
event_3.add_participant(SignParticipant('Mark Ruffalo', 'Usa'))
event_3.add_participant(SignParticipant('Tofu Minamato', 'Japon'))
event_3.add_participant(SignParticipant('Milano milanesa', 'Italia'))

event_4 = Event('Tiro con arco')
event_4.add_participant(SignParticipant('Daniel Galvan', 'España'))
event_4.add_participant(SignParticipant('Mark Ruffalo', 'Usa'))
event_4.add_participant(SignParticipant('Tofu Minamato', 'Japon'))
event_4.add_participant(SignParticipant('Milano milanesa', 'Italia'))

event_5 = Event('Natación')
event_5.add_participant(SignParticipant('Daniel Galvan', 'España'))
event_5.add_participant(SignParticipant('Mark Ruffalo', 'Usa'))
event_5.add_participant(SignParticipant('Tofu Minamato', 'Japon'))
event_5.add_participant(SignParticipant('Milano milanesa', 'Italia'))

event_6 = Event('Esgrima')
event_6.add_participant(SignParticipant('Daniel Galvan', 'España'))
event_6.add_participant(SignParticipant('Mark Ruffalo', 'Usa'))
event_6.add_participant(SignParticipant('Tofu Minamato', 'Japon'))
event_6.add_participant(SignParticipant('Milano milanesa', 'Italia'))


# Inicializa los eventos de manera aleatoria
while SignEvent.event_list:
    start_event = StartEvent().start()
    if start_event:
        SimulEvent.start(start_event)

# Mostrar la clasificación final por países
CountryRanking.ranking()





