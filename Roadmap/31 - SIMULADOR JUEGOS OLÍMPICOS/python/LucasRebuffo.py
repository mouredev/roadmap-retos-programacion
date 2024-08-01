import random
from typing import List


class Event:

    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.participants: List[Participant] = []

    def simular(self):
        if len(self.participants) < 3:
            print(f"Falta {len(self.participants) - 3 } participante|s mas")
        else:
            random.shuffle(self.participants)
            self.participants[0].oro += 1
            self.participants[1].plata += 1
            self.participants[2].bronce += 1

            print(f"Evento {self.nombre} simulado")
            print("Podio: ")
            print(f"1 - {self.participants[0].nombre}")
            print(f"2 - {self.participants[1].nombre}")
            print(f"3 - {self.participants[2].nombre}")
            print("\n")

    def agregarParticipante(self, *participantes):

        for participant in participantes:
            self.participants.append(participant)


class Participant:

    def __init__(self, nombre, pais) -> None:
        self.nombre = nombre
        self.pais = pais
        self.oro = 0
        self.plata = 0
        self.bronce = 0

    def __str__(self) -> str:
        print(f"Nombre: {self.nombre} > Nacionalidad: {self.pais}")


participant1 = Participant("lucas", "Argentina")
participant2 = Participant("gaston", "España")
participant3 = Participant("jose", "España")
participant4 = Participant("marta", "Argentina")
participant5 = Participant("belen", "Uruguay")
participant6 = Participant("jhon", "EEUU")
participant7 = Participant("steven", "EEUU")
participant8 = Participant("ahmed", "Arabia")
participant8 = Participant("maria", "Arabia")
participant9 = Participant("sheila", "Uruguay")
participant10 = Participant("gertha", "Alemania")
participant11 = Participant("hunter", "Alemania")
participant12 = Participant("igor", "Rusia")
participant13 = Participant("katrina", "Rusia")


evento1 = Event("Evento1")
evento1.agregarParticipante(participant1, participant2, participant3, participant4)
evento2 = Event("Evento2")
evento2.agregarParticipante(participant5, participant6, participant7, participant8)
evento3 = Event("Evento3")
evento3.agregarParticipante(
    participant9, participant10, participant11, participant12, participant13
)

eventos = [evento1, evento2, evento3]


def info_evento(evento: Event):
    print(f"Nombre de evento: {evento.nombre}")
    for participante in evento.participants:
        print(participante.nombre)
    print("---------------------------------\n")


def mostrar_ganadores():
    for evento in eventos:
        print(f"Evento: {evento.nombre} Ganador: {evento.participants[0].nombre}")
        print(f"Evento: {evento.nombre} Segundo: {evento.participants[1].nombre}")
        print(f"Evento: {evento.nombre} Tercero: {evento.participants[2].nombre}")
    print("\n")


def mostrar_ranking():
    participantes = []
    for evento in eventos:
        participantes.extend(evento.participants)

    paises = list(set(map(lambda x: x.pais, participantes)))
    paises = list((map(lambda x: {"pais": x, "contador": 0}, paises)))

    participantes = list(map(
        lambda x: {"pais": x.pais, "cant_medallas": x.oro + x.plata + x.bronce},
        participantes,
    ))

    ranking = []

    for pais in paises:
        for partcipante in participantes:
            if pais["pais"] == partcipante["pais"]:
                pais["contador"] += partcipante["cant_medallas"]
        ranking.append(pais)

    pos = 1

    ranking = sorted(ranking,key=lambda x: x["contador"],reverse=True)

    for pais in ranking:
        print(f"{pos} - {pais["pais"]}. Coantidad de medallas: {pais["contador"]}")
        pos += 1

    print("\n")
def celebrar_juegos():

    while True:

        print("1 - Registrar evento")
        print("2 - Registrar participante")
        print("3 - Simular eventos")
        print("4 - Crear informe")
        print("5 - Mostrar estado de eventos")
        print("6 - Salir")
        print("\n")

        op = int(input("Ingresa un valor\n"))
        print("\n")

        match op:
            case 1:
                nombre = input("Ingrese nombre de evento: \n")
                eventos.append(Event(nombre))

            case 2:
                nombre_evento = input("Ingrese nombre de evento: \n")
                nombre_participante = input("Ingrese nombre de participante: \n")
                pais_participante = input("Ingrese pais de participante: \n")

                evento: Event = filter(lambda x: x.nombre == nombre_evento, eventos)
                evento.agregarParticipante(
                    Participant(nombre_participante, pais_participante)
                )
            case 3:
                for evento in eventos:
                    evento.simular()
            case 4:
                mostrar_ganadores()
                mostrar_ranking()
            case 5:
                for evento in eventos:
                    info_evento(evento)
            case 6:
                break
            case _:
                print("Operacion no valida")


celebrar_juegos()



