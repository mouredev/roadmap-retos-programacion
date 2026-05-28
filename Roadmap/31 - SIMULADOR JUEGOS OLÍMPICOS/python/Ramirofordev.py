'''
Ejercicio:
Crea un programa que simule la celebracion de los juegos.

El programa debe permitir al usuario registrar eventos y participantes, realizar la simulacion de los eventos asignando posiciones de manera aleatoria y generar un informe final. Todo ello por terminal.

Requisitos:
    1. Registrar eventos deportivos.
    2. Registrar participantes por nombre y país.
    3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
    4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
    5. Mostrar los ganadores por cada evento.
    6. Mostrar el ranking de países según el número de medallas.

Acciones: 
    1. Registro de eventos.
    2. Registro de participantes.
    3. Simulación de eventos.
    4. Creación de informes.
    5. Salir del programa.
'''
import random

class Evento:
        def __init__(self, n_participantes: int, nombre: str):
            self.n_participantes = n_participantes
            self.nombre = nombre
            self.resultados = []

class Participante:
    def __init__(self, nombre: str, pais: str):
        self.nombre = nombre
        self.pais = pais

# Creamos un singleton
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
            

# Creamos un manager usando singleton que tenga las listas de los eventos y participantes
class OlympicManager(metaclass = SingletonMeta):
    def __init__(self):
        self.eventos = []
        self.participantes = []

manager = OlympicManager()

def menu():
    while True:
        print("Bienvenido a los juegos olimpicos. Escoja una de las siguientes opciones: \n"\
        "1. Registrar un nuevo evento.\n" \
        "2. Registrar un nuevo participante.\n"\
        "3. Simulacion de eventos.\n"\
        "4. Creacion de informes.\n"\
        "5. Salir del programa.")
        opcion = int(input("> "))

        return opcion

def registrar_evento():
    n_participantes = int(input("Por favor inserte el numero de participantes: "))
    nombre = input("Por favor inserte el nombre del evento: ").strip()

    if n_participantes < 3:
        print("El evento debe tener al menos 3 participantes.")
        return

    evento = Evento(n_participantes, nombre)
    manager.eventos.append(evento)
    print(f"Evento '{nombre}' registrado correctamente.")

def registrar_participante():
    nombre = input("Inserte el nombre del participante: ")
    pais = input("Inserte el pais del participante: ")

    participante = Participante(nombre, pais)
    manager.participantes.append(participante)
    print(f"Participante '{nombre}' agregado.")

def simular_evento():

    # Validar que existan eventos antes de simular.
    if not manager.eventos:
        print("No hay eventos registrados.")
        return

    # Verificar que existan participantes suficientes
    if len(manager.participantes) < 3:
        print("No hay suficientes participantes para la simulacion (minimo 3).")
        return
    
    for idx, evento in enumerate(manager.eventos, 1):
        print(f"{idx}. {evento.nombre} ({evento.n_participantes} competidores)")
    
    eleccion = int(input("Seleccione un evento: ")) - 1

    if eleccion < 0 or eleccion >= len(manager.eventos):
        print("Opcion invalida.")
        return

    evento = manager.eventos[eleccion]

    if len(manager.participantes) < evento.n_participantes:
        print("No hay suficientes participantes para este evento.")
        return
    
    # Escojemos los competidores
    competidores = random.sample(manager.participantes, evento.n_participantes)

    # Generamos un resultado aleatorio.
    random.shuffle(competidores)

    # Guardamos los resultados
    evento.resultados = competidores

    # Mostramos ganadores
    print(f"Resultados del evento '{evento.nombre}'.")
    print(f"Oro: {competidores[0].nombre} ({competidores[0].pais})")
    print(f"Plata: {competidores[1].nombre} ({competidores[1].pais})")
    print(f"Bronce: {competidores[2].nombre} ({competidores[2].pais})")


def crear_informe():

    medallas = {} # Incializamos antes del bucle

    for evento in manager.eventos:
        if not evento.resultados:
            print(f"El evento '{evento.nombre}' aun no se ha simulado.")
            continue

        if len(evento.resultados) < 3:
            print(f"El evento '{evento.nombre}' no tiene suficientes resultados para asignar medallas.")
            continue

        print(f"\nResultados del evento '{evento.nombre}':")
        print(f"Oro: {evento.resultados[0].nombre} ({evento.resultados[0].pais})")
        print(f"Plata: {evento.resultados[1].nombre} ({evento.resultados[1].pais})")
        print(f"Bronce: {evento.resultados[2].nombre} ({evento.resultados[2].pais})")

        #contar medallas 
        medallas[evento.resultados[0].pais] = medallas.get(evento.resultados[0].pais, 0) + 1
        medallas[evento.resultados[1].pais] = medallas.get(evento.resultados[1].pais, 0) + 1
        medallas[evento.resultados[2].pais] = medallas.get(evento.resultados[2].pais, 0) + 1

    if not medallas:
        print("\nAun no hay medallas registradas.")
        return

    ranking = sorted(medallas.items(), key = lambda x: x[1], reverse = True)
    print("\nRanking de paises por medallas: ")
    for idx, (pais, total) in enumerate(ranking, 1):
        print(f"{idx}. {pais}: {total} medallas")

def functions(o):
     funciones = {
          1: registrar_evento,
          2: registrar_participante,
          3: simular_evento,
          4: crear_informe
     }
     return funciones[o]()

def main():
    while True:
        opcion = menu()
        if opcion == 5:
            print("Saliendo de los juegos olimpicos..")
            break
        elif opcion in [1, 2, 3, 4]:
            functions(opcion)
        else:
             print("Opcion no valida. Intente de nuevo.")

main()