import random


class Participant:

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Participant):
            return self.name == other.name and self.country == other.country
        return False

    def __hash__(self) -> int:
        return hash(self.name, self.country)


class Olympics():

    def __init__(self):
        self.events = []
        self.participants = {}
        self.event_results = {}
        self.country_results = {}

    def register_event(self):
        event = input("Introduce nombre del evento: ").strip()

        if (event in self.events):
            print(f"Evento {event} ha sido registrado anteriormente")
        else:
            self.events.append(event)
            print(f"Evento {event} ha sido registado.")

    def register_participant(self):
        if not self.events:
            print("No existen eventos. Por favor, registra un evento deportivo.")
            return
        name = input("Introduce el nombre del participante: ").strip()
        country = input("País del participante: ").strip()
        participant = Participant(name, country)

        print("Eventos deportivvos disponibles: ")
        for index, event in enumerate(self.events):
            print(f"{index+1}. {event}")

        event_choice = int(
            input("Selecciona el número del evento para asignar al participante: ")) - 1

        if event_choice >= 0 and event_choice < len(self.events):
            event = self.events[event_choice]

            if event in self.participants and participant in self.participants[event]:
                print(
                    f"El participante {name} de {country} ya está registrado en el evento deportivo {event}")
            else:
                if event not in self.participants:
                    self.participants[event] = []
                self.participants[event].append(participant)
                print(
                    f"El participante {name} de {country} se ha registrado en el evento deportivo {event}")
        else:
            print("El evento deporivo es inválido. El participante no se ha registrado")

    def simulate_event(self):
        if not self.events:
            print("No hay eventos. Por favor registra un evento.")
            return

        for event in self.events:
            if len(self.participants[event]) < 3:
                print("Participantes insuficientes, se necesitan al menos 3")
                continue

            event_participants = random.sample(self.participants[event], 3)
            random.shuffle(event_participants)
            gold, silver, bronze = event_participants
            self.event_results[event] = [gold, silver, bronze]

            self.update_country_results(gold.country, "gold")
            self.update_country_results(silver.country, "silver")
            self.update_country_results(bronze.country, "bronze")

            print(f"Resultados simulación del evento: {event}")
            print(f"Oro: {gold.name} ({gold.country})")
            print(f"Plata: {silver.name} ({silver.country})")
            print(f"Bronce: {bronze.name} ({bronze.country})")

    def update_country_results(self, country, medal):
        if country not in self.country_results:
            self.country_results[country] = {
                "gold": 0, "silver": 0, "bronze": 0}
        self.country_results[country][medal] += 1

    def report(self):
        print("Informe JJOO Paris 2024")
        if self.event_results:
            print("Informe por evento")
            for event, winners in self.event_results.items():
                print(f"Evento: {event}")
                print(f"Oro: {winners[0].name} ({winners[0].country})")
                print(f"Plata: {winners[1].name} ({winners[1].country})")
                print(f"Bronce: {winners[2].name} ({winners[2].country})")
        else:
            print("No hay resultados registrados.")

        if self.country_results:
            print("\nInforme por país:")
            for country, medals in sorted(self.country_results.items(), key=lambda x: (
                    x[1]["gold"], x[1]["silver"], x[1]["bronze"]), reverse=True):
                print(
                    f"{country}: Oro {medals['gold']}, Plata {medals['silver']}, Bronce {medals['bronze']}")
        else:
            print("No hay medallas por país registradas.")


olympics = Olympics()
while True:
    print("""\n Simulador de Juegos Olimpicos
    1. Registro de eventos.
    2. Registro de participantes.
    3. Simulación de eventos.
    4. Creación de informes.
    5. Salir""")

    option = input("Selecciona una acción: ")

    match option:
        case "1":
            olympics.register_event()
        case "2":
            olympics.register_participant()
        case "3":
            olympics.simulate_event()
        case "4":
            olympics.report()
        case "5":
            print("Gracias por simular...")
            break
        case _:
            print("opción no encontrada")
