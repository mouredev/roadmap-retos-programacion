# 32 BATALLA DEADPOOL Y WOLVERINE

import time
import random
import pandas as pd


class Batalla:
    """
    Clase que registra ataques.
    """

    def __init__(self):
        self.registro = {}

    def registro_ataque(self, personaje, vida, evita_ataque, numero_ataque=0, dano_max=1, dano_var=0):
        """
        Función que registra un ataque.
        """
        nuevo_registro = {
            "Puntos de vida": vida,
            "Evasión de ataque": evita_ataque,
            "Numero de ataque": numero_ataque,
            "Daño máximo": dano_max,
            "Daño": dano_var
        }
        self.registro[personaje] = nuevo_registro
        print(f"Resultado del ataque de '{personaje}' registrado con éxito.\n")

    def calcular_dano(self, atacante):
        """
        Función que calcula el daño.
        """
        dano_var = round(random.uniform(0.4, atacante["Daño máximo"]), 2)
        return dano_var


simulador_batalla = Batalla()

# Función para mostrar el menú


def menu():
    while True:
        print("Menú:")
        print("1. Asignar puntos de vida")
        print("2. Simular batalla")
        print("3. Resultado final")
        print("4. Salir")
        opcion = input("Ingrese una opción: ")
        try:
            return int(opcion)
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número entero.")


while True:
    opcion = menu()

    if opcion == 1:
        vida_deadpool = int(input("Ingrese puntos de vida de DEADPOOL: "))
        evita_ataque_deadpool = 0.25
        numero_ataque = 0
        dano_max_d = 0.8
        simulador_batalla.registro_ataque(
            "Deadpool", vida_deadpool, evita_ataque_deadpool, numero_ataque, dano_max_d)

        vida_wolverine = int(input("Ingrese puntos de vida de WOLVERINE: "))
        evita_ataque_wolverine = 0.2
        dano_max_w = 0.7
        simulador_batalla.registro_ataque(
            "Wolverine", vida_wolverine, evita_ataque_wolverine, numero_ataque, dano_max_w)

    elif opcion == 2:
        while simulador_batalla.registro["Deadpool"]["Puntos de vida"] > 0 and simulador_batalla.registro["Wolverine"]["Puntos de vida"] > 0:
            for personaje in list(simulador_batalla.registro.keys()):
                atacante = simulador_batalla.registro[personaje]
                defensor = simulador_batalla.registro["Wolverine" if personaje ==
                                                      "Deadpool" else "Deadpool"]

                if random.random() > defensor['Evasión de ataque']:
                    dano = simulador_batalla.calcular_dano(atacante)

                    if dano < atacante["Daño máximo"]:
                        dano_realizado = round(
                            dano * defensor["Puntos de vida"])
                        defensor["Puntos de vida"] -= dano_realizado
                        atacante["Numero de ataque"] += 1
                        print(f"Turno {atacante['Numero de ataque']}: {
                              personaje} ataca y causa {dano_realizado} de daño.")
                        print(f"A {list(simulador_batalla.registro.keys())[1 if personaje == 'Deadpool' else 0]} le quedan {
                              round(defensor['Puntos de vida'], 2)} puntos de vida.")

                        simulador_batalla.registro_ataque(list(simulador_batalla.registro.keys())[
                                                          1 if personaje == 'Deadpool' else 0], defensor["Puntos de vida"], defensor["Evasión de ataque"], defensor["Numero de ataque"], defensor["Daño máximo"], dano)
                    else:
                        atacante["Numero de ataque"] += 1
                        print(f"Turno {atacante['Numero de ataque']}: {
                              personaje} realiza un ataque máximo.")
                        print(f"{list(simulador_batalla.registro.keys())[
                              1 if personaje == 'Deadpool' else 0]} se regenera.")
                        defensor["Puntos de vida"] += random.randint(1, 3)
                        simulador_batalla.registro_ataque(list(simulador_batalla.registro.keys())[
                                                          1 if personaje == 'Deadpool' else 0], defensor["Puntos de vida"], defensor["Evasión de ataque"], defensor["Numero de ataque"], defensor["Daño máximo"], dano)
                else:
                    atacante["Numero de ataque"] += 1
                    print(f"Turno {atacante['Numero de ataque']}.")
                    print(f"{personaje} esquiva el ataque en el turno {
                          atacante['Numero de ataque']}.\n")

                time.sleep(1)

            if simulador_batalla.registro["Deadpool"]["Puntos de vida"] <= 0 or simulador_batalla.registro["Wolverine"]["Puntos de vida"] <= 0:
                break

        if simulador_batalla.registro["Deadpool"]["Puntos de vida"] <= 0:
            print("¡Wolverine gana!")
        else:
            print("¡Deadpool gana!")

    elif opcion == 3:
        resultados = simulador_batalla.registro
        if not resultados:
            print("No hay resultados para mostrar. Primero simula la batalla.")
        else:
            df = pd.DataFrame(resultados).T
            print(df)

    elif opcion == 4:
        print("¡El juego ha finalizado!")
        break
