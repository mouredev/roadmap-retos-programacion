import random


class Participant:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Participant):
            return False
        return self.name == other.name and self.country == other.country

    def __hash__(self) -> int:
        return hash(self.name, self.country)


class Olympics:
    def __init__(self):
        self.events = []
        self.participants = {}
        self.event_results = {}
        self.country_results = {}

    def register_event(self):
        event = input(
            "Introducir nombre del evento deportivo: ").strip().lower()
        if event not in self.events:
            self.events.append(event)
            self.participants[event] = []  # crear la clave del evento vacía
            # Inicializar la lista de participantes
            # self.participants[event] = []
            print(f"✅ El evento --{event}-- registrado OK")
        else:
            print(f"❌ El evento --{event}-- ya existe")

    def register_participant(self):
        if not self.events:
            print("❌No hay eventos registrados. Por favor, registra uno")
            return

        name = input("Introducir nombre participante: ").strip().capitalize()
        country = input(
            "Introducir país del participante: ").strip().capitalize()
        participant = Participant(name, country)

        print("🔹Eventos disponibles para registrar el participante: ")
        for index, event in enumerate(self.events):
            print(f"{index + 1}.-  {event}")
        event_choice = int(
            input(f"Selecciona el nro del evento para {name}: ")) - 1
        if event_choice >= 0 and event_choice < len(self.events):
            event = self.events[event_choice]
            '''if event not in self.participants:
                self.participants[event] = []'''
            if participant in self.participants[event]:
                print(
                    f"❌El participante {name} de {country} ya está registrado en el evento deportivo {event}")
            else:
                self.participants[event].append(participant)
                print(
                    f"✅El participante {name} de {country} se ha registrado en el evento deportivo {event}")
        else:
            print(f"❌ Evento deportivo inválido")

    def simulate_events(self):
        if not self.events:
            print("❌ No hay eventos registrados.")
            return
        for event in self.events:

            count_participants = len(self.participants[event])
            if count_participants < 3:
                print(
                    f"💥 Solo hay {count_participants} para el evento {event}, debe haber al menos 3 ")
                continue
            # me quedo al azar con sólo 3 participantes para el oro plata cobre
            event_winner_particpants = random.sample(
                self.participants[event], 3)
            # ordenarlo de manera aleatoria
            random.shuffle(event_winner_particpants)
            # asigno a cada medalla los participantes
            gold, silver, bronze = event_winner_particpants
            self.event_results[event] = [gold, silver, bronze]

            # medallero por país
            self.update_country_results(gold.country, "gold")
            self.update_country_results(silver.country, "silver")
            self.update_country_results(bronze.country, "bronze")

            print(f"🥇🥈🥉 Resultados Simulación del evento: {event}")
            print(f"🥇 ORO: {gold.name} ({gold.country})")
            print(f"🥈 PLATA: {silver.name} ({silver.country})")
            print(f"🥉 BRONCE: {bronze.name} ({bronze.country})")

    def update_country_results(self, country, medal):
        if country not in self.country_results:
            self.country_results[country] = {
                "gold": 0, "silver": 0, "bronze": 0}
        self.country_results[country][medal] += 1

    def show_report(self):
        print("Informe JJOO")
        if self.event_results:

            for event, winners in self.event_results.items():
                print(f"🏁 Evento: {event}")
                print(f"🥇 ORO: {winners[0].name} ({winners[0].country})")
                print(f"🥈 PLATA: {winners[1].name} ({winners[1].country})")
                print(f"🥉 BRONCE: {winners[2].name} ({winners[2].country})")
        else:
            print("Sin resultados de eventos")

        if self.country_results:
            sorted_countries = sorted(self.country_results.items(), key=lambda x: (
                x[1]["gold"], x[1]["silver"], x[1]["bronze"]), reverse=True)

            for country, medals in sorted_countries:
                print(
                    f"🏁 País: {country} - 🥇 ORO: {medals["gold"]} - 🥈 PLATA: {medals["silver"]} - 🥉 BRONCE: {medals["bronze"]}")
        else:
            print("Sin resultados por país")


olympics = Olympics()

print("Simulador de JJOO")

while True:
    print()
    print(" * 1. Registro de eventos.")
    print(" * 2. Registro de participantes.")
    print(" * 3. Simulación de eventos.")
    print(" * 4. Creación de informes.")
    print(" * 5. Salir del programa.")

    option = input("Seleccione una opción: ")
    match option:
        case "1":
            olympics.register_event()
        case "2":
            olympics.register_participant()
        case "3":
            olympics.simulate_events()
        case "4":
            olympics.show_report()
        case "5":
            print("Saliendo del programa.")
            break
        case _:
            print("Opción no válida. Intente nuevamente.")
