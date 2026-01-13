"""
Programa para simular los JJOO

Requisitos
- Registrar eventos deportivos
- Registrar participantes
- Simular eventos de manera aleatoria en base a los participantes (min 3)
- Asignar medallas (oro, plata y bronce) basandose en el resultado del evento
- Mostrar a los ganadores por cada eventos
- Mostrar el ranking de paises segun el número de medallas
"""

import random
from dataclasses import dataclass, field
from datetime import datetime
from enum import StrEnum


# --- Data Models ---
@dataclass(unsafe_hash=True)
class Participant:
    # --- 1. Atributos de Identidad (Se usan en __eq__ y __hash__) ---
    name: str
    country: str

    # --- 2. Atributos de Estado (Mutables: NO se usan en __eq__ ni __hash__) ---
    # registered_events: Es un set. Necesita su propia fábrica (set()) para no compartirse.
    registered_events: set = field(
        default_factory=set,
        compare=False,
        hash=False,
        repr=False,  # No lo mostramos en el __repr__ por defecto para no ensuciar el log
    )

    # medals: Es un dict. Necesita su propia fábrica lambda.
    medals: dict = field(
        default_factory=lambda: {"Gold": 0, "Silver": 0, "Bronze": 0},
        compare=False,
        hash=False,
        repr=False,
    )

    def add_medal(self, medal_type: str):
        """Método de negocio para añadir medallas."""
        if medal_type in self.medals:
            self.medals[medal_type] += 1

    def __str__(self) -> str:
        """
        Las dataclasses crean un __repr__ automático, pero tú puedes
        definir tu propio __str__ para que se vea bonito en la consola.
        """
        events = ", ".join(e.sport for e in self.registered_events)
        return f"Deportista: {self.name} Pais: {self.country} Eventos registrados: {events}"


@dataclass(unsafe_hash=True)
class Event:
    # --- Identidad ---
    sport: str
    date: datetime

    # --- Estado Mutable (Colecciones) ---
    participants: set = field(
        default_factory=set,  # ¡Vital para que cada evento tenga su propia lista!
        compare=False,
        hash=False,
        repr=False,
    )

    # --- Estado Mutable (Resultados / Nullables) ---
    # Nota: Para valores simples como None, usamos default=None en vez de default_factory
    results: list | None = field(default=None, compare=False, hash=False, repr=False)
    gold: Participant | None = field(default=None, compare=False, hash=False, repr=False)
    silver: Participant | None = field(default=None, compare=False, hash=False, repr=False)
    bronze: Participant | None = field(default=None, compare=False, hash=False, repr=False)

    def __str__(self) -> str:
        date_str = self.date.strftime("%d/%m/%Y")
        return f"Evento: {self.sport} Fecha: {date_str} Nº Participantes: {len(self.participants)}"


@dataclass(unsafe_hash=True)
class Country:
    name: str

    medals: dict = field(
        default_factory=lambda: {"Gold": 0, "Silver": 0, "Bronze": 0},
        compare=False,
        hash=False,
        repr=False,
    )

    def add_medal(self, medal_type: str):
        if medal_type in self.medals:
            self.medals[medal_type] += 1


class ProgramOptions(StrEnum):
    ADD_EVENT = "1"
    ADD_PARTICIPANT = "2"
    SIMULATE_EVENT = "3"
    GET_REPORT = "4"
    EXIT = "5"


# --- Repositories ---
class EventRepository:
    def __init__(self):
        self.event_repo = {}

    def add_event(self, event_sport: str, event_date: datetime) -> Event:
        if event_sport in self.event_repo:
            raise ValueError("El evento ya existe.")

        new_event = Event(event_sport, event_date)
        self.event_repo[event_sport] = new_event
        return new_event

    def get_event(self, name: str) -> Event | None:
        return self.event_repo.get(name)

    def list_events(self) -> list[Event]:
        return list(self.event_repo.values())


class ParticipantRepository:
    def __init__(self):
        self.participant_repo = {}

    def add_participant(self, name: str, country: str) -> Participant:

        key = (name, country)
        if key in self.participant_repo:
            raise ValueError("El participante ya existe.")

        new_participant = Participant(name, country)
        self.participant_repo[key] = new_participant
        return new_participant

    def get_participant(self, name: str, country: str) -> Participant | None:
        return self.participant_repo.get((name, country))

    def list_all_participants(self):
        return self.participant_repo


class CountryRepository:
    def __init__(self):
        self.country_repo = {}

    def add_country(self, name) -> None:
        if name in self.country_repo:
            return

        new_country = Country(name)
        self.country_repo[name] = new_country
        return new_country

    def get_country(self, name) -> Country | None:
        return self.country_repo.get(name)

    def get_ranking(self) -> list[Country]:
        if not self.country_repo:
            return []

        countries = list(self.country_repo.values())
        return sorted(
            countries,
            key=lambda c: (c.medals["Gold"], c.medals["Silver"], c.medals["Bronze"]),
            reverse=True,
        )

    def list_countries(self):
        return self.country_repo


# --- JJOO Manager ---
class JJOO:
    def __init__(
        self,
        event_repo: EventRepository,
        participants_repo: ParticipantRepository,
        country_repo: CountryRepository,
    ):
        self.event_repo = event_repo
        self.participants_repo = participants_repo
        self.country_repo = country_repo

    def register_participant(self, participant: Participant, event: Event) -> None:
        if participant in event.participants:
            raise ValueError("El participante ya está registrado en este evento.")

        event.participants.add(participant)
        participant.registered_events.add(event)

    def simulate_event(self, event: Event) -> list:
        if len(event.participants) < 3:
            raise ValueError(
                "El evento seleccionado no llega al minimo de participantes para simularse"
            )

        participants = list(event.participants)
        random.shuffle(participants)
        event.results = participants

        winner = participants[0]
        winner_country = self.country_repo.get_country(winner.country)
        second = participants[1]
        second_country = self.country_repo.get_country(second.country)
        third = participants[2]
        third_country = self.country_repo.get_country(third.country)

        event.gold = winner
        winner.add_medal("Gold")
        winner_country.add_medal("Gold")

        event.silver = second
        second.add_medal("Silver")
        second_country.add_medal("Silver")

        event.bronze = third
        third.add_medal("Bronze")
        third_country.add_medal("Bronze")

        return participants


# --- View ---
class View:
    def show_menu(self):
        print(
            "1. Registrar eventos deportivos\n"
            "2. Registrar participantes\n"
            "3. Simular eventos\n"
            "4. Crear informes\n"
            "5. Salir del programa\n"
        )

    def get_input(self, prompt: str) -> str:
        return input(prompt)

    def display_msg(self, msg: str) -> None:
        print(f"\n{msg}")

    def display_err(self, err: str) -> None:
        print(f"\nERROR: {err}.")


# --- Controllers ---
class Controller:
    def __init__(
        self,
        view: View,
        games: JJOO,
        event_repo: EventRepository,
        participant_repo: ParticipantRepository,
        country_repo: CountryRepository,
    ):
        self.view = view
        self.games = games
        self.event_repo = event_repo
        self.participant_repo = participant_repo
        self.country_repo = country_repo

    def add_event_handler(self):
        event_name = self.view.get_input("Nombre del evento a registrar: ").strip().title()
        date_str = self.view.get_input("Introduce una fecha para el evento (Ej: dd/mm/yyyy): ")

        try:
            event_date = datetime.strptime(date_str, "%d/%m/%Y")
        except ValueError:
            self.view.display_err("Formato de fecha incorrecto.")
            self.view.display_msg("No se pudo crear el evento")
            return

        try:
            new_event = self.event_repo.add_event(event_name, event_date)
            self.view.display_msg("¡Evento creado con éxito!")
            self.view.display_msg(new_event)
        except ValueError as verr:
            self.view.display_err(verr)

    def add_participant_handler(self) -> None:

        if not self.event_repo.list_events():
            self.view.display_err("No hay eventos deportivos registrados, registra uno primero.")
            return

        participant_name = (
            self.view.get_input("Nombre del participante a registrar: ").strip().title()
        )
        participant_country = self.view.get_input("Pais del participante: ").strip().title()

        participant = self.participant_repo.get_participant(participant_name, participant_country)
        if not participant:
            participant = self.participant_repo.add_participant(
                participant_name, participant_country
            )
            self.view.display_msg("¡Participante añadido con éxito!")

        country = self.country_repo.get_country(participant_country)
        if not country:
            country = self.country_repo.add_country(participant_country)

        self.view.display_msg("Eventos deportivos disponibles")
        for event in self.event_repo.list_events():
            print(event.sport)

        participant_event = self.view.get_input("Evento del participante: ").strip().title()
        event = self.event_repo.get_event(participant_event)

        if not event:
            self.view.display_err("El evento no existe.")
            return

        try:
            self.games.register_participant(participant, event)
            self.view.display_msg(f"¡Participante añadido al evento: {event.sport} con éxito!")

        except ValueError as verr:
            self.view.display_err(
                f"Algo no salio bien al registrar el participante en el evento {event.sport}- {verr}"
            )

    def simulate_event_handler(self) -> None:

        if not self.event_repo.list_events():
            self.view.display_err("No hay eventos deportivos registrados, registra uno primero.")
            return

        self.view.display_msg("Eventos deportivos disponibles para simular")
        for index, event in enumerate(self.event_repo.list_events()):
            print(f"{index + 1}. {event.sport}: (Participantes: {len(event.participants)})")

        self.view.display_msg(" ")

        selected_event = (
            self.view.get_input("Selecciona un evento de los disponibles: ").strip().title()
        )
        event = self.event_repo.get_event(selected_event)

        if not event:
            self.view.display_err("El evento no existe o no esta disponible para simular.")
            return

        try:
            results = self.games.simulate_event(event)

            self.view.display_msg(f"Resultados del evento: {event.sport}\n")
            for index, participant in enumerate(results):
                if index == 0:
                    print(f"{index + 1}. {participant.name} - GOLD")
                elif index == 1:
                    print(f"{index + 1}. {participant.name} - SILVER")
                elif index == 2:
                    print(f"{index + 1}. {participant.name} - BRONZE")
                else:
                    print(f"{index + 1}. {participant.name}")

            self.view.display_msg(" ")

        except ValueError as verr:
            self.view.display_err(verr)
        except Exception as e:
            self.view.display_err(e)

    def get_report_handler(self):

        ranked_countries = self.country_repo.get_ranking()
        if not ranked_countries:
            self.view.display_err("No hay paises registrados en el sistema")
            return

        for event in self.event_repo.list_events():
            print(event)
            if event.gold:
                print(f"\t1. {event.gold.name}")
                print(f"\t2. {event.silver.name}")
                print(f"\t3. {event.bronze.name}")
                print("\n*********************************************\n")
            else:
                print("\t- El evento no se ha simulado por el momento.\n")
                print("\n*********************************************\n")

        self.view.display_msg("RANKING DE PAISES")
        print(f"{'PAÍS':<15} | {'ORO':<5} | {'PLATA':<5} | {'BRONCE':<5}")
        print("-" * 45)
        for index, country in enumerate(ranked_countries):
            country_cell = f"{index + 1}. {country.name}"
            print(
                f"{country_cell:<15} | "
                f"{country.medals['Gold']:<5} | "
                f"{country.medals['Silver']:<5} | "
                f"{country.medals['Bronze']:<5}"
            )
        print("-" * 45)


# --- Main Flow ---
def main():
    try:
        view = View()
        event_repo = EventRepository()
        participants_repo = ParticipantRepository()
        country_repo = CountryRepository()
        games = JJOO(event_repo, participants_repo, country_repo)

        controller = Controller(view, games, event_repo, participants_repo, country_repo)
        print("Simulador de Juegos Olimpicos.\n")

    except Exception as e:
        view.display_err(f"Error al iniciar - {e}")

    while True:
        try:
            view.show_menu()
            option = ProgramOptions(view.get_input("Elige una opcion de las anteriores: "))

            match option:
                case ProgramOptions.ADD_EVENT:
                    controller.add_event_handler()
                case ProgramOptions.ADD_PARTICIPANT:
                    controller.add_participant_handler()
                case ProgramOptions.SIMULATE_EVENT:
                    controller.simulate_event_handler()
                case ProgramOptions.GET_REPORT:
                    controller.get_report_handler()
                case ProgramOptions.EXIT:
                    view.display_msg("Saliendo del programa ...\n")
                    break

        except ValueError:
            view.display_err("Opcion no válida, pruebe otra vez.")
        except Exception as e:
            view.display_err(f"Error en el flujo repetitivo - {e}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error inesperado en el arranque - {e}.")
