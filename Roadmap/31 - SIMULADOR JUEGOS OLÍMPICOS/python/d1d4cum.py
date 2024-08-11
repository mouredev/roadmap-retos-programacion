import random
from enum import Enum

events = []


class Country(Enum):
    SPAIN = "SP"
    FRANCE = "FR"
    GERMANY = "GER"
    ENGLAND = "EN"
    ITALY = "IT"


class Participant:
    name: str
    country: Country

    def __init__(self, name, country):
        self.name = name
        self.country = country


class Event:
    name: str
    participants: list
    gold: Participant
    silver: Participant
    bronze: Participant

    def __init__(self, name):
        self.name = name
        self.participants = []
        self.gold = None
        self.silver = None
        self.bronze = None

    def simulate(self):
        random.shuffle(self.participants)
        if len(self.participants) >= 3:
            self.gold = self.participants[0]
            self.silver = self.participants[1]
            self.bronze = self.participants[2]
        else:
            print("El número de participantes no es suficiente")


def print_winners(event: Event):
    print(f"\n| {event.name} |")
    try:
        print(f"*** Gold: {event.gold.name} - {event.gold.country}")
        print(f"** Silver: {event.silver.name} - {event.silver.country}")
        print(f"* Bronze: {event.bronze.name} - {event.bronze.country}")
    except Exception as e:
        print(e)
        print("No hay resultados")


def country_ranking():
    countries = {}

    for country in Country:
        countries[country.name] = 0

    for event in events:
        try:
            for medal in [event.gold, event.silver, event.bronze]:
                if medal:
                    match medal.country:
                        case 'IT':
                            countries['ITALY'] += 1
                        case 'SP':
                            countries['SPAIN'] += 1
                        case 'FR':
                            countries['FRANCE'] += 1
                        case 'EN':
                            countries['ENGLAND'] += 1
                        case 'GER':
                            countries['GERMANY'] += 1
        except Exception as e:
            print("⚠️ No se han realizado pruebas aún\n")

    for country, points in countries.items():
        print(f"{country}: {points} points")


def event_registration():
    name = input("\nNombre del evento: ")
    new_event = Event(name=name)
    events.append(new_event)


def paticipant_registration():
    name = input("\nNombre del participante: ")
    country = input("País del participante (SP, FR, GER, EN, IT): ")
    print("Prueba en la que participa: ")

    for event in events:
        print(f"- {event.name}")

    selected_event = input("> ")

    new_participant = Participant(name, country)

    if country == "SP" or country == "FR" or country == "GER" or country == "EN" or country == "IT":

        found = False

        for event in events:
            if event.name == selected_event:
                event.participants.append(new_participant)
                found = True
                break

        if not found:
            print("Prueba no encontrada")
        else:
            print("Participante añadido correctamente")
    else:
        print("País erróneo")


def make_report():
    print("\n---------------")
    print("|   Winners   |")
    print("---------------")

    for event in events:
        print_winners(event)

    print("\n---------------------")
    print("|   Country ranking   |")
    print(" ---------------------")

    country_ranking()


def main():
    quit = False

    while not quit:
        print("\nSelecciona una opción:")
        print("1. Registro de eventos\n"
              "2. Registro de participantes\n"
              "3. Simulación de eventos\n"
              "4. Creación de informes\n"
              "5. Salir del programa")

        option = input("> ")

        match option:
            case "1":
                event_registration()
            case "2":
                paticipant_registration()
            case "3":
                for event in events:
                    event.simulate()
                print("Simulación completada")
            case "4":
                make_report()
            case "5":
                quit = True
            case _:
                print("Opción no válida")


if __name__ == '__main__':
    main()
