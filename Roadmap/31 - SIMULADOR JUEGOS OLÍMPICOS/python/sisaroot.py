# #31 SIMULADOR JUEGOS OLÍMPICOS - SisaRoot

import random
from collections import defaultdict


def shuffle_participants(participants: list) -> list:
    shuffled = participants[:]
    random.shuffle(shuffled)
    return shuffled


class OlympicSimulator:
    def __init__(self):
        self.events: dict[str, list[dict]] = {}
        self.medal_table: dict[str, dict] = defaultdict(lambda: {"gold": 0, "silver": 0, "bronze": 0})
        self.results: list[dict] = []

    def register_event(self):
        name = input("Nombre del evento: ").strip()
        if not name:
            print("Nombre inválido.")
            return
        if name.lower() in (k.lower() for k in self.events):
            print(f"El evento '{name}' ya existe.")
            return
        self.events[name] = []
        print(f"Evento '{name}' registrado.")

    def register_participant(self):
        if not self.events:
            print("No hay eventos registrados. Registra un evento primero.")
            return
        print("Eventos disponibles:")
        event_names = list(self.events.keys())
        for i, ev in enumerate(event_names, 1):
            print(f"  {i}. {ev}")
        try:
            idx = int(input("Selecciona el número del evento: ").strip())
            if not (1 <= idx <= len(event_names)):
                raise ValueError
        except ValueError:
            print("Selección inválida.")
            return
        event_name = event_names[idx - 1]
        participant_name = input("Nombre del participante: ").strip()
        country = input("País del participante: ").strip()
        if not participant_name or not country:
            print("Datos inválidos.")
            return
        self.events[event_name].append({"name": participant_name, "country": country})
        print(f"Participante '{participant_name} ({country})' registrado en '{event_name}'.")

    def simulate_events(self):
        if not self.events:
            print("No hay eventos para simular.")
            return
        self.results.clear()
        for event_name, participants in self.events.items():
            print(f"\n=== Simulando: {event_name} ===")
            if len(participants) < 3:
                print(f"  Necesita al menos 3 participantes (tiene {len(participants)}). Saltando.")
                continue
            shuffled = shuffle_participants(participants)
            gold   = shuffled[0]
            silver = shuffled[1]
            bronze = shuffled[2]
            print(f"  🥇 Oro:    {gold['name']} ({gold['country']})")
            print(f"  🥈 Plata:  {silver['name']} ({silver['country']})")
            print(f"  🥉 Bronce: {bronze['name']} ({bronze['country']})")
            self.medal_table[gold["country"]]["gold"] += 1
            self.medal_table[silver["country"]]["silver"] += 1
            self.medal_table[bronze["country"]]["bronze"] += 1
            self.results.append({
                "event": event_name,
                "gold": gold, "silver": silver, "bronze": bronze,
            })

    def show_report(self):
        print("\n" + "=" * 50)
        print("        INFORME FINAL — JJOO PARÍS 2024")
        print("=" * 50)
        if not self.results:
            print("No se han simulado eventos aún.")
            return
        print("\n📋 GANADORES POR EVENTO:")
        for result in self.results:
            print(f"\n  Evento: {result['event']}")
            print(f"    🥇 {result['gold']['name']} ({result['gold']['country']})")
            print(f"    🥈 {result['silver']['name']} ({result['silver']['country']})")
            print(f"    🥉 {result['bronze']['name']} ({result['bronze']['country']})")
        print("\n🏆 RANKING DE PAÍSES:")
        ranking = sorted(
            self.medal_table.items(),
            key=lambda x: (-x[1]["gold"], -x[1]["silver"], -x[1]["bronze"])
        )
        print(f"{'Pos.':<5} {'País':<25} {'🥇':<6} {'🥈':<6} {'🥉':<6} {'Total':<6}")
        print("-" * 58)
        for pos, (country, medals) in enumerate(ranking, 1):
            total = medals["gold"] + medals["silver"] + medals["bronze"]
            print(f"{pos:<5} {country:<25} {medals['gold']:<6} {medals['silver']:<6} {medals['bronze']:<6} {total:<6}")

    def run(self):
        menu = {
            "1": ("Registrar evento",       self.register_event),
            "2": ("Registrar participante", self.register_participant),
            "3": ("Simular eventos",        self.simulate_events),
            "4": ("Ver informe final",      self.show_report),
            "5": ("Salir",                  None),
        }
        while True:
            print("\n====== SIMULADOR JJOO PARÍS 2024 ======")
            for key, (label, _) in menu.items():
                print(f"{key}. {label}")
            option = input("Selecciona una opción: ").strip()
            if option == "5":
                print("¡Hasta luego!")
                break
            elif option in menu:
                menu[option][1]()
            else:
                print("Opción no válida.")


if __name__ == "__main__":
    OlympicSimulator().run()
