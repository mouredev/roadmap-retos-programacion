import random
from colorama import Fore, Back, Style, init

# Inicializar colorama
init()


hoja = Back.BLACK + Style.DIM + Fore.GREEN + "*"
tronco = Back.BLACK + Style.DIM + Fore.RED + '|'
estrella = Fore.YELLOW + "@"
bola = Back.BLACK + Style.BRIGHT + Fore.RED + "o"
luz_encendida = Back.BLACK + Style.BRIGHT + Fore.YELLOW + "+"
luz_apagada = Back.BLACK + Style.DIM + Fore.YELLOW + "+"

# Función para dibujar el árbol
def dibujar_arbol(pisos, tiene_estrella, posiciones_bolas, posiciones_luces, luces_encendidas):
    if tiene_estrella:
        print(' ' * (pisos - 1) + estrella)  # Dibuja la estrella
    for i in range(pisos):
        fila = []
        for j in range(2 * i + 1):
            pos = (i, j)
            if pos in posiciones_bolas:  # Coloca bolas
                fila.append(bola)
            elif pos in posiciones_luces:  # Coloca luces
                fila.append(luz_encendida if luces_encendidas else luz_apagada)
            else:  # Hoja normal
                fila.append(hoja)
        # Imprime la fila con espacios
        print(' ' * (pisos - i - 1) + ''.join(fila))
   
    tronco_espacios = ' ' * (pisos - 1)
    for _ in range(2):  # Altura del tronco
        print(tronco_espacios + tronco)


pisos = int(input('Indica número de pisos: '))
tiene_estrella = input('¿Quieres poner la estrella al árbol? (si/no): ').lower() == 'si'
posiciones_bolas = set()
posiciones_luces = set()
luces_encendidas = True

# Funciones para modificar el árbol
def agregar_bolas():
    global posiciones_bolas
    for _ in range(2):  # Añade de dos en dos
        while True:
            fila = random.randint(0, pisos - 1)
            columna = random.randint(0, 2 * fila)
            if (fila, columna) not in posiciones_bolas and (fila, columna) not in posiciones_luces:
                posiciones_bolas.add((fila, columna))
                break

def eliminar_bolas():
    global posiciones_bolas
    for _ in range(2):  # Elimina de dos en dos
        if posiciones_bolas:
            posiciones_bolas.pop()

def agregar_luces():
    global posiciones_luces
    for _ in range(3):  # Añade de tres en tres
        while True:
            fila = random.randint(0, pisos - 1)
            columna = random.randint(0, 2 * fila)
            if (fila, columna) not in posiciones_bolas and (fila, columna) not in posiciones_luces:
                posiciones_luces.add((fila, columna))
                break

def eliminar_luces():
    global posiciones_luces
    for _ in range(3):  # Elimina de tres en tres
        if posiciones_luces:
            posiciones_luces.pop()

def apagar_encender_luces():
    global luces_encendidas
    luces_encendidas = not luces_encendidas

while True:
 
    print("\n--- ÁRBOL ACTUAL ---")
    dibujar_arbol(pisos, tiene_estrella, posiciones_bolas, posiciones_luces, luces_encendidas)

    print("\nOpciones:")
    print("1. Añadir bolas")
    print("2. Eliminar bolas")
    print("3. Añadir luces")
    print("4. Eliminar luces")
    print("5. Apagar/Encender luces")
    print("6. Salir")

    opcion = input("Elige una opción: ")
    if opcion == '1':
        agregar_bolas()
    elif opcion == '2':
        eliminar_bolas()
    elif opcion == '3':
        agregar_luces()
    elif opcion == '4':
        eliminar_luces()
    elif opcion == '5':
        apagar_encender_luces()
    elif opcion == '6':
        break
    else:
        print("Opción no válida.")
