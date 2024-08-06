#El enfoque para implementar este programa ha sido tratando de seguir los principios SOLID
#MEJORAS POSIBLES A IMPLEMENTAR:
# - Regex en todos los inputs
# - Uso de archivos externos para guardar información y generar informes
# - Logging para el debug e información de sistema
# - Manejo de excepciones: sería necesario probablemente implementarlo en alguno de los métodos sobre todo si se incluyera el control de los input por Regex.

from abc import ABC,abstractmethod
from random import randint

#INTERFACES ABSTRACTAS
class AbstractEvent(ABC):
    @abstractmethod
    def __init__(self,discipline:str):
        pass

class AbstractParticipant(ABC):
    @abstractmethod
    def __init__(self,name:str,country:str):
        pass

class AbstractListOfEvents(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

class AbstractCountry(ABC):
    @abstractmethod
    def __init__(self,name:str,medals_quantity:int=0, gold: int=0,silver:int=0,bronze:int=0):
        pass

class AbstractOlympicWinner(ABC):
    @abstractmethod
    def __init__(self,name:str,country:str,medals_quantity:int=0,gold:int=0,silver:int=0,bronze:int=0):
        pass

class AbstractInformsGenerator(ABC):
    @abstractmethod
    def generate_country_informs(self):
        pass

    @abstractmethod
    def generate_winner_informs(self):
        pass

class AbstractInformsPrinter(ABC):
    @abstractmethod
    def show_country_ranking(self):
        pass

    abstractmethod
    def show_winners_ranking(self):
        pass

class AbstractEventRegister(ABC):
    @abstractmethod
    def event_register(self,event:AbstractEvent,event_list:AbstractListOfEvents):
        pass

class AbstractParticipantRegister(ABC):
    @abstractmethod
    def participant_register(self,event:AbstractEvent,participant:AbstractParticipant):
        pass

class AbstractEventSimulator(ABC):
    @abstractmethod
    def simulate_event(self,event:AbstractEvent):
        pass

    @abstractmethod
    def show_event_winners(self,event:AbstractEvent):
        pass

#CLASES QUE HEREDAN DE LAS INTERFACES ABSTRACTAS

class Participant(AbstractParticipant):
    def __init__(self,name:str,country:str):
        self.data = {"name":name,"country":country}
        self.medals = {"quantity":0,"gold":0,"silver":0,"bronze":0}

    def print_participant(self):
        return f"- Nombre: {self.data["name"]}\n- País: {self.data["country"]}\n"

class Event(AbstractEvent):
    def __init__(self,discipline:str):
        self.discipline = discipline.upper()
        self.participant_list = []
        self.event_winners = []

    def add_participant(self,participant:AbstractParticipant):
        return self.participant_list.append(participant)
    
    def show_details(self): #imprime por pantalla la disciplina del evento y el número de participantes
        print(f"Disciplina: {self.discipline}")
        print(f"Número de participantes:{len(self.participant_list)}")
        print("\n")

    def event_completed(self): #devuelve un true si el evento está completado y un false si no lo está
        if len(self.event_winners) == 0:
            return False
        else:
            return True

class Events(AbstractListOfEvents):
    def __init__(self):
        self.events = list()

    def add_event(self,event:AbstractEvent):
        return self.events.append(event)
    
    def get_event(self,position:int): #devuelve el evento dada una posición en la lista
        try:
            return self.events[position]
        except:
            print("Esa disciplina no está presente en estos Juegos Olímpicos")
    
    def show_events(self): #muestra todos los eventos que hay almacenados
        for event in self.events:
            event.show_details()

    def find_event(self,event:str): #busca un evento y devuelve el índice que tiene dentro de la lista
        found = False
        event_index = None
        for index,listed_event in enumerate(self.events):
            if listed_event.discipline == event:
                found = True
                event_index = index
                break
        if found:
            return event_index
        else:
            print("Esta disciplina no se encuentra en la lista\n") #podría preguntar si se quiere añadir...            

class EventRegister(AbstractEventRegister):
    def event_register(self,event:AbstractEvent,event_list:AbstractListOfEvents): #registra una disciplina y no deja registrar disciplinas con el mismo nombre
        event_found = False
        for element in event_list.events:
            if element.discipline == event.discipline:
                event_found = True
        if not event_found:
            event_list.add_event(event)
            print("Disciplina registrada\n")
        else:
            print("Disciplina anteriormente registrada, prueba de nuevo\n")

class ParticipantRegister(AbstractParticipantRegister):
    def participant_register(self,event:AbstractEvent,participant:AbstractParticipant): #registra un participante y no deja registrar un participante con el mismo nombre
        participant_found = False                                                       # -- se podría controlar comparando nombre y país
        for element in event.participant_list:
            if element.data["name"] == participant.data["name"]:
                participant_found = True
        if not participant_found:
            event.add_participant(participant)
        else:
            print("Participante anteriormente registrado.\n")

class EventSimulator(AbstractEventSimulator):
    def simulate_event(self,event:AbstractEvent): #simula un evento cogiendo un número aleatorio entre 0 y el número de participantes -1
        if len(event.participant_list) < 3:       # y guarda los ganadores en una lista siendo el 0 - ORO, 1 - PLATA, 2 - BRONCE
            print("No se puede simular el evento, no hay participantes suficientes")
        else: 
            win_count = 0
            index = 0
            while win_count < 3:
                index = randint(0,len(event.participant_list)-1)
                if event.participant_list[index] not in event.event_winners:
                    event.participant_list[index].medals["quantity"] = 1
                    #si win_count = 0 -- ORO || win_count = 1 -- PLATA || win_count = 2 -- BRONCE
                    if win_count == 0:
                        event.participant_list[index].medals["gold"] += 1
                    elif win_count == 1:
                        event.participant_list[index].medals["silver"] += 1
                    elif win_count == 2:
                        event.participant_list[index].medals["bronze"] += 1
                    event.event_winners.append(event.participant_list[index])
                    win_count += 1
    
    def show_event_winners(self,event:AbstractEvent): #muestra el detalle de los ganadores y qué medalla han ganado. Si no hay ganadores, muestra un mensaje de que el evento no se ha celebrado
        if len(event.event_winners) != 0:
            print(f"Disciplina: {event.discipline}\nNúmero de participantes: {len(event.participant_list)}\nORO\n{event.event_winners[0].print_participant()}\nPLATA\n{event.event_winners[1].print_participant()}\nBRONCE\n{event.event_winners[2].print_participant()}\n")
        else:
            print(f"Disciplina: {event.discipline}\n-- No se ha celebrado el evento --\n")

class OlympicWinner(AbstractOlympicWinner): #clase para almacenar el ranking de los deportistas que han participado, con su cantidad de medallas y tipo
    def __init__(self,name:str,country:str,medals_quantity:int=0,gold:int=0,silver:int=0,bronze:int=0):
        self.data ={"name":name,"country":country}
        self.medals = {"quantity":medals_quantity,"gold":gold,"silver":silver,"bronze":bronze}

class Country(AbstractCountry): #clase para almacenar los países que han participado con su nombre, cantidad de medallas y tipo
    def __init__(self, name:str,medals_quantity:int=0, gold: int=0,silver:int=0,bronze:int=0):
        self.name = name
        self.medals = {"quantity":medals_quantity,"gold":gold,"silver":silver,"bronze":bronze}

class InformsGenerator(AbstractInformsGenerator): #clase para generar los informes por país y por deportistas
    def __init__(self):
        self.country_ranking = []
        self.winner_ranking = []

    def generate_country_informs(self,list_of_events:AbstractListOfEvents):
        for event in list_of_events.events:
            for winner in event.event_winners:
                country = next((c for c in self.country_ranking if c.name == winner.data["country"]), None)
                if country is None:
                    country = Country(name=winner.data["country"], medals_quantity=1, gold=winner.medals["gold"], silver=winner.medals["silver"], bronze=winner.medals["bronze"])
                    self.country_ranking.append(country) #si el país no está en la lista, lo crea con el constructor de Country
                else:
                    country.medals["quantity"] += 1
                    country.medals["gold"] += winner.medals["gold"]
                    country.medals["silver"] += winner.medals["silver"]
                    country.medals["bronze"] += winner.medals["bronze"] #si está, actualiza la cantidad de medallas

    def generate_winner_informs(self,list_of_events:AbstractListOfEvents):
        for event in list_of_events.events:
            for winner in event.event_winners:
                olympic_winner = next((ow for ow in self.winner_ranking if ow.data["name"]== winner.data["name"]),None)
                if olympic_winner == None: #si el deportista no está en la lista, lo crea con el constructor de OlympicWinner
                    self.winner_ranking.append(OlympicWinner(name=winner.data["name"],country=winner.data["country"],medals_quantity=1,gold=winner.medals["gold"],silver=winner.medals["silver"],bronze=winner.medals["bronze"]))
                else: #si el deportista está, actualiza su cantidad de medallas
                    olympic_winner.medals["quantity"] +=1
                    olympic_winner.medals["gold"] += winner.medals["gold"]
                    olympic_winner.medals["silver"] += winner.medals["silver"]
                    olympic_winner.medals["bronze"] += winner.medals["bronze"]

class InformsPrinter(AbstractInformsPrinter):
    def show_all_events(self,list_of_events:AbstractListOfEvents): #muestra el resultado de todos los eventos, con los ganadores de oro, plata y bronce
        print("CLASIFICACIONES POR DISCIPLINA OLÍMPICA:\n")
        for event in list_of_events.events:
            EventSimulator().show_event_winners(event)

    def show_country_ranking(self,inform:AbstractInformsGenerator): #ordena la lista de los países en base a medallas>oro>plata>bronce y la muestra
        if len(inform.country_ranking) !=0:
            print("RANKING DE PAÍSES (según cantidad de medallas y tipo)")
            sorted_countries = sorted(inform.country_ranking,key = lambda x : (x.medals["quantity"],x.medals["gold"],x.medals["silver"],x.medals["bronze"]),reverse=True)
            for country in sorted_countries:
                print(f"País: {country.name}\nMedallas: {country.medals["quantity"]}\n--Oro:{country.medals["gold"]}\n--Plata:{country.medals["silver"]}\n--Bronce:{country.medals["bronze"]}\n")
            inform.country_ranking = []

    def show_winners_ranking(self,inform:AbstractInformsGenerator): #ordena la lista de los deportistas en base a medallas>oro>plata>bronce y la muestra
        if len(inform.winner_ranking) != 0:
            print("RANKING DE DEPORTISTAS DE LOS JUEGOS OLÍMPICOS (según cantidad de medallas y tipo)")
            sorted_olympic_winners = sorted(inform.winner_ranking,key = lambda x : (x.medals["quantity"],x.medals["gold"],x.medals["silver"],x.medals["bronze"]),reverse=True)
            for olympic_winner in sorted_olympic_winners:
                print(f"Nombre:{olympic_winner.data["name"]}\nPaís: {olympic_winner.data["country"]}\nMedallas: {olympic_winner.medals["quantity"]}\n--Oro:{olympic_winner.medals["gold"]}\n--Plata:{olympic_winner.medals["silver"]}\n--Bronce:{olympic_winner.medals["bronze"]}\n")
        inform.winner_ranking = []

# CLASE QUE AGRUPA LAS FUNCIONES PRINCIPALES DEL PROGRAMA
class MainFunctions():
    def __init__(self,event_register:AbstractEventRegister,participant_register:AbstractParticipantRegister,event_simulator:AbstractEventSimulator,generate_informs:AbstractInformsGenerator,print_informs:AbstractInformsPrinter) -> None:
        self.event_register = event_register
        self.particiant_register = participant_register
        self.event_simulator = event_simulator
        self.generate_informs = generate_informs
        self.print_informs = print_informs

    def event_registration(self,list_of_events:AbstractListOfEvents):
        event = Event(input("Dime por favor el nombre de la disciplina olímpica: ").upper())
        self.event_register.event_register(event,list_of_events)
        return list_of_events
    
    def participant_registration(self,list_of_events:AbstractListOfEvents):
        index = None
        event = input("Dime el evento en al que quieres añadir participantes: ").upper()
        index = list_of_events.find_event(event)
        if index != None:
            name = input("Dime el nombre completo del participante: ").title()
            country = input("Y por último el país que representa: ").title()
            self.particiant_register.participant_register(list_of_events.get_event(index),Participant(name,country))
            print("\n")
            return list_of_events

    def simulate_event(self,list_of_events:AbstractListOfEvents):
        index = None
        event = input("¿Qué evento quieres simular?: ").upper()
        index = list_of_events.find_event(event)
        if index != None:
            if not list_of_events.get_event(index).event_completed():
                self.event_simulator.simulate_event(list_of_events.get_event(index))
                self.event_simulator.show_event_winners(list_of_events.get_event(index))
                print("\n")
            else:
                print("El evento ya se ha terminado con el siguiente resultado")
                self.event_simulator.show_event_winners(list_of_events.get_event(index))
                print("\n")

    def inform_generator(self,list_of_events:AbstractListOfEvents):
        self.generate_informs.generate_country_informs(list_of_events)
        self.generate_informs.generate_winner_informs(list_of_events)
        self.print_informs.show_all_events(list_of_events)
        self.print_informs.show_country_ranking(self.generate_informs)
        self.print_informs.show_winners_ranking(self.generate_informs)

#PROGRAMA PRINCIPAL
list_of_events = Events()
main_functions = MainFunctions(EventRegister(),ParticipantRegister(),EventSimulator(),InformsGenerator(),InformsPrinter())
print("\n")
print("--- TE DOY LA BIENVENIDA A LA APLICACIÓN DE LAS OLIMPIADAS DE 2024 ---")
while True:
    option = input("Por favor elige una opción:\n- Registrar un Evento(E)\n- Registrar un Participante(P)\n- Simulación de Eventos(S)\n- Generación de informes(G)\n- Salir(O)\n----> ").upper()
    print("\n")
    if option == "E":
        main_functions.event_registration(list_of_events)
    elif option == "P":
        main_functions.participant_registration(list_of_events)
    elif option == "S":
        main_functions.simulate_event(list_of_events)
    elif option == "G":
        main_functions.inform_generator(list_of_events)
    elif option == "O":
        print("Gracias por usar la app de los Juegos Olímpicos 2024. Hasta pronto")
        break
    else:
        option = input("Tu opción no es válida, prueba de nuevo\n")
