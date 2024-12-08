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
from typing import Literal


class Participant:
    def __init__(self, name: str, country: str):
        self.name = name
        self.country = country

    def __eq__(self, other: object) -> bool:
        """Indicates to the Participant class when two instances are equals.

        Parameters
        ----------
        other : object
            The second object with which the current instance must be compared.

        Returns
        -------
        bool
            Whether the both objects are equals.
        """

        if isinstance(other, Participant):
            return self.name == other.name and self.country == other.country

        return False

    def __hash__(self) -> int:
        return hash(self.name, self.country)


class Olympics:
    def __init__(self):
        self.events: list[str] = []
        self.participants: dict[str, list[Participant]] = dict()
        self.results: dict[
            str, dict[Literal["gold", "silver", "bronze"], Participant]
        ] = dict()
        self.countries: dict[
            str, dict[Literal["gold", "silver", "bronze"], int]
        ] = dict()

    def add_event(self):
        """Asks the user for an event name and adds it to the events list if it
        didn't exist already."""

        event: str = input("Introducer el nombre del evento:\n > ").strip()

        if event in self.events:
            print(f"El evento '{event}' ya ha sido añadido anteriormente.")
        else:
            self.events.append(event)
            print(f"El evento '{event}' ha sido añadido.")

    def add_participant(self):
        """Asks the user for the name and the country of a participant. If
        there are not events yet, it won't be possible to add a participant. A
        participant can't be added to the same event twice."""

        if not self.events:
            print(
                "No existen eventos todavía. Espera a que haya alguno para inscribirte!"
            )
            return

        # Get participant's information
        name: str = input("Introduce el nombre del participante:\n > ").strip()
        country: str = input(
            "Introduce el país del participante:\n > "
        ).strip()
        participant: Participant = Participant(name, country)

        # Register the participant in an event
        event_choice: int = menu(
            options=self.events,
            prompt="Selecciona en qué evento deseas participar: ",
        )
        event: str = self.events[event_choice]

        if (
            event in self.participants
            and participant in self.participants[event]
        ):
            print(
                f"El participante {name} de {country} ya está registrado en el evento deportivo {event}."
            )
        else:
            if event not in self.participants:
                self.participants[event] = []

            self.participants[event].append(participant)
            print(
                f"El participante {name} de {country} se ha registrado en {event}."
            )

    def simulate(self):
        """Simulates the games by picking the gold, silver and bronze
        participants and updates the results."""

        if not self.events:
            print("Aún no hay eventos registrados.")

        for event in self.events:
            if (
                event not in self.participants
                or len(self.participants[event]) < 3
            ):
                print(
                    f"No hay participantes suficientes para simular el evento {event}."
                )
                continue

            # Get Golden, Silver and Bronze randomly
            event_participants: list[Participant] = random.sample(
                self.participants[event], 3
            )
            random.shuffle(event_participants)

            gold, silver, bronze = event_participants
            winners = {
                "gold": gold,
                "silver": silver,
                "bronze": bronze,
            }
            self.results[event] = winners

            # Update each country's medal counter
            self._update_country_results(gold.country, "gold")
            self._update_country_results(silver.country, "silver")
            self._update_country_results(bronze.country, "bronze")

            self._print_results(event, winners)

    def write_summary(self):
        """Prints a summary of the results into the console."""

        print("\nINFORME DE LOS JJOO")
        print("-------------------\n")

        if not self.results:
            print("No hay resultados registrados.")
        else:
            for event, winners in self.results.items():
                self._print_results(event, winners)

        if not self.countries:
            print("No hay medallas por país registradas.")
        else:
            for country, medals in self.countries.items():
                print(f"{country}:")
                print(f"  {medals['gold']} Oro")
                print(f"  {medals['silver']} Plata")
                print(f"  {medals['bronze']} Bronce")

    def _update_country_results(
        self, country: str, medal: Literal["gold", "silver", "bronze"]
    ):
        """Updates the countries' medal quantities.

        Parameters
        ----------
        country : str
            The name of the country.
        medal : Literal["gold", "silver", "bronze"]
            The type of medal the country has won.
        """

        if not country in self.countries:
            self.countries[country] = {"gold": 0, "silver": 0, "bronze": 0}

        self.countries[country][medal] += 1

    def _print_results(
        self,
        event: str,
        winners: dict[Literal["gold", "silver", "bronze"], Participant],
    ):
        """Prints the received results, showing the event name and who are the
        winners of it.

        Parameters
        ----------
        event : str
            The event name.
        winners : dict[Literal["gold", "silver", "bronze"], Participant]
            The winners' names and countries.
        """

        print(f"RESULTADOS DEL EVENTO:", event)
        print(f"Oro: {winners['gold'].name} ({winners['gold'].country})")
        print(f"Plata: {winners['silver'].name} ({winners['silver'].country})")
        print(
            f"Bronce: {winners['bronze'].name} ({winners['bronze'].country})"
        )


def menu(
    options: list[str], prompt: str = "Selecciona qué quieres hacer: "
) -> int:
    """Prints a sequence of options and asks the user to choose one of them.

    Parameters
    ----------
    options : list[str]
        A list that contains the available options.

    Returns
    -------
    int
        The index of the selected option.
    """

    while True:
        print("\nMENÚ DE OPCIONES")
        print("----------------")
        for index, option in enumerate(options):
            print(f"{index + 1}. {option}")

        try:
            chosen: str = input(prompt)
            assert chosen.isnumeric()
        except:
            print(f"Debes introducir un número entre [1-{len(options)}]!")
        else:
            chosen: int = int(chosen)
            if chosen >= 1 and chosen <= len(options):
                print()
                return chosen - 1  # chosen option's index


if __name__ == "__main__":
    OPTIONS: list[str] = [
        "Registro de eventos",
        "Registro de participantes",
        "Simulación de eventos",
        "Creación de informes",
        "Salir del programa",
    ]
    jjoo = Olympics()

    while True:
        chosen_option: int = menu(OPTIONS)

        if chosen_option == 0:
            jjoo.add_event()
        elif chosen_option == 1:
            jjoo.add_participant()
        elif chosen_option == 2:
            jjoo.simulate()
        elif chosen_option == 3:
            jjoo.write_summary()
        elif chosen_option == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")
