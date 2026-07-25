# 39 Batman day

from tkinter import *
from tkinter import ttk
import numpy as np
import calendar
import datetime
# Reto 1


class BatmanDay:
    def __init__(self, root, anio=2039, mes=9):
        self.root = root
        self.root.title("Días para el centenario de Batman")
        self.root.configure(background='black')
        self.root.geometry("600x140")
        self.anio = anio
        self.mes = mes

        # Etiqueta
        self.etiqueta = ttk.Label(self.root, font=("Helvetica", 20),
                                  foreground="yellow", background="black")
        self.etiqueta.pack(pady=20)

        # Estilo
        self.style = ttk.Style()
        self.style.configure(
            'TButton', foreground='yellow', background='black')

        # Botón para cerrar la ventana
        self.boton_apagado = ttk.Button(self.root, text="Cerrar",
                                        style='TButton', command=self.root.destroy)
        self.boton_apagado.pack(pady=10)

        # Calcular los días y mostrar el resultado
        self.mostrar_dias(anio, mes)  # Centenario de Batman

    def tercer_sabado_de_mes(self, anio, mes):
        """
        Calcula la fecha del tercer sábado de un mes dado.
        """
        calendario = calendar.Calendar(firstweekday=calendar.SATURDAY)
        dias_del_mes = calendario.itermonthdates(anio, mes)

        sabados = 0
        for dia in dias_del_mes:
            if dia.weekday() == calendar.SATURDAY:
                sabados += 1
            if sabados == 3:
                return dia

        return None

    def calcular_dias(self, anio, mes):
        """Calcula los días entre la fecha actual y la fecha final."""
        fecha1 = datetime.date.today()
        fecha2 = self.tercer_sabado_de_mes(anio, mes)
        diferencia = (fecha2 - fecha1)
        return diferencia.days

    def mostrar_dias(self, anio, mes):
        """Muestra el número de días restantes."""
        dias_restantes = self.calcular_dias(anio, mes)
        self.etiqueta.config(
            text=f"Faltan {dias_restantes} días para el centenario de Batman")


# Inicializar la aplicación
if __name__ == "__main__":
    root = Tk()
    app = BatmanDay(root)
    root.mainloop()

# Reto 2

# Crear el mapa de ciudad Gothica


def crear_grilla(filas=20, columnas=20, amenaza=10, sensores=0.8):
    if filas < 20 or columnas < 20:
        raise ValueError(
            "La grilla debe tener al menos 20 filas y 20 columnas")

    # Grilla
    grilla = [[None for _ in range(columnas)] for _ in range(filas)]

    # Asignar entrada (🦇)
    fila_entrada = np.random.randint(0, filas)
    columna_entrada = np.random.randint(0, columnas)
    grilla[fila_entrada][columna_entrada] = (fila_entrada, columna_entrada, 0)
    print(f"La baticueva está en {fila_entrada} y {columna_entrada}")

    # Llenar la grilla con celdas sin amenaza y con amenazas detectadas por sensores
    for i in range(filas):
        for j in range(columnas):
            if grilla[i][j] is None:
                if np.random.random() > sensores:
                    grilla[i][j] = (i, j, 0)
                else:
                    nivel_amenaza = np.random.randint(0, amenaza + 1)
                    grilla[i][j] = (i, j, nivel_amenaza)

    return grilla, fila_entrada, columna_entrada

# Encontrar la máxima amenaza de la ciudad


def encontrar_max_amenaza(grilla, fila, columna):
    amenazas = []

    # Poner los límites de la subgrilla
    fila_inicial = max(0, fila - 1)
    fila_final = min(len(grilla), fila + 2)
    columna_inicial = max(0, columna - 1)
    columna_final = min(len(grilla[0]), columna + 2)

    # Subgrilla 3x3
    subgrilla = [grilla[i][columna_inicial:columna_final]
                 for i in range(fila_inicial, fila_final)]

    # Extraer los niveles de amenaza de la subgrilla
    for fil_sub in subgrilla:
        for celda in fil_sub:
            amenazas.append(celda[2])

    # Suma de amenaza de la subgrilla
    suma_amenaza = sum(amenazas)

    return (fila, columna, suma_amenaza) if suma_amenaza >= 20 else None

# Calcular la distancia al punto crítico donde se está produciendo el delito


def calcular_distancia_manhattan(fila, fila_entrada, columna, columna_entrada):
    return abs(fila - fila_entrada) + abs(columna - columna_entrada)

# Mostrar el menú


def menu():
    while True:
        print("Menú:")
        print("1. Generar grilla")
        print("2. Determinar máxima amenaza")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")
        try:
            return int(opcion)
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número entero.")


# Variables globales
grilla = None
fila_bati = None
columna_bati = None

while True:
    opcion = menu()

    if opcion == 1:
        try:
            filas = int(input("Ingrese el número de filas: "))
            columnas = int(input("Ingrese el número de columnas: "))
            amenaza = int(input("Ingrese el nivel máximo de amenaza: "))
            sensores = float(
                input("Ingrese el porcentaje de sensores (entre 0.5 y 1.0): "))
            grilla, fila_bati, columna_bati = crear_grilla(
                filas, columnas, amenaza, sensores)

            for fila in grilla:
                print(fila)
        except ValueError:
            print("Intente nuevamente.")

    elif opcion == 2:
        if grilla is None:
            print("Primero debe generar la grilla.")
        else:
            max_amenaza = None

            for i in range(1, filas - 1):
                for j in range(1, columnas - 1):
                    tupla = encontrar_max_amenaza(grilla, i, j)
                    if tupla is not None:
                        if max_amenaza is None or tupla[2] > max_amenaza[2]:
                            max_amenaza = tupla

            if max_amenaza is not None:
                distancia = calcular_distancia_manhattan(
                    max_amenaza[0], fila_bati, max_amenaza[1], columna_bati)
                print(f"El área donde se desarrolla el crimen está en {
                      max_amenaza[0]} y {max_amenaza[1]}")
                print(f"Con un nivel de amenaza de {
                      max_amenaza[2]} se activó el protocolo de seguridad.")
                print(f"La distancia al punto crítico es {distancia}")
            else:
                print(f"No se detectaron amenazas en la zona ({i}, {j}).")

    elif opcion == 3:
        print("¡Hasta la próxima!")
        break
