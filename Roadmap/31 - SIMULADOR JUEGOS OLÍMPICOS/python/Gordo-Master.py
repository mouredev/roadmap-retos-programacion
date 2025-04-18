from abc import ABC, abstractmethod
import os, time


# Definiendo las clases de competidor y evento
class Competitor():

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Competitor):
            return self.name == other.name and self.country == other.country
        return False
    
    def __hash__(self):
        return hash((self.name,self.country))

class Event():

    def __init__(self, name):
        self.name = name
        self.competitors = set()
        self.results = dict()

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Event):
            return self.name == other.name
        return False
    
    def __hash__(self):
        return hash(self.name)
    
    def add_competitor(self, competitor: Competitor):
        self.competitors.add(competitor)
    
    def enough_competitors(self) -> bool:
        if len(self.competitors) >= 3:
            return True
        else:
            return False

    def event_simulator(self):
        for num, person in enumerate(self.competitors):
            self.results[num+1] = person
        
        return [self.results[1],self.results[2],self.results[3]]
    


# Definiendo el metodo de registar
class Registration(ABC):

    @abstractmethod
    def register(self, data, recorder):
        pass

# Asignando metodos de mas bajo nivel de acuerdo a una abstracción
class CompetitorRegistration(Registration):

    def register(self, data: Competitor, recorder: Event):
        if data in recorder.competitors:
            print("El participante ya existe en esta prueba")
        else:
            recorder.add_competitor(data)
            print("Competidor agregado exitosamente")

class EventRegistration(Registration):

    def register(self, data: Event, recorder: list):
        if data in recorder:
            print("El evento ya existe")
        else:
            recorder.append(data)
            print("Evento agregado exitosamente")


# Funcion que se repite
def error_return_init(text):
    print(f"{text}\nRegresando al menu inicial")
    time.sleep(1.8)


# Clase que va manejar toda la logica. De nivel superior

class Olimpycs():

    def __init__(self):
        self.events = []
        self.country_results= {}

    
    def event_register(self):
        EventRegistration().register(Event(input("Nombre del evento:").strip()), self.events)
        
        input("[*] Presione enter para continuar...")

    def competitor_register(self):

        if not self.events:
            return error_return_init("No hay eventos registrados")

        self.events.sort(key= lambda x: x.name)

        print("Eventos:") 
        for num, i in enumerate(self.events):
            print (f"{num + 1 }.{i.name}")

        try:
            number = int(input("Elige el numero del evento: "))-1
        except:
            error_return_init("Valor invalido")
        else:
            if number < 0 or number >= len(self.events) :
                error_return_init(f"Valor invalido. Debe ser un numero entre 1 y {len(self.events)}")

            else:        
                name = input("Nombre del participante: ").strip()
                country = input("Nacionalidad: ").strip()
                CompetitorRegistration().register(Competitor(name, country),self.events[number])
                input("[*] Presione enter para continuar...")
                


    def country_count_medals(self, medals:list):
        for num, med in enumerate(medals):
            if med.country not in self.country_results:
                self.country_results[med.country] = {
                    "gold" : 0,
                    "silver" : 0,
                    "bronze" : 0
                }
            match num:
                case 0:
                    self.country_results[med.country]["gold"] += 1
                case 1:
                    self.country_results[med.country]["silver"] += 1
                case 2:
                    self.country_results[med.country]["bronze"] += 1

    def event_simulator(self):

        flag = False

        if not self.events:
            return error_return_init("No hay eventos registrados")
        

        for event in self.events:
            if not event.enough_competitors():
                print(f"No hay suficiente competidores para {event.name}! (3 participantes mínimos)")
                input("Presione enter para continuar...")
                continue

            flag = True

            list_medals = event.event_simulator()

            self.country_count_medals(list_medals)
        
        if flag:
            input("Simulación concluida con exito!")


    def show_report(self):
        print("Informe de resultados:")
        if self.events:
            for event in self.events:
                
                print(f"\nEvento: {event.name}")
                if not event.enough_competitors():
                    print(f"No hay suficiente competidores para {event.name}! (3 participantes mínimos)")
                    continue

                for position, competitor in event.results.items():
                    
                    print(f"Puesto {position}: {competitor.name}, {competitor.country}")
        else: 
            print("\nNo hay resultados registrados.")

        input("Presione enter para continuar...")

        print("Informe de medallas por paises")

        if self.country_results:

            for country, valor in sorted(self.country_results.items(), key = lambda x: (x[1]["gold"],x[1]["silver"],x[1]["bronze"]), reverse= True):
                print(f"{country}: \nGold: {valor["gold"]}{" "*4}Plate: {valor["silver"]}{" "*4}Bronce: {valor["bronze"]}")

        else:
            input("\nNo hay medallas por pais registrados.")

        input("Presione enter para continuar...")


oojj = Olimpycs()

# Función principal
def main():
    text = """Acciones:
1. Registro de eventos.
2. Registro de participantes.
3. Simulación de eventos.
4. Creación de informes.
5. Salir del programa."""

    while True:
        os.system("cls")
        print(text)
        option = input("\nElige un opción (número):")
        match option:

            case "1":
                oojj.event_register()

            case "2":
                oojj.competitor_register()

            case "3":
                oojj.event_simulator()

            case "4":
                oojj.show_report()

            case "5":
                print("[+] Saliendo del programa...")
                break
            case _:
                error_return_init("El valor es incorrecto. \nDebe ser un valor entre 1 - 5.")


if __name__ == "__main__":
    main()