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

import json
import random

# Inicializar datos
data = {
    "eventos": [],
    "participantes": [],
    "resultados": []
}

# Función para guardar datos en un archivo JSON
def guardar_datos():
    with open('juegos_olimpicos.json', 'w') as archivo:
        json.dump(data, archivo, indent=4)

# Función para registrar eventos
def registrar_evento():
    evento = input("Nombre del evento: ")
    data["eventos"].append(evento)
    guardar_datos()
    print(f"Evento '{evento}' registrado con éxito.")

# Función para registrar participantes
def registrar_participante():
    nombre = input("Nombre del participante: ")
    pais = input("País del participante: ")
    data["participantes"].append({"nombre": nombre, "pais": pais})
    guardar_datos()
    print(f"Participante '{nombre}' de '{pais}' registrado con éxito.")

# Función para simular eventos
def simular_evento():
    if len(data["participantes"]) < 3:
        print("Se necesitan al menos 3 participantes para simular un evento.")
        return

    evento = input("Nombre del evento a simular: ")
    if evento not in data["eventos"]:
        print(f"El evento '{evento}' no está registrado.")
        return

    participantes = random.sample(data["participantes"], 3)
    random.shuffle(participantes)
    medallas = ["oro", "plata", "bronce"]

    resultado = {
        "evento": evento,
        "ganadores": []
    }

    for i in range(3):
        resultado["ganadores"].append({
            "nombre": participantes[i]["nombre"],
            "pais": participantes[i]["pais"],
            "medalla": medallas[i]
        })

    data["resultados"].append(resultado)
    guardar_datos()
    print(f"Evento '{evento}' simulado con éxito.")
    for ganador in resultado["ganadores"]:
        print(f"{ganador['nombre']} de {ganador['pais']} ganó la medalla de {ganador['medalla']}.")

# Función para crear informes
def crear_informe():
    paises = {}
    for resultado in data["resultados"]:
        for ganador in resultado["ganadores"]:
            pais = ganador["pais"]
            medalla = ganador["medalla"]
            if pais not in paises:
                paises[pais] = {"oro": 0, "plata": 0, "bronce": 0}
            paises[pais][medalla] += 1

    print("\nRanking de países según el número de medallas:")
    for pais, medallas in sorted(paises.items(), key=lambda item: (item[1]["oro"], item[1]["plata"], item[1]["bronce"]), reverse=True):
        print(f"{pais}: Oro: {medallas['oro']}, Plata: {medallas['plata']}, Bronce: {medallas['bronce']}")

# Menú interactivo
def menu():
    while True:
        print("\nMenú:")
        print("1. Registro de eventos")
        print("2. Registro de participantes")
        print("3. Simulación de eventos")
        print("4. Creación de informes")
        print("5. Salir del programa")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_evento()
        elif opcion == "2":
            registrar_participante()
        elif opcion == "3":
            simular_evento()
        elif opcion == "4":
            crear_informe()
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el menú
menu()
