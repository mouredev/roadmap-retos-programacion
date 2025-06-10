#31 { Retos para Programadores } SIMULADOR JUEGOS OLÍMPICOS

# Bibliography reference:
# I use GPT as a reference and sometimes to correct or generate proper comments.

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

import random
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
log = logging.info

def shuffle_array(array):
    for i in range(len(array) - 1, 0, -1):
        j = random.randint(0, i)
        array[i], array[j] = array[j], array[i]
    return array

class Events:
    def __init__(self):
        self.events = {}
        self.prizes = Prizes()

    def add_event(self, event):
        if event in self.events:
            log(f"There's a {event} event already registered.")
        else:
            self.events[event] = []
            log(f"Event {event} registered.")

    def add_player(self, player):
        if player.event not in self.events:
            log(f"Event {player.event} is not registered.")
            return

        is_player = next((p for p in self.events[player.event] if p.name == player.name), None)
        if not is_player:
            self.events[player.event].append(player)
            log(f"Player {player.name} added to {player.event} event.")
        else:
            log(f"The player {player.name} is already registered to {player.event} event.")

    def random_events(self):
        events_list = list(self.events.keys())
        return shuffle_array(events_list)

    def show_participants_for_event(self, event):
        if event in self.events:
            log(f"Participants for {event} event:")
            for p in self.events[event]:
                log(f"{p.name} from {p.country}")
        else:
            log(f"There's no participant registered for the {event} event.")

    def show_registry_data(self):
        for key in self.events:
            log(f"{key} event:")
            for element in self.events[key]:
                log(f"{element.name} from {element.country}")

class Player:
    def __init__(self, name, event, country):
        self.name = name
        self.country = country
        self.event = event

class Prizes:
    def __init__(self):
        self.gold = {}
        self.silver = {}
        self.bronze = {}
        self.country_medals = {}

    def add_gold(self, player):
        self.add_prize(player, 'gold')

    def add_silver(self, player):
        self.add_prize(player, 'silver')

    def add_bronze(self, player):
        self.add_prize(player, 'bronze')

    def add_prize(self, player, prize_type):
        if player.event not in self.__getattribute__(prize_type):
            self.__getattribute__(prize_type)[player.event] = []
        if not any(p.name == player.name for p in self.__getattribute__(prize_type)[player.event]):
            self.__getattribute__(prize_type)[player.event].append(player)
            self.count_country_medal(player.country, prize_type)

    def count_country_medal(self, country, prize_type):
        if country not in self.country_medals:
            self.country_medals[country] = {'gold': 0, 'silver': 0, 'bronze': 0}
        self.country_medals[country][prize_type] += 1

    def show_winners(self):
        log('Winners:')
        for event in self.gold:
            log(f"{event}: Gold - {', '.join(p.name for p in self.gold[event])}")
            log(f"       Silver - {', '.join(p.name for p in self.silver.get(event, [])) if event in self.silver else 'None'}")
            log(f"       Bronze - {', '.join(p.name for p in self.bronze.get(event, [])) if event in self.bronze else 'None'}")

    def show_country_medals(self):
        log('Country Medal Count:')
        for country in self.country_medals:
            log(f"{country}: Gold - {self.country_medals[country]['gold']}, Silver - {self.country_medals[country]['silver']}, Bronze - {self.country_medals[country]['bronze']}")

def event_simulator(events):
    for key in events.events:
        if len(events.events[key]) >= 3:
            winners = shuffle_array(events.events[key])
            events.prizes.add_gold(winners[0])
            events.prizes.add_silver(winners[1])
            events.prizes.add_bronze(winners[2])
        else:
            log(f"Not enough participants for {key} event.")
    events.prizes.show_winners()

dummy_data = [
    ['Bob Marley', 'Archery', 'Jamaica'],
    ['Lenny Kravitz', 'Swimming', 'USA'],
    ['John Lennon', 'Weightlifting', 'England'],
    ['Lorenna McKennit', '100m Sprint', 'Somewhere in Europe'],
    ['Alice', '200m Freestyle', 'The Rabbit Hole'],
    ['Che Guevara', '3000m Steeplechase', 'Argentina'],
    ['Buda', 'Discus Throw', 'India'],
    ['Bugs Bunny', 'Archery', 'Disney'],
    ['Asterix', 'Swimming', 'Comics'],
    ['Lucky Luke', 'Weightlifting', 'Comics'],
    ['Jerry Maguire', '100m Sprint', 'Comics'],
    ['Atreyo', '200m Freestyle', 'Book'],
    ['Simón Bolívar', '3000m Steeplechase', 'Venezuela'],
    ['Goku', 'Discus Throw', 'Anime'],
    ['Shihiro', 'Archery', 'Anime'],
    ['Ruby', 'Swimming', 'Book'],
    ['Crows', 'Weightlifting', 'Book'],
    ['Devian', '100m Sprint', 'Book'],
    ['Peque', '200m Freestyle', 'My World'],
    ['Sophy', '3000m Steeplechase', 'My World'],
    ['Beth', 'Discus Throw', 'My World']
]

first_round = Events()

olympic_events = ['Archery', 'Swimming', 'Weightlifting', '100m Sprint', '200m Freestyle', '3000m Steeplechase', 'Discus Throw']
for event in olympic_events:
    first_round.add_event(event)

for d in dummy_data:
    first_round.add_player(Player(d[0], d[1], d[2]))

first_round.show_registry_data()

event_simulator(first_round)

# Output:
"""    
INFO:root:Event Archery registered.
INFO:root:Event Swimming registered.
INFO:root:Event Weightlifting registered.
INFO:root:Event 100m Sprint registered.
INFO:root:Event 200m Freestyle registered.
INFO:root:Event 3000m Steeplechase registered.
INFO:root:Event Discus Throw registered.
INFO:root:Player Bob Marley added to Archery event.
INFO:root:Player Lenny Kravitz added to Swimming event.
INFO:root:Player John Lennon added to Weightlifting event.
INFO:root:Player Lorenna McKennit added to 100m Sprint event.
INFO:root:Player Alice added to 200m Freestyle event.
INFO:root:Player Che Guevara added to 3000m Steeplechase event.
INFO:root:Player Buda added to Discus Throw event.
INFO:root:Player Bugs Bunny added to Archery event.
INFO:root:Player Asterix added to Swimming event.
INFO:root:Player Lucky Luke added to Weightlifting event.
INFO:root:Player Jerry Maguire added to 100m Sprint event.
INFO:root:Player Atreyo added to 200m Freestyle event.
INFO:root:Player Simón Bolívar added to 3000m Steeplechase event.
INFO:root:Player Goku added to Discus Throw event.
INFO:root:Player Shihiro added to Archery event.
INFO:root:Player Ruby added to Swimming event.
INFO:root:Player Crows added to Weightlifting event.
INFO:root:Player Devian added to 100m Sprint event.
INFO:root:Player Peque added to 200m Freestyle event.
INFO:root:Player Sophy added to 3000m Steeplechase event.
INFO:root:Player Beth added to Discus Throw event.
INFO:root:Archery event:
INFO:root:Bob Marley from Jamaica
INFO:root:Bugs Bunny from Disney
INFO:root:Shihiro from Anime
INFO:root:Swimming event:
INFO:root:Lenny Kravitz from USA
INFO:root:Asterix from Comics
INFO:root:Ruby from Book
INFO:root:Weightlifting event:
INFO:root:John Lennon from England
INFO:root:Lucky Luke from Comics
INFO:root:Crows from Book
INFO:root:100m Sprint event:
INFO:root:Lorenna McKennit from Somewhere in Europe
INFO:root:Jerry Maguire from Comics
INFO:root:Devian from Book
INFO:root:200m Freestyle event:
INFO:root:Alice from The Rabbit Hole
INFO:root:Atreyo from Book
INFO:root:Peque from My World
INFO:root:3000m Steeplechase event:
INFO:root:Che Guevara from Argentina
INFO:root:Simón Bolívar from Venezuela
INFO:root:Sophy from My World
INFO:root:Discus Throw event:
INFO:root:Buda from India
INFO:root:Goku from Anime
INFO:root:Beth from My World
INFO:root:Winners:
INFO:root:Archery: Gold - Bob Marley
INFO:root:       Silver - Shihiro
INFO:root:       Bronze - Bugs Bunny
INFO:root:Swimming: Gold - Lenny Kravitz
INFO:root:       Silver - Ruby
INFO:root:       Bronze - Asterix
INFO:root:Weightlifting: Gold - Crows
INFO:root:       Silver - John Lennon
INFO:root:       Bronze - Lucky Luke
INFO:root:100m Sprint: Gold - Devian
INFO:root:       Silver - Jerry Maguire
INFO:root:       Bronze - Lorenna McKennit
INFO:root:200m Freestyle: Gold - Atreyo
INFO:root:       Silver - Peque
INFO:root:       Bronze - Alice
INFO:root:3000m Steeplechase: Gold - Sophy
INFO:root:       Silver - Che Guevara
INFO:root:       Bronze - Simón Bolívar
INFO:root:Discus Throw: Gold - Buda
INFO:root:       Silver - Goku
INFO:root:       Bronze - Beth

"""