from enum import Enum
import random

eventos = []

class Pais(Enum):
    ESPANA = "SP"
    FRANCIA = "FR"
    ELEMANIA = "GR"
    ITALIA = "IT"
    PERU = "PE"
    INGLATERRA = "EN"

class Participante:
    def __init__(self, nombre: str, pais: Pais) -> None:
        self.nombre = nombre
        self.pais = pais

class Evento:
    oro: Participante
    plata: Participante
    bronce: Participante

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.participantes = []
        self.oro = None
        self.plata = None
        self.bronce = None

    def simulacion(self):
        random.shuffle(self.participantes)
        if len(self.participantes) >= 3:
            self.oro = self.participantes[0]
            self.plata = self.participantes[1]
            self.bronce = self.participantes[2]
        else:
            print("El número de participantes insuficiente")


def ganadores(evento: Evento):
    print(f"\n| {evento.nombre} |")
    try:
        print(f"*** Gold: {evento.oro.nombre} - {evento.oro.pais}")
        print(f"** Silver: {evento.plata.nombre} - {evento.plata.pais}")
        print(f"* Bronze: {evento.bronce.nombre} - {evento.bronce.pais}")
    except Exception as e:
        print(e)
        print("No hay resultados")


def ranking_paises():
    paises = {}

    for pais in Pais:
        paises[pais.name] = 0

    for evento in eventos:
        try:
            for medalla in [evento.oro, evento.plata, evento.bronce]:
                if medalla:
                    match medalla.pais:
                        case 'IT':
                            paises['ITALIA'] += 1
                        case 'SP':
                            paises['ESPANA'] += 1
                        case 'FR':
                            paises['FRANCIA'] += 1
                        case 'EN':
                            paises['INGLATERRA'] += 1
                        case 'GER':
                            paises['ALEMANIA'] += 1
                        case 'PE':
                            paises['PERU'] += 1
        except Exception as e:
            print("No hay pruebas aún\n")

    for pais, points in paises.items():
        print(f"{pais}: {points} puntos")


def registro_evento():
    nombre = input("\nNombre del evento: ")
    nuevo_evento = Evento(nombre=nombre)
    eventos.append(nuevo_evento)


def registro_participante():
    nombre = input("\nNombre del participante: ")
    pais = input("País del participante (SP, FR, GER, EN, IT, PE): ")
    print("Prueba en la que participa: ")

    for evento in eventos:
        print(f"- {evento.nombre}")

    selected_event = input("> ")

    new_participant = Participante(nombre, pais)

    if pais == "SP" or pais == "FR" or pais == "GER" or pais == "EN" or pais == "IT" or pais == "PE":

        found = False

        for evento in eventos:
            if evento.nombre == selected_event:
                evento.participantes.append(new_participant)
                found = True
                break

        if not found:
            print("Prueba no encontrada")
        else:
            print("Participante añadido correctamente")
    else:
        print("País erróneo")


def reporte():
    print("\n---------------")
    print("|   Winners   |")
    print("---------------")

    for evento in eventos:
        ganadores(evento)

    print("\n---------------------")
    print("|   Country ranking   |")
    print(" ---------------------")

    ranking_paises()


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
                registro_evento()
            case "2":
                registro_participante()
            case "3":
                for evento in eventos:
                    evento.simulacion()
                print("Simulación completada")
            case "4":
                reporte()
            case "5":
                quit = True
            case _:
                print("Opción no válida")


if __name__ == '__main__':
    main()
