# @Author Daniel Grande (Mhayhem)

import random
from abc import ABC, abstractmethod

# EJERCICIO:
# ¡Los JJOO de París 2024 han comenzado!
# Crea un programa que simule la celebración de los juegos.
# El programa debe permitir al usuario registrar eventos y participantes,
# realizar la simulación de los eventos asignando posiciones de manera aleatoria
# y generar un informe final. Todo ello por terminal.
# Requisitos:
# 1. Registrar eventos deportivos.
# 2. Registrar participantes por nombre y país.
# 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
# 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
# 5. Mostrar los ganadores por cada evento.
# 6. Mostrar el ranking de países según el número de medallas.
# Acciones:
# 1. Registro de eventos.
# 2. Registro de participantes.
# 3. Simulación de eventos.
# 4. Creación de informes.
# 5. Salir del programa.

# // class //

# athlete instance
class Athlete:
    # athelte init
    def __init__(self, name : str, surname: str, country: str):
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.country = country.capitalize()
    # display athlete info
    def __str__(self):
        return f"Nombre: {self.name} {self.surname}; Pais {self.country}"


class OlimpicEvents:
    def __init__(self):
        self.participants = []
        self.event = []
        self.medals = {}
        
    def register_participants(self):
        print("Registro de participantes.")
        while len(self.participants) < 5:
            name = input("Nombre:\n")
            surname = input("Apellido:\n")
            country = input("País:\n")
            
            if name and surname and country:
                athlete = Athlete(name, surname, country)
                self.participants.append(athlete)
            else:
                print("Ninguna entrada puede estar vacía.")
        
        self.medals = {person.country : 0 for person in self.participants}
            
    def register_event(self):
        print("Registro de eventos.")
        while len(self.event) < 3:
            event = input("Evento:\n")
            if event and event not in self.event:
                self.event.append(event)
            else:
                print("Evento ya registrado o no has escrito nada.")
    
    def events_simulator(self):
        events_copy = self.event
        for event in events_copy:
            print(f"El evento {event} va ha comenzar.")
            print("*" * 40)
            events_copy.remove(event)
            gold, silver, bronze = random.sample(self.participants, 3)
            print(f"Oro: {gold.name}, plata: {silver.name} y bronce: {bronze.name}")
            print("*" * 40)
            
            self.medals[gold.country] += 1
            self.medals[silver.country] += 1
            self.medals[bronze.country] += 1
    
    def display_report(self):
        print("Tabla de medallas por pais")
        print(f"{"=" * 10} MEDALS {"=" * 10}")
        for k, v in self.medals.items():
            print(f"{k}: {v}")


def main():
    print("1. Registrar eventos(3 por registro).\n"
        "2. Registrar participantes(5 por registro).\n"
        "3. Simular los eventos.\n"
        "4. Mostrar informes.\n"
        "5. Cerrar programa.")
    
    olimpics = OlimpicEvents()
    
    while True:
        try:
            option = int(input())
        except ValueError:
            print("Debes introducir solo números (del 1 al 5)")
            continue
        
        match option:
            case 1:
                olimpics.register_event()
            case 2:
                olimpics.register_participants()
            case 3:
                olimpics.events_simulator()
            case 4:
                olimpics.display_report()
            case 5:
                print("Cerrando programa.")
                break