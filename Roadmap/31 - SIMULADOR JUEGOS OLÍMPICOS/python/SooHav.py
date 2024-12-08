# 31 SIMULADOR JUEGOS OLÍMPICOS

import random
import pandas as pd

# Registro de personas


class RegistroPersonas:
    __instance = None

    @staticmethod
    def get_instance():
        if RegistroPersonas.__instance is None:
            RegistroPersonas.__instance = RegistroPersonas()
        return RegistroPersonas.__instance

    def __init__(self):
        self.personas = []

    def registrar_persona(self, nombre, pais, deporte):
        self.personas.append((nombre, pais, deporte))

    def obtener_personas(self):
        return self.personas

# Registro de eventos olímpicos


class RegistroEventos:
    __instance = None

    @staticmethod
    def get_instance():
        if RegistroEventos.__instance is None:
            RegistroEventos.__instance = RegistroEventos()
        return RegistroEventos.__instance

    def __init__(self):
        self.eventos = []

    def registrar_evento(self, descripcion, fecha):
        self.eventos.append((descripcion, fecha))

    def obtener_eventos(self):
        return [evento[0] for evento in self.eventos]

# Simulador de eventos


def simular_podio(participantes, num_ganadores=3):
    if len(participantes) < num_ganadores:
        raise ValueError("No hay suficientes participantes para el podio.")

    random.shuffle(participantes)
    podio = participantes[:num_ganadores]
    categorias = ["Oro", "Plata", "Bronce"]
    return [(participante, categorias[i]) for i, participante in enumerate(podio)]

# Contador de medallas por país


def contar_medallas(resultados):
    conteo_medallas = {}
    for deporte, resultados_deporte in resultados.items():
        for atleta, medalla in resultados_deporte:
            pais = atleta[1]
            if pais not in conteo_medallas:
                conteo_medallas[pais] = {
                    'Oro': 0, 'Plata': 0, 'Bronce': 0, 'Total': 0}
            conteo_medallas[pais][medalla] += 1
            conteo_medallas[pais]['Total'] += 1
    return conteo_medallas

# Función para mostrar el menú


def menu():
    while True:
        print("Menú:")
        print("1. Registrar evento")
        print("2. Registrar persona")
        print("3. Simular podios")
        print("4. Mostrar resultados")
        print("5. Salir")
        opcion = input("Ingrese una opción: ")
        try:
            return int(opcion)
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número entero.")


def menu_resultados():
    while True:
        print("Menú Resultados:")
        print("1. Ranking por países")
        print("2. Ganadores por deportes")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")
        try:
            return int(opcion)
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número entero.")


# Instanciar los registros de personas y eventos
registro_personas = RegistroPersonas.get_instance()
registro_eventos = RegistroEventos.get_instance()

resultados = {}

while True:
    opcion = menu()

    if opcion == 1:
        evento = input("Ingrese el nombre del deporte: ").strip()
        fecha = input("Ingrese la fecha de la final: ")
        registro_eventos.registrar_evento(evento, fecha)

    elif opcion == 2:
        nombre = input("Ingrese el nombre del atleta: ").strip()
        pais = input("Ingrese el país del atleta: ").strip()
        listado_eventos = registro_eventos.obtener_eventos()
        print("¿A que evento se registra?")
        print(f"Deporte: ")
        for deporte in listado_eventos:
            print(f"{deporte}")
        deporte = input("Ingrese el deporte: ").strip()
        registro_personas.registrar_persona(nombre, pais, deporte)

    elif opcion == 3:
        listado_personas = registro_personas.obtener_personas()
        listado_eventos = registro_eventos.obtener_eventos()

        if len(listado_personas) < 3:
            print("Error: Debes registrar al menos 3 atletas.")
        elif len(listado_eventos) < 1:
            print("Error: Debes registrar al menos un evento.")
        else:
            for evento in listado_eventos:
                participantes_evento = random.sample(
                    listado_personas, k=len(listado_personas))
                podio = simular_podio(participantes_evento)
                resultados[evento] = podio
            print("Simulación de podios completada.")

    elif opcion == 4:
        if not resultados:
            print("No hay resultados para mostrar. Primero realiza una simulación.")
        else:
            while True:
                opcion_resultados = menu_resultados()

                if opcion_resultados == 1:
                    conteo = contar_medallas(resultados)
                    data = [{'País': pais, **medallas}
                            for pais, medallas in conteo.items()]
                    df = pd.DataFrame(data)
                    df = df.sort_values(by=['Oro', 'Total'], ascending=False)
                    print(df)

                elif opcion_resultados == 2:
                    for evento, ganadores in resultados.items():
                        print(f"Deporte: {evento}")
                        for atleta, medalla in ganadores:
                            print(f"{medalla}: {atleta[0]} ({atleta[1]})")
                    print()

                elif opcion_resultados == 3:
                    break

    elif opcion == 5:
        print("¡Hasta luego!")
        break
